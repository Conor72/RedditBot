import config
import praw


reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.secret,
    user_agent=config.user_agent,
    username=config.username,
    password=config.password,
)

subreddit = reddit.subreddit("learnpython")
for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")

print(reddit.user.me()) #Print  username