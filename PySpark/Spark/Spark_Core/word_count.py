from pyspark import SparkContext

import zipfile

sc = SparkContext("local[*]","Word Analysis")

rdd1 = sc.textFile("D:/Spark_Prudvi/wordscount.txt",3)
print(type(rdd1))
print(rdd1)
print(rdd1.getNumPartitions())
#partition_list=rdd1.glom().collect()


