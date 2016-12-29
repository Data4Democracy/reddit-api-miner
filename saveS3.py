import boto3
import config
boto_session = boto3.session.Session(profile_name = config.AWS_PROFILE_NAME)
s3 = boto_session.resource('s3')
reddit_bucket = s3.Bucket(config.AWS_BUCKET_NAME)

def save_to_s3(filename, data):
    reddit_bucket.put_object(Key=filename, Body=data)
