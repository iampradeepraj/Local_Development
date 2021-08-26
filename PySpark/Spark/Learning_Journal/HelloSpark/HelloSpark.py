import sys

from pyspark.sql import *

if __name__=="__main__":
    spark = SparkSession.builder \
        .appName("Hello Spark") \
        .master("local[3]") \
        .getOrCreate()

    sample_df = spark.read.option("header","true").option("inferSchema","true").csv(sys.argv[1])
    partitioned_df = sample_df.repartition(2)

    filtered_df = partitioned_df.select("Age","Gender","Country","state").where("Age < 40").groupby("country")
    count_df=filtered_df.count()

    count_df.show()

    spark.stop()

