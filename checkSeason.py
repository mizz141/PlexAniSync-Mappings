import os, sys, tvdb_v4_official
from dotenv import load_dotenv
from pathlib import Path

# Load API Key and initialize tvdb
load_dotenv(Path(".env"))
apikey = os.getenv("TVDB_API_KEY")
tvdb = tvdb_v4_official.TVDB(apikey)

# TODO: iterate through PR changes of newly added seasons, and run the following for each show/season

showName = "KamiErabi GOD.app"
seasonNumber = 2
foundSeason = False

# Get ID of show
showId = None
searchResults = tvdb.search(showName)
for result in searchResults:
    print(result['translations']['eng'])
    if ((showName == result['name']) or
        ('aliases' in result and showName in result['aliases']) or
        ('translations' in result and 'eng' in result['translations'] and showName == result['translations']['eng'])
        ):
        showId = result['tvdb_id']

if (showId is None):
    sys.exit("Did not find result for show title: " + showName)
else:
    print("Found show: " + showName + " with id: " + showId)

# fetching a season's episode list
series = tvdb.get_series_extended(showId)
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
    sys.exit("Did not find season: " + str(seasonNumber))
