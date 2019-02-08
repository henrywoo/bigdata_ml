#!/bin/bash

INT_DIR="assignment1_interim_"$(date +"%s%6N")
OUT_DIR="assignment1_"$(date +"%s%6N")

# Code for your first job
# yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar ...

NUM_REDUCERS=8

mapred streaming \
    -D mapred.jab.name="Streaming wordCount" \
    -D mapreduce.job.reduces=${NUM_REDUCERS} \
    -files mapper1.py,reducer1.py \
    -mapper "python mapper1.py" \
    -combiner "python reducer1.py" \
    -reducer "python reducer1.py" \
    -input hdfs://u3:9000/henry/wikipedia.txt \
    -output ${INT_DIR} > /dev/null


# Code for your second job
# yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar ...
NUM_REDUCERS=1

mapred streaming \
    -D mapred.jab.name="Streaming wordCount Rating" \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D map.output.key.field.separator=\t \
    -D mapreduce.partition.keycomparator.options=-k1,1nr \
    -D mapreduce.job.reduces=${NUM_REDUCERS} \
    -files mapper2.py,reducer2.py \
    -mapper "python mapper2.py" \
    -reducer "python reducer2.py" \
    -input ${INT_DIR} \
    -output ${OUT_DIR} > /dev/null

# Code for obtaining the results
hdfs dfs -cat ${OUT_DIR}/part-00000 | head
#hdfs dfs -cat ${OUT_DIR}/part-00000 | sed -n '7p;8q'

hdfs dfs -rm -r -skipTrash ${INT_DIR} > /dev/null
hdfs dfs -rm -r -skipTrash ${OUT_DIR} > /dev/null
