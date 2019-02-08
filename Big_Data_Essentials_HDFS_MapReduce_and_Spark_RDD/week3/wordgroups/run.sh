OUT_DIR="word_groups"
NUM_REDUCERS=8

hdfs dfs -rm -r -skipTrash ${OUT_DIR} > /dev/null

#yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
mapred streaming \
    -D mapred.jab.name="Streaming word groups" \
    -D mapreduce.job.reduces=${NUM_REDUCERS} \
    -files mapper_wg.py,reducer_wg.py,stop_words_en.txt \
    -mapper "python mapper_wg.py" \
    -reducer "python reducer_wg.py" \
    -input hdfs://u3:9000/henry/wikipedia.txt \
    -output ${OUT_DIR} > /dev/null
    
hdfs dfs -cat word_groups/* | grep -P '(,|\t)english($|,)'
