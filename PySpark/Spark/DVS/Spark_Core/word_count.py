from pyspark import SparkContext

sc = SparkContext("local[2]", "Word Analysis")

# rdd1 is the parentRDD.
rdd1 = sc.textFile("D:/Spark_Prudvi/wordscount.txt")
# Used to get the Number of partitions for a RDD.
print(rdd1.getNumPartitions())
# prints the type of RDD that is created in PVM(Python)
# 2
print(type(rdd1))
# <class 'pyspark.rdd.RDD'>
# Print the type of RDD that is created in JVM(Scala)
print(rdd1)


# D:/Spark_Prudvi/wordscount.txt MapPartitionsRDD[1] at textFile at <unknown>:0

def removeunicode_splitwords(x):
    # Removing non-ascii charecters
    ascii_str = str(x).encode("ascii", "ignore").decode()
    # split each word in a line using single space.
    return ascii_str.split(" ")


# Applying the map transformation
rdd2 = rdd1.map(removeunicode_splitwords)
# You cannot change the number of partitions using narrow transformations and they inherit from the parentRDD
print(type(rdd2))
# <class 'pyspark.rdd.PipelinedRDD'>
print(rdd2)
# PythonRDD[2] at RDD at PythonRDD.scala:53
rdd2.getNumPartitions()
# 2

# flatMap is transformation used to flatten the nested data structure.
rdd3 = rdd2.flatMap(lambda x: x)


def makepairedRDD(x):
    return (x, 1)


# rdd4 is a Paired RDD.
rdd4 = rdd3.map(makepairedRDD)


def mapValuesUDF(x):
    # Example (but -> [1,1,1,1]) for this  [1,1,1,1] is an input
    return sum(x)


# groupByKey is a wide Transformation which leades to shuffling
# mapValues is a transformation which can be applied on pairedRDD(Each element of RDD is (Key,Value)).
# For each key it takes its values as an input
# on the values it apply the compute (Example: sum(x))
# returns back the computed value as an output.

action_collect = rdd4.groupByKey().mapValues(mapValuesUDF).collect()
type(action_collect)
print(action_collect)

# Below lines exactly does the same as above.

# action_collect = trans5.groupByKey().mapValues(len).collect()
# action_collect = trans5.groupByKey().mapValues(lambda x: len(x)).collect()
# action_collect = trans5.groupByKey().mapValues(lambda x: sum(x)).collect()

# CountByKey is an action. It will send back all the parititons ouput to driver and then find the count of each key using Counter
# Note: Don't use this production.
action1 = rdd4.countByKey().items()
print(type(action1))
print(action1)

rdd5 = rdd4.reduceByKey(lambda x, y: x + y)
type(rdd5)

rdd5.take(100)

# Total Number of Words in Dataset
action6 = rdd5.map(lambda x: x[1]).reduce(lambda x, y: x + y)
print(action6)
