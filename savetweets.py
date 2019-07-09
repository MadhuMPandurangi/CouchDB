from TweetStore import TweetStore
from TwitterAPI.TwitterAPI import TwitterAPI


COUCH_DATABASE = 'twitter'
TWITTER_ENDPOINT = 'statuses/filter'
TWITTER_PARAMS = {'track':'@aprameya_n'}

API_KEY = "hKZR0AnC9nN0fJa66yF0R99Xg"
API_SECRET = "MJZJUDwYR3RW08RC699a4alCTDeCuSi7j6AQ2MJzCKkLAVKmeO"
ACCESS_TOKEN = "3119537052-rOmgBkCV4EzoIVd3HileGAD9HG0MKOBjXM3iWvf"
ACCESS_TOKEN_SECRET = "JVDiF3si82Moej77CfVjGHgaRV8alKMry7Kp6fzBrZhwE "

storage = TweetStore(COUCH_DATABASE)

api = TwitterAPI(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


for item in api.request(TWITTER_ENDPOINT, TWITTER_PARAMS):
	if 'text' in item:
		print('%s -- %s\n' % (item['user']['screen_name'], item['text']))
		storage.save_tweet(item)
	elif 'message' in item:
		print('ERROR %s: %s\n' % (item['code'], item['message']))
