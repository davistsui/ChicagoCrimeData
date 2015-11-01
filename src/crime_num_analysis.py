from pyspark import SparkContext
import matplotlib.pyplot as plt
import numpy as np


'''
	This file is responsible for outputing all the crime number analysis plots.
	All plots are in the "output/crime_num_plots" folder

	Plots generated:
		1) '2001-2015_Crime_Num.png':
			This is the bar chart that shows the total crime number per year for the past 15 years

		2) 15 monthly crime number bar charts -- one for each year
			In the 'monthly_crime_num_by_year' folder, you will find 15 bar charts that will show the monthly crime count for the respective year

	Questions investigated:
		1) How has the crime numbers changed for the past 15 years (from year to year)?

		2) How does monthly crime numbers change within a year?
'''


# these are the fieldnames for each line in the csvfile in order
fieldnames = ['ID','Case Number','Date','Block','IUCR','Primary Type','Description',
			  'Location Description','Arrest','Domestic','Beat','District','Ward',
			  'Community Area','FBI Code','X Coordinate','Y Coordinate','Year',
			  'Updated On','Latitude','Longitude','Location']

# we will use these for making the bar charts
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
years = ["'01", "'02", "'03", "'04", "'05", "'06", "'07", "'08", "'09", "'10", "'11", "'12", "'13", "'14", "'15" ]


# each line in the csvfile is disritbuted as a string to each node
# returns the the tuple (year, month) for each crime_line
def year_month_tup(crime_line):
	# every crime has a date
	crime = crime_line.split(',')
	timestamp = crime[2]
	# '12/31/2013 11:59:00 PM'
	date = timestamp.split(' ')[0]
	year = int(date.split('/')[2])
	month = int(date.split('/')[0])

	# both year and month are int
	return (year, month)


# returns a LIST of tuples in the format: ((year, month), crime_count)
# all the heavy lifting is done here: we need to process almost 6 million crime lines
def mk_crime_num_list(csvfile_name):
	# 'local' because it is a self-contained application
	sc = SparkContext('local', 'CrimeNumAnalysis')
	crimes = sc.textFile(csvfile_name).cache()

	# for each node, return the tuple: ((year, month), 1)
	# 1 is the count for crime in mapper
	pairs = crimes.map(lambda crime_line: (year_month_tup(crime_line), 1))
	# now combine and add up all the counts for the same (year, month) keys
	reduced_pairs = pairs.reduceByKey(lambda a, b: a + b)

	# reduced_pairs is a LIST of 12 tuples: ((year, month), tot_crime_counts)
	result = reduced_pairs.collect()
	return result


# re-format the list outputed above into a dictionary for easy access for plotting
def mk_crime_num_dict(crime_num_list):
	d = {}
	for pair in crime_num_list:
		# both year and month are int
		date = pair[0]
		year = date[0]
		month = date[1]
		# check keys
		if year in d:
			if month in d[year]:
				d[year][month] += pair[1]
			else:
				d[year][month] = pair[1]
		else:
			d[year] = {}
			d[year][month] = pair[1]

	return d


# helper function to plot each monthly crime num bar chart
def plot_monthly_crime_num_helper(monthly_crime_num_list, year):
	pos = np.arange(len(monthly_crime_num_list))
	width = 0.7

	ax = plt.axes()
	ax.set_xticks(pos + (width / 2))
	ax.set_xticklabels(months)

	light_blue = (162.0/255.0, 200.0/255.0, 236.0/255.0)

	plt.bar(pos, monthly_crime_num_list, width, color = light_blue)

	title = str(year) + ' Monthly Crime Numbers'
	plt.title(title)
	plt.xlabel('Month')
	plt.ylabel('Count')
	plt.ylim([0, 50000])
	plt.grid(True)

	save_name = 'output/crime_num_plots/monthly_crime_num_by_year/' + str(year) + '.png'
	plt.savefig(save_name)
	plt.close()


# generates the 15 monthly crime num bar charts, one for each year
# x-axis: months; y-axis: total_crime_counts
def plot_monthly_crime_num(crime_num_dict):
	for year in crime_num_dict:
		monthly_crime_num_list = []
		# so that the list of monthly revenues is in order
		for i in range(1, 13):
			# this is for 2015, because we only have data until October 24th
			try:
				crime_num = crime_num_dict[year][i]
			except:
				crime_num = 0

			monthly_crime_num_list.append(crime_num)

		plot_monthly_crime_num_helper(monthly_crime_num_list, year)


# helper function to plot the year by year crime number: 1 bar chart
def plot_yearly_crime_num_helper(yearly_crime_num_list):
	pos = np.arange(len(yearly_crime_num_list))
	width = 0.6

	ax = plt.axes()
	ax.set_xticks(pos + (width / 2))
	ax.set_xticklabels(years)

	light_blue = (162.0/255.0, 200.0/255.0, 236.0/255.0)

	plt.bar(pos, yearly_crime_num_list, width, color = light_blue)

	title = '2001 - 2015 Total Crime Numbers'
	plt.title(title)
	plt.xlabel('Year')
	plt.ylabel('Count')
	plt.ylim([0, 500000])
	plt.grid(True)

	save_name = 'output/crime_num_plots/2001-2015_Crime_Num.png'
	plt.savefig(save_name)
	plt.close()

# generates the year by year crime number bar chart
# x-axis: years; y-axis: total_crime_count
def plot_yearly_crime_num(crime_num_dict):
	yearly_crime_num_list = []
	# to ensure the order of the years:
	for i in range(2001, 2016):
		year_count = 0
		for month in crime_num_dict[i]:
			year_count += crime_num_dict[i][month]
		yearly_crime_num_list.append(year_count)

	print yearly_crime_num_list

	plot_yearly_crime_num_helper(yearly_crime_num_list)


if __name__ == '__main__':
	csvfile_name = 'data/2001-Present_Crime_Data.csv'
	crime_num_list = mk_crime_num_list(csvfile_name)
	crime_num_dict = mk_crime_num_dict(crime_num_list)
	
	# make the 15 plots, one for each year
	# within each plot, we will see the crime count for each month
	plot_monthly_crime_num(crime_num_dict)

	# make 1 plot for all the years
	# observe how the total number of crimes has changed over the years
	plot_yearly_crime_num(crime_num_dict)

