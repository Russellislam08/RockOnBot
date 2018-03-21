# RockOnBot

A custom reddit bot that monitors the subreddit r/uwaterloo.
The purpose of the bot is to look for any post that is along the lines of "To the person who is..."
When the bot detects a suitable post, it will reply with "Rock on my dude!"

# Initializing Bot
Before you can use the bot, you must make a reddit account or use an existing one. Within the account, you must create a new script app. The name and description could be whatever you like. To make things easy, you can set the redirect uri as "http://localhost:8080".

# Initializing praw.ini
For the bot to function, there must be a praw.ini file in the same directory as the script itself. Within the .ini file, you must put in the credentials of the app. It should be initialized like this:

[BotName]
client_id = Your Client ID

client_secret = Your Client Secret

password = Your reddit account password

user_agent = A custom user agent. It is easy to just name it something like "RockOn1"

username = Your reddit account username


For consistency, make sure this is written at the end of the praw.ini file and you should be good to go.
