 
# Setup PySpark and its S3 connection

- Create an environment with your favorite venv manager, ala: 
`conda create --name etl_spark_standalone python=3.8 && activate etl_spark_standalone`
- `pip install -r requirements.txt`. Note: This installs pyspark.

## Make a choice 
- Do you want standalone spark/hadoop (any version you want) or 
- Built-in Spark that comes with pip installs ala `pip install pyspark==3.0.1`

 
- Download <a href="https://spark.apache.org/downloads.html">spark</a>. I picked spark 3.0.1 with hadoop 3.2.0/. 
Set the SPARK_HOME accordingly.
- Don't set anything/set SPARK_HOME to the pyspark directory.

# Steps 
Examples follow standalone hadoop:
- On Windows, clone `git clone https://github.com/cdarlint/winutils` into `c:\dev\hadoop`
- Set envvars accordingly, ala `set HADOOP_HOME=C:\dev\hadoop\winutils\hadoop-3.2.0; set SPARK_HOME=C:\dev\spark-3.0.1-bin-hadoop3.2`. 
- Add `$HADOOP_HOME\bin` to PATH
- Restart your editor/session 
 
In Pycharm set the following envvars in the run configuration, similar to the above:
 `PYTHONUNBUFFERED=1;HADOOP_HOME=C:\dev\hadoop\winutils\hadoop-3.2.0;SPARK_HOME=C:\dev\spark-3.0.1-bin-hadoop3.2`
 
### Add AWS jars to your Spark jars folder to access S3
 Per <a href="http://hadoop.apache.org/docs/r3.2.0/hadoop-aws/dependency-analysis.html">
    3.2.0 hadoop-aws jar dependencies</a>:
 
 Note: if you pick another version of hadoop, make sure you check the files needed for download in the link above.
 
In a linux shell emulator:
- `cd $SPARK_HOME/jars`
- `wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.375/aws-java-sdk-bundle-1.11.375.jar`
- `wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.2.0/hadoop-aws-3.2.0.jar`


Sources: 
- <a href="https://blog.insightdatascience.com/how-to-access-s3-data-from-spark-74e40e0b2231">How to access s3 data from spark</a>
- <a href="https://stackoverflow.com/questions/34685905/how-to-link-pycharm-with-pyspark">Pycharm config</a>

# Code
```python
  session: Session = boto3.session.Session(profile_name='hierarchy_playground')
  credentials = session.get_credentials().get_frozen_credentials()
  # todo: use STS https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.get_session_token 
  # note: Hive catalog is supported with Delta only on Spark 3.0 https://github.com/delta-io/delta/releases
  spark = SparkSession \
      .builder \
      .appName("Demo") \
      .config('spark.hadoop.fs.s3a.access.key', credentials.access_key) \
      .config('spark.hadoop.fs.s3a.secret.key', credentials.secret_key) \
      .config('spark.hadoop.fs.s3a.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem') \
      .enableHiveSupport() \
      .getOrCreate()
  # https://hadoop.apache.org/docs/current/hadoop-aws/tools/hadoop-aws/index.html
```
### Bonus - add delta lake with the following
   ```python
      .config("spark.jars.packages", "io.delta:delta-core_2.12:0.7.0") \
      .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
      .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") 
   ```
      
