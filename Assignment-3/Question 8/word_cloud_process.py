import json
import operator
import os
word_cloud_map={}
with open('word_cloud.json','r') as fopen:
    word_cloud_map=json.load(fopen)



newA = dict(sorted(word_cloud_map.iteritems(), key=operator.itemgetter(1), reverse=True)[:10000])

with open("max_word.json",'a+')as f:
    f.write('[')
    for k,v in newA.iteritems():
        k=k.strip('\n')
        k=k.strip('\t')
        k=k.strip('\r')
        if(len(k)<2):
            continue
        f.write('{'+'"'+'Word'+'"'+':'+'"'+k+'",')
        f.write('"'+'Count'+'"'+':'+'"'+str(v)+'"},')
    f.seek(-1, os.SEEK_END)
    f.truncate()
    f.write(']')
