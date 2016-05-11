from collections import defaultdict
import tika
import json
import os
import sys
from tika import language

arg1=str(sys.argv[1])
language_map=defaultdict(list)
count=0

def printMap(tag,filename):
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename,'a+') as fopen:
        json.dump(tag,fopen)
count=0
for root, dirs, files in os.walk(arg1):
    for file in files:
        count+=1
        print count
        path=''
        lang=''
        if(file!='.DS_Store'):
            count+=1
            print count
            path=os.path.join(root, file)
            tika.initVM()
            try:
                lang=language.from_file(path)
            except:
                lang='unknown'
            print lang
            language_map[lang].append(file)

printMap(language_map,"language.json")

