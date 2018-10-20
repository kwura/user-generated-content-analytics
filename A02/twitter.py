from tweepy import OAuthHandler
import tweepy
import csv
import sys
import datetime

api_key="dNm8C29HpvurD0TeuaJXzOYfK"
api_secret_key="QP2RGyOLW7XuToa8vCqLAWVJxKsjOjME6ZFnP4Y3sHt5X66qG4"
atoken="147355411-IaF0fsHK5ynd0wU3UKafHYJgPRHpJUUApMB8DEJA"
asecret="Yq2fKqeQclrmOPa6pRwy1oMKignOB9KQuOjOdpbphlL8I"
auth = OAuthHandler(api_key, api_secret_key)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

# Making dictionary to translate emoji's in order to print to terminal
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

#file names - commented out file names have already been used
#file_name = 'tweets.csv'
#file_name = 'tweets2.csv'
#file_name = 'tweets3.csv'
file_name = 'tweets4.csv'

out_file = open('/Users/barrettpoth/Google Drive/School/MIS 381N - User Generated Content Analytics/Assignments/02 - Twitter/' + file_name, "w")
writer = csv.writer(out_file)
writer.writerow(["id", "location", "text"])

# queries - commented out queries have already been used
# query = 'Texas Senate Race'
#query = 'texas senate'
query = '#Texas Senate Race'

all_tweets = tweepy.Cursor(api.search, q=query).items()

for tweet in all_tweets:
	out_tweets = [tweet.id_str, tweet.user.location, tweet.text.encode("utf-8")]
	writer.writerow(out_tweets)
	print(out_tweets)
out_file.close()