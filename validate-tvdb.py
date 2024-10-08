import os, sys, subprocess
import tvdb_v4_official, yaml
from dotenv import load_dotenv
from pathlib import Path

# Load API Key and initialize tvdb
load_dotenv()
apikey = os.getenv("TVDB_API_KEY")
tvdb = tvdb_v4_official.TVDB(apikey)

def getTvdbId(showName):
    # Get TVDB ID of show
    showId = None
    searchResults = tvdb.search(showName)
    for result in searchResults:
        if ((showName == result['name']) or
            ('aliases' in result and showName in result['aliases']) or
            ('translations' in result and 'eng' in result['translations'] and showName == result['translations']['eng'])
            ) and result['primary_type'] == "series":
            # print(result)
            showId = result['tvdb_id']
            break
    return showId

# Validate user-mapped season entries against TVDB seasons
def validateShowSeasons(showName, seasonsToFind):
    errors = 0

    showId = getTvdbId(showName)

    if (showId is None):
        print("No TVDB series result: " + showName)
        return errors
    # TODO: does not work for primary_type: movie, maybe separate method for those? Test with 5cm per second
    series = tvdb.get_series_extended(showId)
    tvdbSeasons = [season['number'] for season in series['seasons'] if season['type']['type'] == 'official']

    # print("Found show: " + showName + " (" + showId + "), with seasons: " + str(tvdbSeasons))
    # print("Validating user-mapped seasons: " + str(seasonsToFind))
    invalidSeasons = []
    for s in seasonsToFind:
        if s not in tvdbSeasons:
            errors += 1
            invalidSeasons.append(s)

    if errors > 0:
        print("Did not find season(s): " + str(invalidSeasons) + " in show: " + showName)
    return errors

def validateMappings():
    errors = 0
    with open("temp.yaml") as f:
        mappings = yaml.safe_load(f)
        for show in sorted(mappings['entries'], key=lambda entry: (entry['title'], entry['seasons'])):
            showName = show['title']
            seasons = [s['season'] for s in show['seasons'] if 'season' in s]
            print("Validating: " + showName + ": " + str(seasons))
            errors += validateShowSeasons(showName, seasons)
    return errors

def get_diff(file_path, commit_old='origin/master', commit_new='HEAD'):
    diff_output = subprocess.run(
        ['git', 'diff', '-U20', commit_old, commit_new, '--', file_path],
        capture_output=True, text=True
    )
    return diff_output.stdout

def extract_changed_groups(diff_output):
    changes = []
    change_group = []
    for line in diff_output.splitlines():
        if line.startswith('+') and not line.startswith('+++'):  # Added lines
            # Add change group and reset it
            if change_group and "title:" in line and "season:" in str(change_group):
                changes.append(change_group)
                change_group = []
            change_group.append(f"{line[1:]}")
        elif line.startswith('-') and not line.startswith('---'):  # Removed lines
            pass
        elif line.startswith(' '): # Unchanged lines
            # Add change group and reset it
            if change_group and "title:" in line and "season:" in str(change_group):
                changes.append(change_group)
                change_group = []
            # Append intermediary line if existing change_group exists
            elif change_group:
                change_group.append(f"{line[1:]}")
    if not changes:
        print("No season mapping changes detected in the latest commit")
        sys.exit()
    return changes

def extractNewMappings():
    diff_output = get_diff("custom_mappings.yaml")
    change_groups = extract_changed_groups(diff_output)
    createTempYaml(change_groups)

# Create new yaml with changed entries
def createTempYaml(change_groups):
    lines = []
    lines.append("entries:\n")
    for group in change_groups:
        if "title:" not in str(group):
            # TODO: search full mappings to find the context
            continue
        for line in group:
            lines.append(line+"\n")
    with open('temp.yaml', 'w') as file:
        file.write(''.join(lines))

def cleanup():
    os.remove("temp.yaml")

# TODO: cross reference anilist-id show name
extractNewMappings()
errors = validateMappings()
if errors != 0:
    sys.exit("Found "+ str(errors) + " error(s) in the season mappings")
cleanup()