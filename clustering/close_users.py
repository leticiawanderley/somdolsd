import pandas as pd
from sklearn.cluster import KMeans
N_CLUSTERS = 10

def distance(userA, userB):
	return len(set(userA["tags"]).intersection(userB["tags"]))

def clusters(data):
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
	matrix

	kmeans = KMeans(init='k-means++', n_clusters=N_CLUSTERS)
	kmeans.fit(data["tags"])
	data['cluster'] = pd.Series(kmeans.labels_)


	print(data.sort_values('cluster'))