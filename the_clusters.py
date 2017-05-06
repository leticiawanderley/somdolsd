import pandas as pd
import requests
from sklearn.cluster import KMeans

def distance(userA, userB):
	return len(set(userA["tags"]).intersection(userB["tags"]))

def clusters(data, n_clusters=3):
	#user, tag
	#usrA, genero1
	#usrA, genero1
	#usrA, genero1
	#usrA, genero2
	#usrA, genero3
	#usrA, genero3
	#usrA, genero3


	#user, genero1, genero2, genero3
	#usrA, 3		1,		 2

	all_tags = data["tag"].drop_duplicates().tolist()
	all_users = data["user"].drop_duplicates().tolist()

	matrix = pd.DataFrame(columns=all_tags+["user"])

	for usr in all_users:
		freq_dict = pd.DataFrame(data[data["user"] == usr]["tag"].value_counts()).to_dict()
		freq_dict = {usr: freq_dict["tag"]}
		matrix = matrix.append(pd.DataFrame(freq_dict).transpose())

	matrix = matrix.fillna(0)

	kmeans = KMeans(init='k-means++', n_clusters=n_clusters)
	kmeans.fit(matrix)

	matrix['cluster'] = kmeans.labels_

	del matrix['user']

	return matrix.sort_values('cluster')

def normalize(series):
	return (series - series.min()) / (series.max() - series.min())


def get_user_tags(username):
	user_tags = pd.DataFrame({"user": [], "tag": []})

	r = requests.get("http://10.11.4.160:8080/user_activity?username=" + username)

	utags_list = r.json()
	for song in utags_list:
		if (len(song["tags"]) > 0):
			tag = song["tags"][0]["name"]
			user_tags = user_tags.append(pd.DataFrame({"user": [username], "tag": [tag]}))

	return user_tags

def get_tag_df():
	tag_df = pd.DataFrame({"user": [], "tag": []})

	for i in (get_users()):
		print(i["last_fm_username"])
		user_df = get_user_tags(i["last_fm_username"])
		tag_df = tag_df.append(user_df)
		print(user_df)
		print("\n\n\n")

	print(tag_df)
	return tag_df


def get_users():
	r = requests.get("http://10.11.4.160:8080/users")
	return r.json()

def relevant_tags(matrix, top=16):
	tags = matrix.columns.tolist()
	tags.remove("cluster")

	tags_relevance = pd.DataFrame({"tag":[], "count":[]})	

	for tag in tags:
		count = matrix[tag].sum()
		tags_relevance = tags_relevance.append(pd.DataFrame({"tag": [tag], "count": [count]}))

	tags_relevance = tags_relevance.sort_values('count', ascending=False)	
	
	return tags_relevance.head(16)

def radar_data(data):
	r_data = []

	cols = data.columns.tolist()
	cols.remove("cluster")

	for group in data["cluster"].drop_duplicates():
		group_data = []
		group_df = data[data["cluster"] == group]

		for col in cols:
			group_df[col] = normalize(group_df[col])

		group_df = group_df.fillna(0)
		#print("grupo", group)
		#print(group_df)
		#print("\n\n\n")

		for col in cols:
			group_data.append({"axis": col, "value": group_df[col].sum()})
		r_data.append(group_data)

	print(r_data)
	return r_data

if __name__ == "__main__":
	data = pd.read_csv("/home/tales/dev/projects/somdolsd/data/user_tags.csv")
	data = get_tag_df()

	matrix = clusters(data)

	use_tags = relevant_tags(matrix)
	print(use_tags)
	print(normalize(use_tags["count"]))

	radar_data(matrix)

	#print(get_user_tags("talestsp"))

	#print(get_tag_df())

	c = clusters(data)
	print(c["cluster"])
	
	