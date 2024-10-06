import os, sys, tvdb_v4_official, yaml
from dotenv import load_dotenv
from pathlib import Path

# Load API Key and initialize tvdb
load_dotenv(Path(".env"))
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

def validateShowSeason(showName, seasonNumber):
    foundSeason = False
    hasError = False

    showId = getTvdbId(showName)

    if (showId is None):
        print("No TVDB series result: " + showName)
        return
    print("Found show: " + showName + " with tvdb id: " + showId)
    # Check if official season number exists for the show in TVDB
    series = tvdb.get_series_extended(showId) # TODO: does not work for primary_type: movie, maybe separate method for those?
    for season in sorted(series["seasons"], key=lambda x: (x["type"]["type"], x["number"])):
        # print(season)
        if season["type"]["type"] == "official" and season["number"] == seasonNumber:
            season = tvdb.get_season_extended(season["id"])
            break
        else:
            season = None

    if season is not None:
        foundSeason = True
        print("Found season: " + str(seasonNumber))
    else:
        hasError = True
        print("Did not find season: " + str(seasonNumber))

    if hasError:
        # print("The following show to season mappings were not found on TVDB:")
        # print(mismatchMap)
        sys.exit(1)

# TODO: get only PR changes of newly added seasons
def validateAllMappings():
    with open("custom_mappings.yaml") as f:
        mappings = yaml.safe_load(f)
        for show in sorted(mappings['entries'], key=lambda entry: (entry['title'], entry['seasons'])):
            showName = show['title']
            seasons = [s['season'] for s in show['seasons'] if 'season' in s]
            # print(showName + ": " + str(seasons))
            for season in seasons:
                validateShowSeason(showName, season)

# TODO: cross reference anilist-id show name
validateShowSeason("The Heroic Legend of Arslan (2015)", 1)
# validateAllMappings()
