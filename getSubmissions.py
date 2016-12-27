import praw
import config
import sys
import getopt
import json
import datetime
import time

client_id = config.REDDIT_CLIENT_ID
client_secret = config.REDDIT_CLIENT_SECRET
username = config.REDDIT_USERNAME
password = config.REDDIT_PASSWORD
useragent = "python.praw" + config.REDDIT_APP_NAME + ':' + config.REDDIT_APP_VERSION + " (by /u/" + username + ")"

try:
    opts, args = getopt.getopt(sys.argv[1:],"i:")
except getopt.GetoptError:
    print("can't get subreddit name")
    sys.exit(2)
for opt, arg in opts:
    if opt == "-i":
        subreddit_name = arg
        print(subreddit_name)

reddit = praw.Reddit(client_id= client_id, client_secret = client_secret,
    password = password, user_agent = useragent, username = username)

subreddit_instance = reddit.subreddit(subreddit_name)
base_data_file_name = "reddit-" + subreddit_name

def convert_submission_to_dict(submission):
    return {
        "language" : "en",
        "source" : "reddit",
        "url" : submission.permalink,
        "title" : submission.title,
        "article_id" : submission.id,
        "text_blob" : submission.selftext,
        "pub_datetime" : submission.created_utc,
        "author" : submission.author.name,
        # "comments" : [x.id for x in submission.comments.list()]
    }

datasets_submissions_entries = []
i = 0
for submission in subreddit_instance.submissions():
    try:
        datasets_submissions_entries.append(submission)
        i = i+1
        if(i % 1000 == 0 and i > 0):
            print(i)
            startdate = datasets_submissions_entries[0].created_utc
            enddate = submission.created_utc
            filename = base_data_file_name + "-submissions-" + str(round(startdate)) + "-" + str(round(enddate))
            # with open(("data/" + filename + ".pickle"), 'wb') as f:
            #     pickle.dump(datasets_submissions_entries, f)
            # print(datasets_submissions_entries)
            json_data = [convert_submission_to_dict(x) for x in datasets_submissions_entries]
            print(json_data)
            with open(("data/" + filename + ".json"), "w", encoding='utf8') as outfile:
                json.dump(json_data, outfile, ensure_ascii=False)
            datasets_submissions_entries = []
    except Exception as e:
        print(type(e))
        print('Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))

if (i > 0 and len(datasets_submissions_entries) > 0) :
    print(i)
    startdate = datasets_submissions_entries[0].created_utc
    enddate = datasets_submissions_entries[len(datasets_submissions_entries) -1].created_utc
    filename = base_data_file_name + "-submissions-" + str(startdate) + "-" + str(enddate) + ".json"
    json_data = [convert_submission_to_dict(x) for x in datasets_submissions_entries]
    with open(("data/" + filename + ".json"), "w", encoding='utf8') as outfile:
        json.dump(json_data, outfile, ensure_ascii=False)
