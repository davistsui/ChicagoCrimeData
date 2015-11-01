import os

PATH = '/usr/local/spark-1.5.1/bin/spark-submit --master local[4] '

# Crime Num Analysis
# Question 1 & 2
os.system(PATH + 'src/crime_num_analysis.py')

# Crime Type Analysis
# Question 3
os.system(PATH + 'src/crime_type_analysis.py')