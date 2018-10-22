'''
rockon.py
When someone posts on r/uwaterloo something along the lines of, "To the person who's being disruptive...",
This bot automatically replies with, "Rock on my dude!"
'''

import praw
import os
import re
from time import sleep

reddit = praw.Reddit("RockOnBot") #In your praw.ini file, create a new bot named whatever you prefer, in this case, I used RockOnBot. In that bot, input the following information:
                                  #client_id, client_secret, password, username, user_agent. Make sure this file is placed in the same directory as rockon.py

'''
If you want to verify that your .ini file is correct and that your bot is able to authenticate, you can write the following line of code:
print (reddit.user.me())
If successful, the program should output the name of the reddit account which the script is being run on
Else, PRAW will return an error
'''

if not os.path.isfile("posts_replied_to.txt"): #A text file within the same directory as the script. This file contains all the submission IDs of which the bot has already replied to.
    posts_replied_to = []                      #Creates an empty list if there are no submission IDs within the text file.
else:
    with open("posts_replied_to.txt", "r") as F:         #This block of code reads the text file with the IDs and puts them in a list.
        posts_replied_to = F.read()                      #This will be used later on so that any submission ID retrieved by the bot can be checked with a database of IDs to determine
        posts_replied_to = posts_replied_to.split("\n")  #Whether the bot replied to the post already or not
        posts_replied_to = list(posts_replied_to)

subreddit = reddit.subreddit("uwaterloo")

while True:                                                                                                                           #Infinite while loop
    for submission in subreddit.new(limit=3):                                                                                         #Limit is 3, to prevent itself from being redundant. Can be changed
        if submission.id not in posts_replied_to:                                                                                     #Compares submission ID with all the IDs in the list, if it's not within the list, it will be assessed
            if re.search("to the", submission.title, re.M.IGNORECASE) or re.search("to my", submission.title, re.M.IGNORECASE):       #re.M.IGNORECASE means to always parse text from the start of title, while ignoring case
                submission.reply("Rock on my dude!")                                                                                  #This is so that if any post has "To the" in other parts of the title, those will be ignored
                print ("Replied to post: " + submission.id)                                                                           #Prints to console, for user
                posts_replied_to.append(submission.id)                                                                                #Appends submission ID to list
                with open("posts_replied_to.txt", "a") as F:
                    F.write(submission.id + "\n")                                                                                     #Writes the submission ID to the text file to create an external database of all posts replied to

        elif submission.id in posts_replied_to:
            print ("Already to replied to post: " + submission.id)          #If the post was already replied to, prints to console for user as well

    sleep(20) #The sleeper can be as long as you prefer. To prevent any ratelimit errors, do not make this value too small. Anything above 5 should be fine
