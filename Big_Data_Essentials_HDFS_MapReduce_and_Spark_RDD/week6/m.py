import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8')  # required to convert to unicode

_term='labor'
_article_id='12'

path = 'stop_words_en.txt'
with open(path) as f:
    stop_words = set(f.read().split())


for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
        text = text.lower()
    except ValueError as e:
        continue

    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
    if _term in words:
        print >> sys.stderr, "reporter:counter:Wiki stats,Valid docs,%d" % 1
    if article_id != _article_id:
        continue
    # Your code for mapper here.
    for word in words:
        if word in stop_words:
            continue
        print >> sys.stderr, "reporter:counter:Wiki stats,Total words,%d" % 1
        if word == _term:
            print >> sys.stderr, "reporter:counter:Wiki stats,Target word,%d" % 1
