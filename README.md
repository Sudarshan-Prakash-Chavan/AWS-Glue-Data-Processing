# AWS-Glue-Data-Processing

## Overview

This repository contains a comprehensive guide for setting up and executing various AWS Glue tasks, focusing on data cataloging, ETL jobs, and job bookmarks. It includes practical labs demonstrating the integration of AWS services for efficient data processing and management.

## Architectural Diagram

![AWS-Glue-Data-Processing](https://github.com/user-attachments/assets/069b1a0f-6acb-42de-bda9-e3a3b07c4142)

1.   **AWS S3:**

   -   **Input Bucket:** `moviestabledata`

   -   **Output Bucket:** `moviestabledata/transformeddata`

   -   Represents where your `movies.json` file is stored and where the transformed CSV files will be saved.

2.   **AWS Glue:**

   -   **Crawler:**

         -   Represents the `movies-data-crawler` which scans the S3 bucket to create the Data Catalog.
      
   -   **Data Catalog:**

         -   Shows the `movies-data-database` and the associated table(s) created by the crawler.
   -   **ETL Job:**

         -   Represents the `movies-data-job` that processes the data, including the transformations applied.

3.   **Data Flow:**

   -   Arrows indicating the flow of data:

       -   From S3 to Glue Crawler to create the Data Catalog.

       -   From Data Catalog to Glue ETL Job for processing.

       -   From Glue ETL Job back to S3 for saving the transformed data.

4.   **IAM Role:**

   -   Indicates the Master IAM role that provides the necessary permissions for the Glue services to access S3.

5.   **CloudWatch:**

   -   Shows integration for monitoring job metrics and logs.

## Prerequisites

- An AWS account with permissions to access S3 and Glue.
- Basic knowledge of AWS services and data processing concepts.

## 1: Setup Glue Data Catalog

### Prerequisites

1. Data set up in S3.
2. This exercise will be conducted in the **us-east-1** region.

### Steps

1. **Create S3 Bucket**: 
   - Create a bucket named `moviestabledata` and upload the `movies.json` file.
   
2. **Navigate to AWS Glue**: 
   - Click on **Crawlers** and then **Add Crawler**.

3. **Crawler Configuration**:
   - **Name**: `movies-data-crawler`
   - **Tag**: Add `movies-classifier`
   - **Data Store**: Select **S3** and specify the path.
   - **Exclude Patterns**: (none for this exercise)
   - **IAM Role**: Create a role named `Master` for read access to the S3 bucket.
   - **Schedule**: Select **Run on Demand**.
   - **Database**: Create a database named `movies-data-database`.
   - Review all settings and click **Finish**.

4. **Run the Crawler**: 
   - Execute the crawler to create a metadata table in AWS Glue Data Catalog.

5. **Review the Table**: 
   - Navigate to `movies-data-database` and view the created table.

## 2: Setup Glue Job

### Steps

1. **Navigate to AWS Glue**: 
   - Locate the table created in Lab 1.

2. **Create a New Job**:
   - Click on **Jobs** under the ETL category and then **Add Job**.

3. **Job Configuration**:
   - **Job Name**: `movies-data-job`
   - **IAM Role**: Select `AWSGlueServiceRole`
   - **Processing Environment**: Choose **Spark**.
   - **Glue Version**: Select the appropriate version.
   - **Script**: Allow Glue to construct a script.

4. **Advanced Properties**: 
   - Leave job bookmarks disabled.

5. **Monitoring Options**: 
   - Enable job metrics and continuous logging.

6. **Worker Configuration**: 
   - Select worker type as `G.1X` and leave DPUs at 10.

7. **Data Source**: 
   - Choose `moviestabledata` as the source.

8. **Schema Change**: 
   - Select **Change Schema**.

9. **Target Path**: 
   - Specify `transformeddata` in your S3 bucket.

10. **Script Editing**:
    - Save and edit the generated script. Remove unnecessary code (e.g., DropNullFields).

11. **Run the Job**: 
    - Execute the job and monitor progress in Continuous Logs.

12. **Verify Output**: 
    - Check the `transformeddata` folder for the resulting `.gz` file and extract it to observe the CSV format.

## 3: Job Bookmarks

### Steps

1. **Edit the Job**:
   - Go to AWS Glue, select `movies-data-job`, and click on **Edit Job**.

2. **Advanced Properties**: 
   - Select **Pause** for job bookmarks.

3. **Specify Values**: 
   - When running the job, specify **from** and **to** values based on job run IDs.

## Conclusion

These labs provide a hands-on approach to using AWS Glue for data cataloging and ETL processes. The workflows demonstrate effective data processing solutions leveraging AWS services.
