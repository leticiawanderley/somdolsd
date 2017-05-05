# -*- coding: utf-8 -*-
import requests, json
from operator import itemgetter

API_KEY = '3f65c66d50219f19adf936214025f697'
USERS = ['danielgem','talitaL','FelipeVF']

def get_top_albums_from_user(user):
	api_call = 'http://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user=' + user + '&api_key=' + API_KEY + '&limit=10&format=json'
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
	api_call = 'http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=' + user + '&api_key=' + API_KEY + '&limit=10&format=json'
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
	api_call = 'http://ws.audioscrobbler.com/2.0/?method=user.getinfo&user=' + user + '&api_key=' + API_KEY + '&format=json'
	try:
		response = requests.get(api_call)
		data = response.json()
		return int(data['user']['playcount'])
	except:
		return -1

def get_top_users():
	top_users = []
	for user in USERS:
		playcount = get_num_of_scrobbles_from_user(user)
		top_users.append({'user':user, 'playcount':playcount})
	return sorted(top_users, key=itemgetter('playcount'), reverse=True)

def get_top_tracks_from_user(user):
	api_call = 'http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user=' + user + '&api_key=' + API_KEY + '&limit=10&format=json'
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
	return sorted(top_tracks, key=itemgetter('playcount'), reverse=True)

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
		print current_user_playing
		if current_user_playing != {}:
			now_playing.append(current_user_playing)
	return now_playing