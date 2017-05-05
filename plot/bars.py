from bokeh.charts import Bar, output_file, show
from bokeh.plotting import figure
from bokeh.charts.attributes import cat
from bokeh.embed import file_html
from bokeh.resources import CDN

class HotUsers:

	def __init__(self):
		pass

	def bar(self, hot_users, plot=False):

		bar = Bar(data=hot_users, values='hotness', 
					label=cat(columns='user',sort=False),
				    color="blue", width=800, height=300, legend=False)


		output_file("hot_users.html")

		if plot:
			show(bar)

		return file_html(bar, CDN, "my plot")