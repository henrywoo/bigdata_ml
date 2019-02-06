import re,sys

reload(sys)
sys.setdefaultencoding('utf-8')

#for line in open("wikipedia.txt","r"):
for line in sys.stdin:
  aid, text= unicode(line.strip()).split("\t",1)
  text = re.sub("^\W+|\W+$", "", text, flags=re.UNICODE)
  ws = re.split("\W*\s+\W*", text, flags=re.UNICODE)
  for w in ws:
    print "%s\t%d" % (w.lower(), 1)
