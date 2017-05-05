#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import lastfm

app = Flask(__name__)

@app.route('/top_users', methods=["GET"])
def top_users():
	return jsonify(lastfm.get_top_users())

@app.route('/top_artists', methods=["GET"])
def top_artists():
	return jsonify(lastfm.get_top_artists())

@app.route('/top_albums', methods=["GET"])
def top_albums():
	return jsonify(lastfm.get_top_albums())

@app.route('/top_tracks', methods=["GET"])
def top_tracks():
	return jsonify(lastfm.get_top_tracks())

@app.route('/now_playing', methods=["GET"])
def now_playing():
	return jsonify(lastfm.get_now_playing())

if __name__ == '__main__':

	app.run(host="10.30.0.33", port=8080, debug=True)