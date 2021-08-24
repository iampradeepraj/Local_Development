import sys

from pyspark.sql import *

from lib.logger import Log4j

if __name__=="__main__":
    spark = SparkSession.builder \
        .appName("Hello Spark") \
        .master("local[3]") \
        .getOrCreate()

    logger = Log4j(spark)

    logger.info("Starting HelloSpark")

    sample_df = spark.read.option("header","true").option("inferSchema","true").csv(sys.argv[1])
    sample_df.show()

    logger.info("Finished HelloSpark")
    spark.stop()

