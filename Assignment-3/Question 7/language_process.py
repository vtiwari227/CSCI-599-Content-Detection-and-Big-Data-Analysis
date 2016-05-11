import json
import os
lang_map={}
temp_map={}
file_type_map={}
with open('language.json','r') as fopen:
    lang_map=json.load(fopen)

for k,v in lang_map.iteritems():
    temp_map[k]=len(v)
    for filename in v:
        try:
            filename=str(filename)
        except:
            continue
        filename= filename.strip().split('.')[1]
        if('js' in filename):
            filename='js'
        elif('php' in filename):
            filename='php'
        elif('csv' in filename):
            filename='csv'
        elif('do' in filename):
            filename='doc'
        elif('pl' in filename):
            filename='pl'
        elif('py' in filename):
            filename='py'
        elif('xml' in filename):
            filename='xml'
        elif('rss' in filename):
            filename='rss'
        elif('cgi' in filename):
            filename='cgi'
        elif('css' in filename):
            filename='css'
        elif('html' in filename):
            filename='html'
        elif('aspx' in filename):
            filename='aspx'
        elif('axd' in filename):
            filename='axd'
        elif('htm' in filename):
            filename='htm'
        elif('cfm' in filename):
            filename='cfm'
        elif('txt' in filename):
            filename='txt'
        elif('asp' in filename):
            filename='asp'
        elif('jpg' in filename):
            filename='jpg'
        elif('jpeg' in filename):
            filename='jpeg'
        elif('pdf' in filename):
            filename='pdf'
        elif('png' in filename):
            filename='png'
        elif('gif' in filename):
            filename='gif'
        elif filename.isdigit() or any(char.isdigit() for char in filename) or '+' in filename or '-' in filename or '_' in filename or '&' in filename:
            continue
        #print filename
        list=file_type_map.get(k)
        if(list==None):
            file_type_map[k]=[]
            file_type_map[k].append(filename)
        else:
            if filename not in list:
                file_type_map[k].append(filename)

print file_type_map
with open("language_count.json",'a+') as f:
    f.write('[')
    for k,v in temp_map.iteritems():
        f.write('{'+'"'+'Language'+'"'+':'+'"'+k+'",')
        f.write('"'+'Count'+'"'+':'+'"'+str(v)+'",')
        list=file_type_map.get(k)
        list=str(list)
        f.write('"'+'FileTypes'+'"'+':'+list+'},')
    f.seek(-1, os.SEEK_END)
    f.truncate()
    f.write(']')