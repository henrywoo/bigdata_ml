#!/bin/bash

#OUT_DIR="coursera_mr_task2"$(date +"%s%6N")

# Stub code for your job
hdfs dfs -rm -r -skipTrash tfidf_output > /dev/null

mapred streaming \
    -D mapred.jab.name="TFIDF" \
    -D mapreduce.job.reduces=0 \
    -files m.py,r.py,/opt/share/coursera/Big_Data_Essentials_HDFS_MapReduce_and_Spark_RDD/data/stop_words_en.txt \
    -mapper "python m.py" \
    -combiner "python r.py" \
    -reducer "python r.py" \
    -input hdfs://u3:9000/henry/articles-part \
    -output tfidf_output > /dev/null 2>stderr_logs.txt



#cat $LOGS | python ./counter_process.py "Stop words" "Total words"
#cat $LOGS >&2
#hdfs dfs -rm -r -skipTrash ${OUT_DIR} > /dev/null

