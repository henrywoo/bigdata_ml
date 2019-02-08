import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8') # required to convert to unicode

with open('stop_words_en.txt') as f:
    stop_words = set(f.read().split())

for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
    except ValueError as e:
        continue
    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
    for word in words:
        word = word.lower()
        if word in stop_words:
            continue
        word_sorted = ''.join(sorted(word))
        print "%s\t%d\t%s" % (word_sorted, 1, word)
