import sys
import re

reload(sys)
sys.setdefaultencoding('utf-8') # required to convert to unicode

current_key = None
current_cnt = 0
words_set = set()

for line in sys.stdin:
    try:
        key, cnt, word = unicode(line.strip()).split('\t')
        cnt = int(cnt)
    except ValueError as e:
        continue
    
    if current_key != key:
        if current_key and (len(words_set) > 1):
            print "%d\t%d\t%s" % (current_cnt, len(words_set), ','.join(sorted(words_set)))
        current_key = key
        words_set = set()
        words_set.add(word)
        current_cnt = cnt
    else:
        words_set.add(word)
        current_cnt += cnt
        
print "%d\t%d\t%s" % (current_cnt, len(words_set), ','.join(sorted(words_set)))

