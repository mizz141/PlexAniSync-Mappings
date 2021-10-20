# PlexAniSync-Mappings
This is a collection of [custom-mappings](https://github.com/RickDB/PlexAniSync#custom-anime-mapping "custom-mappings") for the [PlexAniSync](https://github.com/RickDB/PlexAniSync "PlexAniSync") plex addon.

Tested for Plex Scanner and TVDB, not tested with and for other scanners.

Currently Mapped Titles:
- Plex Season And Anilist Entries are respective to each other.
- Plus (+) sign indicates that two Anilist entries have been mapped to a single Plex Season respectively.

|  Title | Type  | Plex  Season |  Anilist Entries| Note|
| ------------ | ------------ | ------------ | ------------ | ------------ |
| 86: Eighty Six  | Series  | S01  | Cour 1 + Cour 2  |  |
| A Certain Scientific Railgun  |  Series | S01, S02, S03  | Railgun, Railgun S, Railgun T  |  |
| A Silent Voice: The Movie  | Movie  | Movie  | A Silent Voice  |  |
| Ascendance of a Bookworm  | Series  | S01  | Cour 1 + Cour 2  |  |
| Attack on Titan  | Series  | S01, S02, S03, S04  | S01, S02, S03P1 + S03P2, S04P1  |  |
|  Cells at Work! | Series  | S01, S02  | Cells at Work!, Cells at Work!!  |  |
|  Clannad | Series  | S01, S02  | Clannad, Clannad After Story  |  |
| Code Geass: Lelouch of the Rebellion  | Series  | S01, S02  | R1, R2  |  |
|  Danganronpa 3: The End of Hope's Peak Academy - Despair Arc | Series  |  S01 | Danganronpa 3: The End of Hope's Peak High School - Despair Arc  |  |
| Demon Slayer | Series | S01, S02 | Demon Slayer: Kimetsu no Yaiba, Demon Slayer: Kimetsu no Yaiba 2| Season 1 is Optional but Season 2 doesn't sync due to Plex and AniList Name differences. |
| Dr. Stone  | Series  | S01, S02  | Dr. Stone, Stone Wars  |  |
| Fate/stay night: Unlimited Blade Works | Series  | S01 | S01+S02  | Anilist Episode 2 mapped to Plex Episode 1 due to TVDB having 25 episodes for S01 and a Special Episode while Anilist has Special Episode included in total episode count,that is,26. |
| Fate/Zero | Series  | S01 | S01+S02  |  |
| Gintama  | Series  | S01-S04, S05, S06, S07, S08, S09, S10  | S01, S02, S03, S04, S05, Slip Arc, Silver Soul Arc + Silver Soul Arc Second Half War   |  |
| JoJo's Bizarre Adventure (2012)  | Series  | S01, S02, S03, S04  | S01, Stardust Crusaders + Egypt Battle, Unbreakable Diamond, Golden Wind |  |
| Kaguya-sama: Love Is War  | Series | S01, S02 |Kaguya-sama: Love Is War, Kaguya-sama: Love Is War? |  |
| Miss Kobayashi's Dragon Maid | Series | S01, S02 | Miss Kobayashi's Dragon Maid, Miss Kobayashi's Dragon Maid S| |
| Monogatari | Series and Movies  | S00, S01, S02, S03, S04, S05  | ***yes***  | ~~S00 for Specials is only a placeholder due to PlexAniSync not recognizing Specials, will get updated when a fix is found.~~ [will never be fixed](https://github.com/RickDB/PlexAniSync/issues/80#issuecomment-944931420) |
| Mushoku Tensei: Jobless Reincarnation  | Series  | S01  | Cour 1 + Cour 2  |  |
|  Re:ZERO -Starting Life in Another World- | Series  | S02 | S02P1, S02P2  |  |
| Shelter | Music | Movie |  Shelter | Music Video released as an Anime. Plex treats it as a Movie. |
| Sword Art Online  | Series  | S01, S02, S03, S04  | I, II, Alicization, Alicization War of Underworld Part 1 + 2|  |
| Symphogear  | Series  | S01, S02, S03, S04, S05 | Symphogear, G, GX, AXZ, XV|  |
| That Time I Got Reincarnated as a Slime | Series | S01, S02 | S01, S02P1 + S02P2 | |
| The Melancholy of Haruhi Suzumiya | Series  | S01  | The Melancholy of Haruhi Suzumiya (2009)  |  |
|  The Rising of the Shield Hero | Series  | S01 | The Rising of the Shield Hero  |  |
|The Slime Diaries| Series | S01 | The Slime Diaries | |
|  Tokyo Ghoul | Series  | S01, S02, S03  | Tokyo Ghoul, √A, re: + re:2  |  |

# Installation on unRAID
First you need to install the PlexAniSync Docker, if you have that already, you can skip this section.

This is easiest done with the [Community Applications](https://forums.unraid.net/topic/38582-plug-in-community-applications/) plugin. (Installation from dockerHub must be enabled).

Enter the Variables according to the [dockerHub](https://hub.docker.com/r/rickdb/plexanisync/)

Configure the Path to be in your AppData folder named "PlexAniSync-Mappings" and create that folder.

**Installation of the Mappings**

You can automate the mappings with a simple script that can be run with the "User Scripts" plugin (also in the Community Applications)

Create a script with a name (preferrably PlexAniSync) and add this:
``` 
#!/bin/bash
rm -r /mnt/user/appdata/PlexAniSync/*
cd /mnt/user/appdata/PlexAniSync
git clone https://github.com/mizz141/PlexAniSync-Mappings.git
docker restart plexanisync
```
The Script will cd into the appdata folder you created, clone the repo, and restart the Docker Container. 

You can set the update interwall to whatever you like, best results are gained with a Daily inteval. It's recommended to test-run the script for any errors, most commonly a misnamed container or wrong filepath.

Credits to [Randy Chen](https://github.com/ZhunCn) for the Script and Installation instructions.
