import os
os.environ["SPARK_HOME"] = "C:\\tools\\spark"
os.environ["JAVA_HOME"] = "C:\\Program Files\\Microsoft\\jdk-11.0.22.7-hotspot"
os.environ["PYSPARK_DRIVER_PYTHON"] = "jupyter"
os.environ["PYSPARK_DRIVER_PYTHON_OPTS"] = "lab"
os.environ["PYSPARK_PYTHON"] = "python"
os.environ['PYSPARK_SUBMIT_ARGS'] = 'pyspark-shell'

from pyspark.sql import SparkSession
#spark = SparkSession.builder.master("local[*]").appName("JiangSparkSQL").getOrCreate()
spark = SparkSession.builder.appName("JiangSparkSQL").config("spark.executor.memory", "2g").getOrCreate()

# ------------------

data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])
df.printSchema()
df.head()
df.show()
spark.stop()