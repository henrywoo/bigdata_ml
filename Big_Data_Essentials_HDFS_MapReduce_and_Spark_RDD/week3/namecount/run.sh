OUT_DIR="coursera_mr_task2_extra"
NUM_REDUCERS=8

mapred streaming \
    -D mapred.jab.name="Streaming name count" \
    -D mapreduce.job.reduces=${NUM_REDUCERS} \
    -files mapper4.py,reducer4.py \
    -mapper "python mapper4.py" \
    -reducer "python reducer4.py" \
    -input hdfs://u3:9000/henry/wikipedia.txt \
    -output ${OUT_DIR} > /dev/null
    
OUT_DIR_2="coursera_mr_task2_extra2"
NUM_REDUCERS=1

mapred streaming \
    -D mapred.jab.name="Streaming name count sorting" \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D map.output.key.field.separator=\t \
    -D mapreduce.partition.keycomparator.options=-k1,1nr \
    -D mapreduce.job.reduces=${NUM_REDUCERS} \
    -files mapper5.py,reducer5.py \
    -mapper "python mapper5.py" \
    -reducer "python reducer5.py" \
    -input ${OUT_DIR} \
    -output ${OUT_DIR_2} > /dev/null
    
hdfs dfs -cat ${OUT_DIR_2}/part-00000 | sed -n '5p;6q'

hdfs dfs -rm -r -skipTrash ${OUT_DIR} > /dev/null
hdfs dfs -rm -r -skipTrash ${OUT_DIR_2} > /dev/null
