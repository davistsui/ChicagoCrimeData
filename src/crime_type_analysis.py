from pyspark import SparkContext
import matplotlib.pyplot as plt
import numpy as np


'''
	This file is responsible for outputing all the crime type analysis plots.
	All plots are in the "output/crime_type_plots" folder

	Plots generated:
		1) Top 10 Crime Type Bar Charts:
		   - 15 plots in total, 1 for each year
		   - x-axis: 10 most frequent Primary Crime Types
		   - y-axis: respective total crime counts

	Questions investigated:
		1) What are the 10 most frequent crime types for each year?

		2) How do they change from year to year?
'''


# These are all the 'Primary Type' for crimes
Primary_Crime_Types = ['ARSON','ASSAULT','BATTERY','BURGLARY','CRIM SEXUAL ASSAULT','CRIMINAL DAMAGE',
			   		   'CRIMINAL TRESPASS','DECEPTIVE PRACTICE','GAMBLING','HOMICIDE','HUMAN TRAFFICKING',
			    	   'INTERFERENCE WITH PUBLIC OFFICER','INTIMIDATION','KIDNAPPING','LIQUOR LAW VIOLATION',
			   	       'MOTOR VEHICLE THEFT','NARCOTICS','NON - CRIMINAL','NON-CRIMINAL','OBSCENITY',
		               'OFFENSE INVOLVING CHILDREN','OTHER NARCOTIC VIOLATION','OTHER OFFENSE',
		               'PROSTITUTION','PUBLIC INDECENCY','PUBLIC PEACE VIOLATION','ROBBERY','SEX OFFENSE',
		               'STALKING','THEFT','WEAPONS VIOLATION']


# each line in the csvfile is disritbuted as a string to each node
# returns the the tuple (year, crime_type) for each crime_line
def year_type_tup(crime_line):
	# every crime has a date
	crime = crime_line.split(',')
	timestamp = crime[2]
	# '12/31/2013 11:59:00 PM'
	date = timestamp.split(' ')[0]
	year = int(date.split('/')[2])

	crime_type = str(crime[5])

	# year is int and crime_type is str
	return (year, crime_type)


# returns a list of tuples: ((year, crime_type), num_crime)
# all the heavy lifting is done here: we need to process over 5 million crimes
def mk_crime_type_num_list(csvfile_name):
	# 'local' because it is a self-contained application
	sc = SparkContext('local', 'CrimeTypeAnalysis')
	crimes = sc.textFile(csvfile_name).cache()

	# for each node, return the tuple: ((year, crime_type), 1)
	# 1 is the count for each crime_line
	pairs = crimes.map(lambda crime_line: (year_type_tup(crime_line), 1))
	reduced_pairs = pairs.reduceByKey(lambda a, b: a + b)

	result = reduced_pairs.collect()
	return result


# re-format the list outputed above into a dictionary for easier access when plotting
def mk_crime_type_num_dict(crime_type_num_list):
	d = {}

	for tup in crime_type_num_list:
		info = tup[0]
		year = info[0]
		crime_type = info[1]

		if year in d:
			if crime_type in d[year]:
				d[year][crime_type] += tup[1]
			else:
				d[year][crime_type] = tup[1]
		else:
			d[year] = {}
			d[year][crime_type] = tup[1]
	
	return d


# helper function to plot each crime_type vs. crime_count bar chart
def plot_crime_type_num_helper(count_type_list, year):
	crime_types = []
	crime_counts = []
	# we only wan to look at top 10
	for i in range(10):
		c = count_type_list[i]
		crime_counts.append(c[0])
		crime_types.append(c[1])

	pos = np.arange(10)
	width = 0.7

	ax = plt.axes()
	ax.set_xticks(pos + (width / 2))
	ax.set_xticklabels(crime_types, rotation = 75)

	warm_red = (205.0/255.0, 85.0/255.0, 85.0/255.0)

	plt.bar(pos, crime_counts, width, color = warm_red)

	title = str(year) + ' Crime Type Counts'
	plt.title(title)
	plt.xlabel('Top 10 Crime Types')
	plt.ylabel('Count')
	plt.ylim([0, 100000])
	plt.grid(True)
	# adjust for the x-axis labels
	plt.gcf().subplots_adjust(bottom=0.45)

	save_name = 'output/crime_type_plots/' + str(year) + '.png'
	plt.savefig(save_name)
	plt.close()


# generates the crime_type vs. crime_count bar chart for the top 10 crime types
def plot_crime_type_num(crime_type_num_dict):
	for year in crime_type_num_dict:
		# now make a list of tuples of : (count, crime_type) for each year
		# feed this list into the ploting function
		count_type_list = []
		for crime_type in crime_type_num_dict[year]:
			count = crime_type_num_dict[year][crime_type]
			count_type_list.append((count, crime_type))

		# sort the count_type_list here in decreasing order because we only want to look at top 10
		count_type_list = sorted(count_type_list, reverse = True)
		plot_crime_type_num_helper(count_type_list, year)


if __name__ == '__main__':
	csvfile_name = 'data/2001-Present_Crime_Data.csv'
	crime_type_num_list = mk_crime_type_num_list(csvfile_name)
	crime_type_num_dict = mk_crime_type_num_dict(crime_type_num_list)
	# generates a top 10 crime type vs. crime count bar chart for every year
	plot_crime_type_num(crime_type_num_dict)
	













