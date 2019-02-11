import sys, re, math

def g():
    Nt, N, Dt = 0, 1, 1
    for line in sys.stdin:
        if "Target word=" in line:
            r=re.match("\s+{0}=(\d+)".format("Target word"), line)
            if r is not None:
                Nt=int(r.group(1))
        if "Total words=" in line:
            r=re.match("\s+{0}=(\d+)".format("Total words"), line)
            if r is not None:
                N=int(r.group(1))
        if "Valid docs=" in line:
            r=re.match("\s+{0}=(\d+)".format("Valid docs"), line)
            if r is not None:
                Dt=int(r.group(1))
    return (1/math.log(1. + Dt)) * Nt / N

if __name__ == '__main__':
    print(g())