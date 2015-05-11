from pymongo import MongoClient
import operator

client = MongoClient('localhost', 27017)
db = client.twitchml
streams = db.streams

def run():
	channels = dict()

	for stream in streams.find():
		name = stream['channel']['name']

		if not channels.has_key(name):
			channels[name] = 1
		else:
			channels[name] += 1

	sorted_x = sorted(channels.items(), key = operator.itemgetter(1))

	print sorted_x

run()

"""
sodapoppin
riotgames
nl_kripp
dreamhackcs
aphromoo
tsm_theoddone
pcgamer
dreamhacksc2
showdownsmash
bigfoltz
"""