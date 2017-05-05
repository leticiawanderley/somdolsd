#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import requests
from flask import Flask, request, jsonify, redirect, url_for, send_file
from sys import argv
from ast import literal_eval
from plot.bars import HotUsers
from html_templater import bokeh_headers

app = Flask(__name__)



@app.route('/hot_users', methods=["GET"])
def hot_users():
	sample = [{"index":2,"user":"Listener","hotness":59},{"index":1,"user":"Cicranis","hotness":43},{"index":0,"user":"Fulano da Silva","hotness":30},{"index":5,"user":"Hackeador","hotness":30},{"index":3,"user":"Lorem Ipsum","hotness":25},{"index":4,"user":"Bla bla","hotness":11},{"index":4,"user":"Bla bla Bla","hotness":12},{"index":4,"user":"Outra pessoa","hotness":27}]
	return jsonify(sample)

@app.route('/hot_artists', methods=["GET"])
def hot_artists():
	sample = [{"index":2,"user":"Geovani Jr","hotness":70},{"index":1,"user":"Falcao","hotness":65},{"index":0,"user":"Tiririca","hotness":39},{"index":5,"user":"Lambadão Stillus","hotness":17},{"index":3,"user":"Gil Bala","hotness":46},{"index":4,"user":"Gil Doce","hotness":41},{"index":4,"user":"Molejao","hotness":99},{"index":4,"user":"Ednaldo Pereira","hotness":27}]
	return jsonify(sample)

@app.route('/hot_users_bar')
def hot_users_bar():
	sample = literal_eval(hot_users().data)
	sample_df = pd.DataFrame.from_dict(sample)

	request_dict = request.args.to_dict()

	if "width" in request_dict and "height" in request_dict:
		return HotUsers().bar(sample_df, width=int(request_dict["width"]), height=int(request_dict["height"]), plot=False)

	r = HotUsers().bar(sample_df, plot=False)
	return jsonify(r)

@app.route('/hot_users_bar2')
def hot_users_bar2():
	sample = literal_eval(hot_users().data)
	sample_df = pd.DataFrame.from_dict(sample)

	request_dict = request.args.to_dict()

	if "width" in request_dict and "height" in request_dict:
		return HotUsers().bar(sample_df, width=int(request_dict["width"]), height=int(request_dict["height"]), plot=False)

	r = HotUsers().bar2(sample_df, plot=False)
	return (r)

@app.route('/hot_artists_bar')
def hot_artists_bar():
	sample = literal_eval(hot_artists().data)
	sample_df = pd.DataFrame.from_dict(sample)

	request_dict = request.args.to_dict()

	if "width" in request_dict and "height" in request_dict:
		return HotUsers().bar(sample_df, width=int(request_dict["width"]), height=int(request_dict["height"]), plot=False)

	r = HotUsers().bar(sample_df, plot=False)
	return jsonify(r)


@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

# @app.route('/wordcount', methods=["GET"])
# def wordcount2():
# 	text = text_cleaner(open(text_path, "r").read().lower())
# 	wordcount_map = Counter(text.split())
	
# 	word = request.args.get('word')
# 	pm.save_word(word)

# 	return jsonify({'word': word, 'count': wordcount_map[word]})

# @app.route('/word_entries', methods=['GET'])
# def word_entries():
# 	return jsonify(pm.word_entries())

# @app.route('/user_entries', methods=['GET'])
# def user_entries():
# 	return jsonify(pm.user_entries())

# @app.route('/form', methods = ['GET'])
# def form():
# 	return template.form()

# @app.route('/add_name', methods = ['POST'])
# def add_name():
# 	name = request.get_json()["name"]
# 	return success(name)

# def success(name):
# 	pm.save_user(name)
# 	return template.success_html(name)

if __name__ == '__main__':

	app.run(host="10.30.100.68", port=8080, debug=True)

