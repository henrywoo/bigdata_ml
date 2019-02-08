import sys
import re

def get_ratio(p1, p2):
    x = 0
    y = 0
    for line in sys.stdin:
        if p1 in line:
            r=re.match("\s+{0}=(\d+)".format(p1), line)
            if r is not None:
                x=int(r.group(1))
        if p2 in line:
            r=re.match("\s+{0}=(\d+)".format(p2), line)
            if r is not None:
                y=int(r.group(1))
    return x*100.0/y

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(get_ratio(sys.argv[1], sys.argv[2]))
