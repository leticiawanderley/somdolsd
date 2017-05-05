from bokeh.charts import Bar, output_file, show
from bokeh.plotting import figure
from bokeh.charts.attributes import cat
from bokeh.embed import file_html
from bokeh.resources import CDN
from bokeh.embed import components

class HotUsers:

	def __init__(self):
		pass

	def bar(self, hot_users, top=5, width=800, height=300, plot=False):

		hot_users = hot_users.sort_values("hotness", ascending=False)
		bar = Bar(data=hot_users.head(top), values='hotness', 
					label=cat(columns='user',sort=False),
				    color="blue", width=width, height=height, legend=False)

		if plot:
			show(bar)

		output_file("temp/bar.html")

		script, div = components(bar)

		return {"script": script, "div": div}
		#return file_html(bar, CDN, "my plot")


	def bar2(self, hot_users, top=5, width=800, height=300, plot=False):

		hot_users = hot_users.sort_values("hotness", ascending=False)
		bar = Bar(data=hot_users.head(top), values='hotness', 
					label=cat(columns='user',sort=False),
				    color="blue", width=width, height=height, legend=False)

		if plot:
			show(bar)

		output_file("temp/bar.html")

		script, div = components(bar)

		#return {"script": script, "div": div}
		return file_html(bar, CDN, "my plot")