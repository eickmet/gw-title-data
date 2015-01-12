import praw

r = praw.Reddit(user_agent="test_application")
submissions = r.get_subreddit("opensource").get_hot(limit=5)
for x in submissions:
    print type(x)
    print x.title
    print x
