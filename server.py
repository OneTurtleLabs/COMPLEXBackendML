import requests
import json
import time

# The base url for the Twitch API
BASE_URL = 'https://api.twitch.tv/kraken'
# The version of the API being used
API_VERSION = 'v3'
# Client ID for application
CLIENT_ID = '4ng71gqx25e27yig6whdsbkgx3q2my8'
# Number of seconds between api calls
SAVE_PERIOD = 2
# Number of featured streams to get (MAX 100)
FEAT_LIMIT = 100

# Will return a dictionary of featured streams
def get_featured_streams(headers):

	params = {
		'limit': FEAT_LIMIT,
	}

	res = requests.get(BASE_URL + '/streams/featured', headers = headers, params = params)
	if res.status_code == 200:
		return json.loads(res.content)
	else:
		print 'Wrong request returned with status code: ' + str(res.status_code)
		return None

# Save stream data
def save_featured_streams(headers):

	response = get_featured_streams(headers)
	featured = response['featured']


	if featured is not None:
		for feature in featured:
			stream = feature['stream']

# runs
if __name__ == '__main__':

	# Headers for every request
	headers = {
		'Accept': 'application/vnd.twitchtv.' + API_VERSION + '+json',
		'Client_ID': CLIENT_ID,
	}

	# Value that helps compensated for time drift
	prev_time = time.time()
	iteration = 0

	# Event loop
	while True:
		time.sleep(SAVE_PERIOD - (time.time() - prev_time))
		prev_time = time.time()
		save_featured_streams(headers)
		iteration += 1
		print 'Iteration: ' + str(iteration) + ' on ' + time.ctime()