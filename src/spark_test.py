from pyspark import SparkContext

def a_b_cnt():

	PATH_TO_SPARK_HOME = '/usr/local/spark-1.5.1/'

	logFile = PATH_TO_SPARK_HOME + 'README.md'
	sc = SparkContext('local', 'Simple App')
	logData = sc.textFile(logFile).cache()

	numAs = logData.filter(lambda s: 'a' in s).count()
	numBs = logData.filter(lambda s: 'b' in s).count()

	print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

if __name__ == '__main__':
	a_b_cnt()