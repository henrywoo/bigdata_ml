#!/bin/bash

#OUT_DIR="coursera_mr_task2"$(date +"%s%6N")
OUT_DIR="coursera_mr_task2_henry"
NUM_REDUCERS=1
LOGS="stderr_logs.txt"

# Stub code for your job
#hdfs dfs -rm -r -skipTrash ${OUT_DIR} > /dev/null

mapred streaming \
    -D mapred.jab.name="Streaming stopwords" \
    -D mapreduce.job.reduces=${NUM_REDUCERS} \
    -files mapper3.py,combiner3.py,reducer3.py,stop_words_en.txt \
    -mapper "python mapper3.py" \
    -combiner "python combiner3.py" \
    -reducer "python reducer3.py" \
    -input hdfs://u3:9000/henry/wikipedia.txt \
    -output ${OUT_DIR} > /dev/null 2>${LOGS}

# yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar ...
# ... \
#    -output ${OUT_DIR} > /dev/null 2> $LOGS

cat $LOGS | python ./counter_process.py "Stop words" "Total words"
cat $LOGS >&2
hdfs dfs -rm -r -skipTrash ${OUT_DIR} > /dev/null

