import requests, json
from datetime import datetime
from pymongo import MongoClient
from kafka import KafkaProducer

# TODO: Fetch this from database
API_KEY = '3f65c66d50219f19adf936214025f697'
DATABASE = MongoClient().dataset
PRODUCER = KafkaProducer()

def playing_now_from_user(user):
	api_call = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=' + user + '&api_key=' + API_KEY + '&limit=10&format=json'
	now_playing = {}
	try:
		response = requests.get(api_call)
		data = response.json()
		last_track = data['recenttracks']['track'][0]
		if '@attr' in last_track:
			if last_track['@attr']['nowplaying'] == 'true':
				now_playing['user_name'] = user
				now_playing['music_name'] = last_track['name']
				now_playing['artist_name'] = last_track['artist']['#text']
				now_playing['album_name'] = last_track['album']['#text']
				return now_playing
	except:
		pass
	return now_playing

def get_song_tags(track, artist):
	api_call = 'http://ws.audioscrobbler.com/2.0/?method=track.getTopTags&api_key=' + API_KEY + '&artist=' + artist + '&track=' + track + '&limit=10&format=json'
	try:
		response = requests.get(api_call)
		return response.json()
	except:
		pass

def get_artist_tags(artist):
	api_call = 'http://ws.audioscrobbler.com/2.0/?method=artist.getTopTags&api_key=' + API_KEY + '&artist=' + artist + '&limit=10&format=json'
	try:
		response = requests.get(api_call)
		return response.json()
	except:
		pass

if __name__ == '__main__':
	while True:
		cursor_users = DATABASE.users.find()
		cursor_users.rewind()		

		# Iterate over every single user stored on database
		for document in cursor_users:
			username = document["last_fm_username"]
			last_song_info = playing_now_from_user(username) 
			if len(last_song_info) > 0:		
				last_played_song = DATABASE.users.find_one({"last_fm_username" : username})["last_played_song"]
				# TODO: Check time (users can listen to the same song multiple times)
				# TODO: Check if there's more than one song to be processed
				if last_played_song != "%s - %s" % (last_song_info["music_name"], last_song_info["artist_name"]):	

					# Updating user last_song for control purposes
					result = DATABASE.users.update_one(
					    {"last_fm_username": username},
					    {
					        "$set": {
					            "last_played_song": "%s - %s" % (last_song_info["music_name"], last_song_info["artist_name"])
					        },
					    }
					)	

					# Increment last listening activity
					last_song_info["listening_time"] = datetime.now().isoformat()
					try:
						last_song_info["tags"] =  get_song_tags(last_song_info["music_name"], last_song_info["artist_name"])["toptags"]["tag"]
					except:
						pass
					last_song_info["user"] = document["name"]

					# Storing listening activity
					DATABASE.tracks.insert_one(
						last_song_info
					)

					# Send new listening activity to kafka producer
					PRODUCER.send('test', str(last_song_info) )

					