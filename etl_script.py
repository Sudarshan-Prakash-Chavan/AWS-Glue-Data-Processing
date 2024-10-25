import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Initialize Glue Context
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Step 1: Read data from the Glue Data Catalog
datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database = "movies-data-database", 
    table_name = "glueinput", 
    transformation_ctx = "datasource0"
)

# Step 2: Apply transformations (modify as needed)
# Example: Convert all titles to uppercase
transformed_data = datasource0.map(lambda row: {
    'title': row['title'].upper(),  # Assuming 'title' is a field in your JSON
    'release_year': row['release_year'],  # Adjust fields according to your JSON structure
    'genre': row['genre']
})

# Step 3: Convert DynamicFrame to DataFrame for writing to CSV
df_transformed = transformed_data.toDF()

# Step 4: Write the output to S3 in CSV format
output_path = "s3://moviestabledata/transformeddata/"
df_transformed.write.mode("overwrite").csv(output_path, header=True)

# Commit job
job.commit()
