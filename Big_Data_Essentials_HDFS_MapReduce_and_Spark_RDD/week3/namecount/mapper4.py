import sys, re

reload(sys)
sys.setdefaultencoding('utf-8') # required to convert to unicode

def is_name(word):
    if len(word) < 2:
        return False
    return word[0].isalpha() and word[0].isupper() and word[1:].islower()

for line in sys.stdin:
    try:
        article_id, text = unicode(line.strip()).split('\t', 1)
    except ValueError as e:
        continue
    words = re.split("\W*\s+\W*", text, flags=re.UNICODE)
    for word in words:
        name_flag = int(is_name(word))
        print "%s\t%d\t%d" % (word.lower(), 1, name_flag)
