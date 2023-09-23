# 1. Crie um banco de dados no PostgreSQL: Tabelas
# 2. Crie uma aplicação que quando executada, recebe como parametro o caminho completo de um arquivo parquet que vai estar em um diretório qualquer,
# e grava no banco de dados Tabelas do PostgreSQL, com o nome de tabela que você também deve passar como parâmetro.

import sys, getopt
from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Atividade").getOrCreate()

    opts, args = getopt.getopt(sys.argv[1:], "i:n:")
    infile, nome = "", ""

    for opt, arg in opts:
        if opt == "-i":
            infile = arg
        elif opt == "-n":
            nome = arg
    
    dados = spark.read.load(infile)

    dados.write.format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/tabelas") \
        .option("dbtable", nome) \
        .option("user", "postgres") \
        .option("password", "123456") \
        .option("driver", "org.postgresql.Driver") \
        .save()
    
    spark.stop()