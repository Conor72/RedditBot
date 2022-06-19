import config
import praw


reddit = praw.Reddit(
    client_id=config.client_id,
    client_secret=config.secret,
    user_agent=config.user_agent,
    username=config.username,
    password=config.password,
)


print(reddit.user.me()) #Print  username