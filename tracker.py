import praw
import pandas as pd

reddit = praw.Reddit(client_id="********",
                     client_secret="*******",
                     user_agent="RedditScrapper",
                     username="kugeltheblitz",
                     password="********")

flairs = ["******"]

subreddit = reddit.subreddit('UIUC')
topics_dict = {"title": [], "comms_num": [], "body": [], }

for flair in flairs:

    get_subreddits = subreddit.search(flair, limit=None)
    for submission in get_subreddits:
        topics_dict["title"].append(submission.title)
        topics_dict["comms_num"].append(submission.num_comments)
        topics_dict["body"].append(submission.selftext)

new_data = pd.DataFrame(topics_dict)

new_data.to_csv("housing.csv")
