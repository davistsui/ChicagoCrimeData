import csv


'''
	This file is mainly used for playing around and getting a feel of the dataset in the beginning.

	Questions investigated:
		1) What info does each crime line hold?

		2) How long does it take to process the 2013 set of data (306,356 crimes) not using Apache Spark
		   It takes about 2.8 seconds to read in the 2013 csvfile into a dictionary, not too slow.

		3) What are the Primary Types of crimes?
'''


fieldnames = ['ID','Case Number','Date','Block','IUCR','Primary Type','Description',
			  'Location Description','Arrest','Domestic','Beat','District','Ward',
			  'Community Area','FBI Code','X Coordinate','Y Coordinate','Year',
			  'Updated On','Latitude','Longitude','Location']


# converts the csv file into a dictionary with corresponding keys and values
# every row in the csvfile is one crime
# every row is now turned into a dict
# the result dict has each unique crime ID as a key and the crime dict as the corresponding value
def csv_to_dict(csv_filename):
	d = {}
	with open(csv_filename) as csvfile:
		# the values in the first row of the csvfile will be used as the fieldnames (the keys for the dict)
		reader = csv.DictReader(csvfile, fieldnames)
		for row in reader:
			d[row['ID']] = row

	return d
# It takes about 2.8 seconds to read in the 2013 csv file, not too slow.


# runs through the dict outputed as above
# returns the list of all primary crime types
def get_all_crime_types(crime_dict):
	crime_type_l = []

	for crime_id in crime_dict:
		crime = crime_dict[crime_id]
		crime_type = crime['Primary Type']
		if crime_type not in crime_type_l:
			crime_type_l.append(crime_type)

	return crime_type_l

'''
	These two functions below are what I used to investigate for my geo-heatmap.
	Unfortunately, I was not able to use them at this point of the project.
'''


# returns the the dictioary with each key being the crime_id and each value being the corresponding (lat, lon)
def get_location_dict(crime_dict):
	location_dict = {}

	for crime_id in crime_dict:
		crime = crime_dict[crime_id]
		# location is the tuple: (lat, lon)
		location = crime['Location']
		location_dict[crime_id] = location

	return location_dict


# this will output a list of (lat, lon)
def get_location_list(crime_dict):
	location_list = []

	for crime_id in crime_dict:
		crime = crime_dict[crime_id]

		if crime['Location'] == '':
			continue

		# location is the tuple: (lat, lon)
		# crime['latitude'] is originially in a string so I need to float it
		lat = float(crime['Latitude'])
		lon = float(crime['Longitude'])
		location_list.append((lat, lon))

	return location_list

