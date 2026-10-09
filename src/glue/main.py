import sys

from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from pyspark.sql import functions as F

from transforms import standardise_column_name

args = getResolvedOptions(sys.argv, ["JOB_NAME", "SOURCE_BUCKET", "TARGET_BUCKET"])

sc = SparkContext()
glue_context = GlueContext(sc)
spark = glue_context.spark_session
job = Job(glue_context)
job.init(args["JOB_NAME"], args)

raw = spark.read.option("header", "true").csv(f"s3://{args['SOURCE_BUCKET']}/input/")
clean = (
    raw.toDF(*[standardise_column_name(c) for c in raw.columns])
    .dropDuplicates()
    .withColumn("processed_at", F.current_timestamp())
)
clean.write.mode("overwrite").parquet(f"s3://{args['TARGET_BUCKET']}/output/")

job.commit()
