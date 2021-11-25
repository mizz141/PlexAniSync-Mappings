# PlexAniSync-Mappings
This is a collection of [custom-mappings](https://github.com/RickDB/PlexAniSync#custom-anime-mapping "custom-mappings") for the [PlexAniSync](https://github.com/RickDB/PlexAniSync "PlexAniSync") plex addon.

Tested for maximum compatibility TVDB, TMDB and the new Plex Scanner.

Currently Mapped Titles:
- Plex Season and Anilist Entries are respective to each other.
- Plus (+) sign indicates that two Anilist entries have been mapped to a single Plex Season respectively.
- TVDB Specials cannot be matched with custom mappings due to [PlexAniSync not supporting Season 0/Specials](https://github.com/RickDB/PlexAniSync/issues/80#issuecomment-944931420).
- You may need to change titles on some mappings if it changes on TheTVDB or you tweak your Plex entry.

# Discord Server

We have set-up a [Discord Server](https://discord.gg/8vcnkkhguf) for questions, contributions and chitchat.

# Installation on unRAID
First you need to install the PlexAniSync Docker, if you have that already, you can skip this section.

This is easiest done with the [Community Applications](https://forums.unraid.net/topic/38582-plug-in-community-applications/) plugin. (Installation from dockerHub must be enabled).
*NOTE: The Official version isn't updated anymore, I suggest getting [this version](https://hub.docker.com/repository/docker/mizz141/plexanisync-mizz141) instead.* 

Enter the Variables according to the [dockerHub](https://hub.docker.com/repository/docker/mizz141/plexanisync-mizz141)

Configure the Path to be in your AppData folder named `PlexAniSync-Mappings`.

**Installation of the Mappings**

You can automate the mappings with a simple script that can be run with the "User Scripts" plugin (also in the Community Applications)

In the unRAID webterminal, input the following commands to clone the git repository:

```
cd /mnt/user/appdata/
mkdir PlexAniSync
cd PlexAniSync
git clone https://github.com/mizz141/PlexAniSync-Mappings.git
```
This will create a `PlexAniSync-Mappings` directory in your appdata share as a nested folder of the PlexAniSync docker and copy all files from the repository into this directory.

You may need to configure default git configurations for it to pull automatically without any additional arguments on the `git pull` command. If you are never going to make changes with the repository and only want to grab changes, you should input the following command in your unRAID webterminal to only fast forward your repository whenever there are new changes:

```
git config --global pull.ff only
```

You can configure this configuration manually by editing the `~/.gitconfig` file. If you have only ran this configuration command, then the content of your config file is:

```
[pull]
        ff = only
```

Now, to finally automate the whole process, create a script with a name (preferrably `PlexAniSync`) and add this:
```
#!/bin/bash
cd /mnt/user/appdata/PlexAniSync/PlexAniSync-Mappings
git pull origin master
docker restart plexanisync-mizz141
```
The Script will cd into the appdata folder you created, pull the latest changes for the repository from GitHub, and restart the Docker Container.

You can set the update interval to whatever you like, best results are gained with a Daily interval. It's recommended to test-run the script for any errors, most commonly a misnamed container or wrong filepath.

Credits to [Randy Chen](https://github.com/ZhunCn) for the Script and Installation instructions.
