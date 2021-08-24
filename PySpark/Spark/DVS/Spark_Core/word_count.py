from pyspark import SparkContext

sc = SparkContext("local[*]","Word Analysis")

rdd1 = sc.textFile("D:/Spark_Prudvi/wordscount.txt")
print(type(rdd1))
print(rdd1.count())
