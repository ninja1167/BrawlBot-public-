# BrawlBot-public-
This was forked from the bot in the Brawl server, and changed to work for melee.

If you would like a melee ranked bot for your server,  do the following:
Fork the repository and export it to Replit (or you can use some other hosting service if you want, if it's already a 24/7 service you can delete keepalive.py, loop.py, and restart.py and the code that calls for those in Brawlbot.py)

Make an app in the discord dev portal, add it to your server, and find it's token.

Change the channel ids in lines 24-27 and 30-33 to the channel ids you want for each of those (search channel is where matches are searched for, they are played in match channel (these can be the same channel), misc channel is where miscellaneous commands can go, and mod channel is for mods).

Replace all the emotes in the code with emotes from your own server (the bot can call emotes from any server it's in if it has the permission to).

If you want, you can change the rules command to be whatever you want, and can change the btt command to be something for your server (or just delete it, since that was for a server the bot used to be in).

Use your service's way of setting a secret variable and set your token to a secret variable that is called at the end (in place of my_secret). Change the line of code with my_secret at the top of Brawlbot.py to whatever you need it to be.

Run!

use -helpme to recieve information about the bot.
If you have any trouble, dm ninja1167#2527 on Discord

Note on WIFI: This was forked from the bot of the Brawl server made by APR Financing. There were two different ladders there. However, WIFI is not functional, and there is only one useable ladder. It was just left in the code in some spots.

Note on smashdown: the code doesn't seem to work, and didn't before this was forked either.
