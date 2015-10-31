from mrjob.job import MRJob
import csv

# I took out the first line of the csv file, which is the list of field names
fieldnames = ['ID','Case Number','Date','Block','IUCR','Primary Type','Description',
			  'Location Description','Arrest','Domestic','Beat','District','Ward',
			  'Community Area','FBI Code','X Coordinate','Y Coordinate','Year',
			  'Updated On','Latitude','Longitude','Location']


class MRYearMonthLocation(MRJob):

	def mapper(self, _, line):
		# ID, Case, Number,Date,Block,IUCR,Primary Type,Description,Location Description,Arrest,Domestic,Beat,District,Ward,Community Area,FBI Code,X Coordinate,Y Coordinate,Year,Updated On,Latitude,Longitude,Location


		timestamp