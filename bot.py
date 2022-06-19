import config
import praw
import pdb
import re
import os



reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.secret,
    user_agent=config.user_agent,
    username=config.username,
    password=config.password,
)

# If this file does not exist, create "txt" file.
if not os.path.isfile("posts_replied_to.txt"): 
    posts_replied_to = []
# If file does exist read the file.
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

# Settings for subreddit "pythonforengineers".
subreddit = reddit.subreddit('pythonforengineers')
# Check first "Hot" 10 submissions in pythonforengineers. Limit= can be changed to number of submissions.
# Hot can be changed to other filters such as "new" or "top".
for submission in subreddit.hot(limit=10):
    # Check if submission.id is NOT in "txt" file.
    if submission.id not in posts_replied_to:
        print("Title: ", submission.title)
        # Searching for Keywords, if found "Replies" with message.
        if re.search("i love python", submission.title, re.IGNORECASE):
            submission.reply("I hecking love python")
            print("Bot replying to : ", submission.title)
            posts_replied_to.append(submission.id)

# Adds submission.id to "txt" file after replying to post.
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

