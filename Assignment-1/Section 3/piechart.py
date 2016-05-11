import urllib, string, os, json
url='https://github.com/chrismattmann/trec-dd-polar/'
jsonurl = urllib.urlopen(url)
fw=open("output.txt",'w')
text = jsonurl.read()
output_json=''
if os.path.exists('output.json'):
    os.remove('output.json')
fjson=open("output.json",'a')
fjson.write('[')
flag=False
for line in text:
    fw.write(line)
fopen=open('output.txt','r')
for lines in fopen:
    if lines=='\n':
        continue
    else:
        if lines=='<pre><code>Total: 1,741,530 records\n' and flag==False:
            flag=True
            continue
        if lines=='}\n':
            flag=False
            fjson.seek(-1, os.SEEK_END)
            fjson.truncate()
        if flag==True and lines!='{\n':
            word=lines.split(':')
            str1=word[0].replace(' ','')
            data={'Application_Name':word[0],'Count':word[1]}
            str1=str1[1:-1]
            str2=word[1]
            str2=str2[2:len(str2)-3]
            fjson.write(json.dumps({'Mime_Type': str1,'Size': str2}))
            fjson.write(',')
            fjson.write('\n')
fjson.seek(-1, os.SEEK_END)
fjson.truncate()
fjson.write(']')



