from pyspark import SparkConf, SparkContext
import re

START_WORD='narodnaya'
START_WORD='henry'
INPUT_FILE="/data/wiki/en_articles_part/articles-part"
INPUT_FILE="/henry/wikipedia.txt"

sc = SparkContext(conf=SparkConf().setAppName("HenryWu").setMaster("yarn"))
#sc = SparkContext(conf=SparkConf().setAppName("HenryWu").setMaster("yarn").set("spark.cores.max", "4"))
#sc = SparkContext(conf=SparkConf().setAppName("HenryWu").setMaster("local[2]"))

def parse_article(line):
    try:
        article_id, text = unicode(line.rstrip()).split('\t', 1)
        words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
        return words
    except ValueError as e:
        return []

def pairs_starting_from_word(words, first_word=START_WORD):
    pairs = []
    for i, word in enumerate(words[:-1]):
        if (word == first_word):
            pair = '{}_{}'.format(word, words[i+1])
            cnt = 1
            pairs.append((pair, cnt))
        else:
            continue
    return pairs


wiki = sc.textFile(INPUT_FILE).map(parse_article)
wiki_lower = wiki.map(lambda words: [x.lower() for x in words])
wiki_pairs = wiki_lower.flatMap(lambda x: pairs_starting_from_word(x))
wiki_pairs = wiki_pairs.filter(lambda x: x != [])
wiki_red = wiki_pairs.reduceByKey(lambda a, b: a + b, numPartitions=8)
wiki_red_sorted = wiki_red.sortByKey()
result = wiki_red_sorted.collect()
for pair, cnt in result:
    print '{}\t{}'.format(pair, cnt)

sc.stop()


