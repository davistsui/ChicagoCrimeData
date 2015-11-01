# City of Chicago Crime Data
An Apache Spark self-contained application on the City of Chicago Crime Dataset (2001 - Present).

----------------------------

Datasets Explained:

	1) '2001-Present_Crime_Data.csv'
		- This csv file contains all the crimes that have occured in the city of Chicago from 1.1.2001 to 10.24.2015.
		- There are 5,924,262 crimes in total, almost 6 million crimes over a span of 15 years
		- File size: 1.39 GB

	2) '2013_Crime_Data.csv'
		- I used the 2013 data as a subsest of the total data to run experiment and to get a sense of how big the larger dataset is
		- There are 306,356 crimes in 2013
		- File size: 72.6 MB

	The total dataset is about 20 times the size of the 2013 dataset (makes sense, since there are 15 years in total, and we will observe that the total number of crimes is descreasing considerably year by year).

----------------------------

Questions Investigated:

	1) How has the crime numbers changed for the past 15 years (from year to year)?
		- It is clear from the yearly_crime_num plot that the number of crimes per year has been consistenly decreasing for the past 15 years

	2) How does monthly crime numbers change within a year?
		- We will see that the monthly trend remains roughly the same for the past 15 years, with the colder months (Nov, Dec, Jan, Feb) having a dip in crime numbers and the hoter months (May, Jun, Jul, Aug, Sep) having a rise in crime numbers
		- Another significant finding is that it is visible that the total number of crimes is dropping year by year consistenlty for the past 15 years, which matches up with our findings in Question 1

	3) Top 10 Most Frequent Crime Types for each year;
		- The year by year graphs show that the top 10 most frequent crime types remainly roughly the same throughout the years
		- It is also visible from the year by year top 10 crime type num charts that the total number of crimes is decreasing year by year, a finding that mathces our previous results

----------------------------

Potenttial Investigations:

	1) I wanted to generate a geo-heatmap for crimes per month and create an animation for the past 15 years to see how crimes shift month by month and year by year.

	    - I couldn't pursuit this question because I would not have enough time to finish it. However, I found a similar and beautfiull done project online:
		http://www.davidhampgonsalves.com/Animated-Heatmaps.js/

	2) Correlate a set of tempareture data to the number of crimes

		- I believe there is a correlation: with colder months having lower number of crimes. Although this finiding is shown through my number of crimes per month chart, I would like to calculate the value of the correlation coefficient.
		- If I didn't waste so much time trying to geo-plot an animating heatmap, I would have definitely investigated this question

----------------------------

Code Structure:

	'data' folder:
		1) '2001-Present_Crime_Data.csv'
		2) '2013_Crime_Data.csv'

	'src' folder:

		1) 'crime_num_analysis.py'
			- the file that outputed all the charts with regard to crime numbers by month or by year

		2) 'crime_type_analysis.py'
			- the file that outpute all the charts with regard to crim types

		3) 'play.py'
			- What I used in the beginning to play around with the 2013 sub-dataset
			- I used it to investigate what info I know about each crime, what types of crimes there are, and how long it would take roughly to run through the entire dataset

	'output' folder:

		1) 'crime_num_plots' folder:
			(1) 'crime_num_plots/2001-2015_Crime_Num.png'
				- this bar chart shows the the total number of crimes per year for the past 15 years

			(2) 'monthly_crime_num_by_year' folder:
				- this folder contains 15 bar charts, one for each year
				- each bar charts plots the total number of crimes per month

		2) 'crime_type_plots' folder:
			- this folder contains 15 bar charts, one for each year, which plots the top 10 most frequeunt crime types in the x-axis and their respective counts in the y-axis
			
----------------------------

Big Data Technique: Apache Spark

	Used Map-Reduce through Apache Spark and returned a key-value pair tuple for each of the scenarios.

----------------------------

How to run all the files:
	
	- Simply run 'python run_all.py' in the top directory and all the files in the 'src' folder will run.
	
	- All plots will be stored in the 'output' folder as described above


