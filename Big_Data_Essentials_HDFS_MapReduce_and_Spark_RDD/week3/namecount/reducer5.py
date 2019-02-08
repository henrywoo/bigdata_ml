import sys

for line in sys.stdin:
    try:

        count, word = line.strip().split('\t', 1)
        count = int(count)
    except ValueError as e:
        continue
    print "%s\t%d" % (word, count)
