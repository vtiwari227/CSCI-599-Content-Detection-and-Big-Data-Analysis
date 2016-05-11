import sys
import os
arg1=str(sys.argv[1])
count=0
flag=False
output=open("relevent.json",'a+')
output.write('[')
for root, dirs, files in os.walk(arg1):
    for file in files:
        if(file!='.DS_Store'):
            count+=1
            print count
            path=os.path.join(root, file)
            f=open(path,'r')
            for line in f:
                if not flag:
                    if 'response' in line:
                        flag=True
                else:
                    if 'hostname' in line:
                        hostname=line
                    if 'body' in line:
                        body_len=len(line)
                    if 'key' in line:
                        key=line
            try:
                hostname=hostname.split(':')[1]
                hostname=hostname.strip()
                hostname=hostname[1:-2]
                key=key.split(':')[1]
                key=key.strip()
                key=key[1:-2]
                hostname=hostname.split('.')
                key=key.split('_')
                flag2=True
            except:
                continue
            for i in range(0,len(hostname)):
                try:
                    if key[i]!=hostname[len(hostname)-i-1]:
                        flag2=False
                except:
                    output.write('{'+'"'+file+'"'+':'+'"'+'No'+'"'+'},')
                    continue
            if flag2 and  body_len>5000:
                output.write('{'+'"'+file+'"'+':'+'"'+'Yes'+'"'+'},')
            else:
                output.write('{'+'"'+file+'"'+':'+'"'+'No'+'"'+'},')

output.write(']')