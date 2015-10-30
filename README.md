# City_of_Chicago_Crime_Data
An Apache Spark self-contained application on the City of Chicago Crime Dataset (2001 - Present). Graph and text analysis.

----------------------------

City of Chicago -- Crimes Dataset

***************

I first used the 2013 Crime dataset as a subset of the entire (2001 - Present) dataset.

	2013 Crime Dataset:
		- There are 306356 crimes
		- In the 2001 - Present dataset, there are over 5 million crimes, making using cluster comupting like Spark necessary

Things that I can possibly do:

	1. Make a beautiful heat map of crime distributions in Chicago
		Make a moving heat map for the past 15 years -- each month being a year
		Clear our mis-conceptions in Chicago
		drug cartels in latin america, they all move together, they follow a unit
		maybe you can look at the more serious crimes only

	2. Crime vs. weather, the correlation
		Two of the most talked about things in Chicago, what is their relationship
		Crimes should drop significantly during winter, makes sense

	3. Use the Google Maps API to cross-check the route that you want to take
		maybe recommend a different route if the "score" of the original route is too low

----------------------------

Understanding the Dataset:

	Each crime has the following list of info:

		['Arrest',
		 'Beat',
		 'Block',
		 'Case Number',
		 'Community Area',
		 'Date',
		 'Description',
		 'District',
		 'Domestic',
		 'FBI Code',
		 'ID',
		 'IUCR',
		 'Latitude',
		 'Location',
		 'Location Description',
		 'Longitude',
		 'Primary Type',
		 'Updated On',
		 'Ward',
		 'X Coordinate',
		 'Y Coordinate',
		 'Year']

	I would like to first sort through the types of crimes there are: from serious to not that serious
	In total, there are these crimes:

		['ARSON',
		 'ASSAULT',
		 'BATTERY',
		 'BURGLARY',
		 'CRIM SEXUAL ASSAULT',
		 'CRIMINAL DAMAGE',
		 'CRIMINAL TRESPASS',
		 'DECEPTIVE PRACTICE',
		 'GAMBLING',
		 'HOMICIDE',
		 'HUMAN TRAFFICKING',
		 'INTERFERENCE WITH PUBLIC OFFICER',
		 'INTIMIDATION',
		 'KIDNAPPING',
		 'LIQUOR LAW VIOLATION',
		 'MOTOR VEHICLE THEFT',
		 'NARCOTICS',
		 'NON - CRIMINAL',
		 'NON-CRIMINAL',
		 'OBSCENITY',
		 'OFFENSE INVOLVING CHILDREN',
		 'OTHER NARCOTIC VIOLATION',
		 'OTHER OFFENSE',
		 'PROSTITUTION',
		 'PUBLIC INDECENCY',
		 'PUBLIC PEACE VIOLATION',
		 'ROBBERY',
		 'SEX OFFENSE',
		 'STALKING',
		 'THEFT',
		 'WEAPONS VIOLATION']



----------------------------

Code Structure:

	"data" folder: all my datasets

	"src" folder: all my source codes

	"output" folder: all the text and graph outputs

