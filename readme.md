# Reddit_api_scraper: using reddit's api to get textual data around subreddits

## Requirements:  
- Python 3.3+  
- [PRAW 4.1.0](https://praw.readthedocs.io)
- reddit user account
- reddit api keys

## Purpose:  
This is a (work in progress) script which let you pull in posts and their subsequent comment from subreddits, and save it to json.

## Setup:
1. make sure you have praw (reddit api wrapper) and boto3 (to write to s3) installed.
2. save `config.example.py` as `config.py` with your own api keys
3. to get submissions for a subreddit, run `getSubmissions.py` with the argument <subreddit name> to the terminal via `-i`, e.g. `python getSubmissions.py -i dataisbeautiful`
4. this will save the submissions to a series of json files in the data directory, with the name to be `reddit-[subreddit_name]-submissions-[timestamp of first entry]-[timestamp of last entry]`, e.g. `reddit-dataisbeautiful-submissions-1464039126-1460036691.json`

* if you don't want to setup/save to s3 then modify the save_to_s3 bit...
