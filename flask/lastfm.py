# -*- coding: utf-8 -*-
import requests, json
from operator import itemgetter
from pymongo import MongoClient
import time

API_KEY = '3f65c66d50219f19adf936214025f697'
WEEK_UNIX_DIFFERENCE = 604800

DATABASE = MongoClient().dataset
cursor = DATABASE.users.find()

USERS = [user['last_fm_username'] for user in cursor]

def get_top_albums_from_user(user):
	api_call = 'http://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user=' + user + '&api_key=' + API_KEY + '&period=7day&limit=10&format=json'
	filtered_rank = []
	try:
		response = requests.get(api_call)
		data = response.json()
		top_albums = data['topalbums']['album']
		for album in top_albums:
			current_album = {'name':album['name'],'artist_name':album['artist']['name'],'playcount':int(album['playcount'])}
			filtered_rank.append(current_album)
		return filtered_rank
	except:
		return []

def get_top_albums():
	top_albums = []
	for user in USERS:
		top_albums_from_user = get_top_albums_from_user(user)
		for current_top_album in top_albums_from_user:
			found = False
			for album in top_albums:
				if album['name'] == current_top_album['name']:
					album['playcount'] += current_top_album['playcount']
					found = True
					break
			if not found:
				top_albums.append(current_top_album)
	return sorted(top_albums, key=itemgetter('playcount'), reverse=True)

def get_top_artists_from_user(user):
	api_call = 'http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=' + user + '&api_key=' + API_KEY + '&period=7day&limit=10&format=json'
	filtered_rank = []
	try:
		response = requests.get(api_call)
		data = response.json()
		top_artists = data['topartists']['artist']
		for artist in top_artists:
			current_artist = {'name':artist['name'],'playcount':int(artist['playcount'])}
			filtered_rank.append(current_artist)
		return filtered_rank
	except:
		return []

def get_top_artists():
	top_artists = []
	for user in USERS:
		top_artists_from_user = get_top_artists_from_user(user)
		for current_top_artist in top_artists_from_user:
			found = False
			for artist in top_artists:
				if artist['name'] == current_top_artist['name']:
					artist['playcount'] += current_top_artist['playcount']
					found = True
					break
			if not found:
				top_artists.append(current_top_artist)
	return sorted(top_artists, key=itemgetter('playcount'), reverse=True) 

def get_num_of_scrobbles_from_user(user):
	until = int(time.time())
	since = until - WEEK_UNIX_DIFFERENCE
	api_call = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=' + user + '&api_key=' + API_KEY + '&from=' + str(since) + '&to=' + str(until) + '&limit=1&format=json'
	try:
		response = requests.get(api_call)
		data = response.json()
		return int(data['recenttracks']['@attr']['total'])
	except:
		return -1

def get_top_users():
	top_users = []
	for user in USERS:
		playcount = get_num_of_scrobbles_from_user(user)
		top_users.append({'user':user, 'playcount':playcount})
	return sorted(top_users, key=itemgetter('playcount'), reverse=True)

def get_top_tracks_from_user(user):
	api_call = 'http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user=' + user + '&api_key=' + API_KEY + '&period=7day&limit=10&format=json'
	filtered_rank = []
	try:
		response = requests.get(api_call)
		data = response.json()
		top_tracks = data['toptracks']['track']
		for track in top_tracks:
			current_track = {'name':track['name'],'artist_name':track['artist']['name'],'playcount':int(track['playcount'])}
			filtered_rank.append(current_track)
		return filtered_rank
	except:
		return []

def get_top_tracks():
	top_tracks = []
	for user in USERS:
		top_tracks_from_user = get_top_tracks_from_user(user)
		for current_top_track in top_tracks_from_user:
			found = False
			for track in top_tracks:
				if track['name'] == current_top_track['name']:
					track['playcount'] += current_top_track['playcount']
					found = True
					break
			if not found:
				top_tracks.append(current_top_track)
	top_tracks = sorted(top_tracks, key=itemgetter('playcount'), reverse=True)
	return top_tracks

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

def get_now_playing():
	now_playing = []
	for user in USERS:
		current_user_playing = playing_now_from_user(user)
		if current_user_playing != {}:
			now_playing.append(current_user_playing)
	return now_playing

def get_top_tag_from_song(artist_name, song_name):
	api_call = 'http://ws.audioscrobbler.com/2.0/?method=track.gettoptags&api_key=' + API_KEY + '&artist=' + artist_name + '&track=' + song_name + '&format=json'
	tag = {}
	try:
		response = requests.get(api_call)
		data = response.json()
		tags = data['toptags']['tag']
		if len(tags) > 0:
			return tags[0]
		else:
			return {}
	except:
		pass
	return tag

def get_top_tags_from_user(user, limit):
	api_call = 'http://ws.audioscrobbler.com/2.0/?method=user.getrecenttracks&user=' + user + '&api_key=' + API_KEY + '&limit=' + limit + '&format=json'
	now_playing = {}
	top_tags = []
	try:
		response = requests.get(api_call)
		data = response.json()
		tracks = data['recenttracks']['track']
		for track in tracks:
			found = False
			tag = get_top_tag_from_song(track['artist']['#text'], track['name'])
			if tag != {}:
				for current_tag in top_tags:
					if current_tag['name'] == tag['name']:
						current_tag['playcount'] += 1
						found = True
						break
				if not found:
					top_tags.append({'name':tag['name'],'playcount':1})
		return sorted(top_tags, key=itemgetter('playcount'), reverse=True)
	except:
		return top_tags
	return top_tags

def get_top_tags():
	top_tags = []
	for user in USERS:
		current_tags = get_top_tags_from_user(user,'10')
		for tag in current_tags:
			found = False
			for current_tag in top_tags:
				if current_tag['name'] == tag['name']:
						current_tag['playcount'] += tag['playcount']
						found = True
						break
			if not found:
				top_tags.append({'name':tag['name'],'playcount':tag['playcount']})
	return sorted(top_tags, key=itemgetter('playcount'), reverse=True)

def get_artists_to_add():
	return [artist['name'] for artist in get_top_artists()][:5]