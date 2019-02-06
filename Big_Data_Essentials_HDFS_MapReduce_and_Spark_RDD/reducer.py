import sys

current_key = None
word_sum = 0

for line in sys.stdin:
  k, v = line.strip().split("\t", 1)
  word_sum += 1
  if current_key is None:
    current_key = k

  if k != current_key:
    print "%s\t%d" % (current_key.lower(), word_sum)
    word_sum = 1
    current_key = k

if current_key is not None:
    print "%s\t%d" % (current_key.lower(), word_sum)


