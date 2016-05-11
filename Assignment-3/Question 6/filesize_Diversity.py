from collections import defaultdict
from sys import getsizeof
import tika
import json
import os
import sys
from tika import parser
import unicodedata
count=0

file_size_map=defaultdict(dict)

parser_chain_map={}

arg1=str(sys.argv[1])
for root, dirs, files in os.walk(arg1):
    for file in files:
        if(file!='.DS_Store'):
            count+=1
            print count
            path=os.path.join(root, file)
            tika.initVM()
            try:
                parsed = parser.from_file(path)
            except:
                continue
            if parsed.get("metadata") is not None:
                type=parsed.get("metadata").get("Content-Type")
                type=type.split(';')[0]
            else:
                continue
            parser_used=parsed.get("metadata").get("X-Parsed-By")
            metadata_collected=parsed.get("metadata")
            content_collected=parsed.get("content")
            metadata_amount=getsizeof(metadata_collected)/float(1024)
            content_amount=getsizeof(content_collected)/float(1024)
            parser_chain=''
            for word in parser_used:
                parser_chain+=word+'->'
            parser_chain=parser_chain[:-2]
            parser_chain=str(parser_chain)
            size=os.path.getsize(path)/float(1024)
            if type not in file_size_map.keys():
                file_size_map[type]={}
            if type in file_size_map.keys():
                temp_map2=file_size_map.get(type)
                if parser_chain not in temp_map2.keys():
                   file_size_map[type][parser_chain]={}
                elif parser_chain in temp_map2.keys():
                    if size>0 and size<10:
                        if '0-10' not in temp_map2.keys():
                            file_size_map[type][parser_chain]['0-10']=[]
                            file_size_map[type][parser_chain]['0-10'].append(1)
                            file_size_map[type][parser_chain]['0-10'].append(content_amount)
                            file_size_map[type][parser_chain]['0-10'].append(metadata_amount)
                        else:
                            file_size_map[type][parser_chain]['0-10'][0]+=1
                            file_size_map[type][parser_chain]['0-10'][1]+=content_amount
                            file_size_map[type][parser_chain]['0-10'][2]+=metadata_amount
                    elif size>=10 and size<50:
                        if '10-50' not in temp_map2.keys():
                            file_size_map[type][parser_chain]['10-50']=[]
                            file_size_map[type][parser_chain]['10-50'].append(1)
                            file_size_map[type][parser_chain]['10-50'].append(content_amount)
                            file_size_map[type][parser_chain]['10-50'].append(metadata_amount)
                        else:
                            file_size_map[type][parser_chain]['10-50'][0]+=1
                            file_size_map[type][parser_chain]['10-50'][1]+=content_amount
                            file_size_map[type][parser_chain]['10-50'][2]+=metadata_amount
                    elif size>=50 and size<100:
                        if '50-100' not in temp_map2.keys():
                            file_size_map[type][parser_chain]['50-100']=[]
                            file_size_map[type][parser_chain]['50-100'].append(1)
                            file_size_map[type][parser_chain]['50-100'].append(content_amount)
                            file_size_map[type][parser_chain]['50-100'].append(metadata_amount)
                        else:
                            file_size_map[type][parser_chain]['50-100'][0]+=1
                            file_size_map[type][parser_chain]['50-100'][1]+=content_amount
                            file_size_map[type][parser_chain]['50-100'][2]+=metadata_amount
                    elif size>=100 and size<=500:
                        if '100-500' not in temp_map2.keys():
                            file_size_map[type][parser_chain]['100-500']=[]
                            file_size_map[type][parser_chain]['100-500'].append(1)
                            file_size_map[type][parser_chain]['100-500'].append(content_amount)
                            file_size_map[type][parser_chain]['100-500'].append(metadata_amount)
                        else:
                            file_size_map[type][parser_chain]['100-500']+=1
                            file_size_map[type][parser_chain]['100-500'][1]+=content_amount
                            file_size_map[type][parser_chain]['100-500'][2]+=metadata_amount
                    else:
                        if '>500' not in temp_map2.keys():
                            file_size_map[type][parser_chain]['>500']=[]
                            file_size_map[type][parser_chain]['>500'].append(1)
                            file_size_map[type][parser_chain]['>500'].append(content_amount)
                            file_size_map[type][parser_chain]['>500'].append(metadata_amount)
                        else:
                            file_size_map[type][parser_chain]['>500']+=1
                            file_size_map[type][parser_chain]['>500'][1]+=content_amount
                            file_size_map[type][parser_chain]['>500'][2]+=metadata_amount

if os.path.exists('file_size_diversity_map.txt'):
    os.remove('file_size_diversity_map.txt')

with open("file_size_diversity_map.txt",'a+') as fileopen:
    json.dump(file_size_map,fileopen)
