from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Streaming").getOrCreate()

    json_schema = "nome STRING, postagem STRING, data INT"

    df = spark.readStream.json("/home/elvin/teste_streaming", schema=json_schema)

    diretorio = "/home/elvin/temp/"

    
    stcal = df.writeStream.format("console") \
                .outputMode("append") \
                .trigger(processingTime="5 second") \
                .option("checkpointlocation", diretorio) \
                .start()

    stcal.awaitTermination()