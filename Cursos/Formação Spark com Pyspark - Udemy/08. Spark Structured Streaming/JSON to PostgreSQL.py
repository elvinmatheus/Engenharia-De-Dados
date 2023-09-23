from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Streaming2").getOrCreate()

    json_schema = "nome STRING, postagem STRING, data INT"

    df = spark.readStream.json("/home/elvin/teste_streaming/", schema=json_schema)

    diretorio = "/home/elvin/temp/"

    def atualiza_postgres(dataf, batchId):
        dataf.write.format("jdbc") \
            .option("url", "jdbc:postgresql://localhost:5432/posts") \
            .option("dbtable", "Posts") \
            .option("user", "postgres") \
            .option("password", "123456") \
            .option("driver", "org.postgresql.Driver") \
            .mode("append") \
            .save()

    stcal = df.writeStream.foreachBatch(atualiza_postgres) \
                .outputMode("append") \
                .trigger(processingTime = "5 second") \
                .option("checkpointlocation", diretorio) \
                .start()

    stcal.awaitTermination()