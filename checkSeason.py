import os, sys, tvdb_v4_official
from dotenv import load_dotenv
from pathlib import Path

# Load API Key and initialize tvdb
load_dotenv(Path(".env"))
apikey = os.getenv("TVDB_API_KEY")
tvdb = tvdb_v4_official.TVDB(apikey)

# TODO: iterate through PR changes of newly added seasons, and run the following for each show/season

showName = "My Hero Academia"
seasonNumber = 8
foundSeason = False

# Get ID of show
showId = None
searchResults = tvdb.search(showName)
# print(searchResults)
for result in searchResults:
    # print(result)
    if showName == result['name']:
        showId = result['tvdb_id']
    elif 'aliases' in result and showName in result['aliases']:
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
