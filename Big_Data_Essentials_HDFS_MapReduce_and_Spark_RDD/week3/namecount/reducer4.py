import sys, re

reload(sys)
sys.setdefaultencoding('utf-8') # required to convert to unicode

def condition_name(cnt, cnt_name):
    return ((cnt - cnt_name) *100.0/ cnt) < 0.5

current_key, current_cnt, current_cnt_name = None, 0, 0

for line in sys.stdin:
    try:
        key, cnt, cnt_name = unicode(line.strip()).split('\t')
        cnt = int(cnt)
        cnt_name = int(cnt_name)
    except ValueError as e:
        continue
    
    if current_key != key:
        if current_key and condition_name(current_cnt, current_cnt_name):
            print "%s\t%d" % (current_key, current_cnt)
        current_key = key
        current_cnt = cnt
        current_cnt_name = cnt_name
    else:
        current_cnt += cnt
        current_cnt_name += cnt_name
        
print "%s\t%d" % (current_key, current_cnt)
