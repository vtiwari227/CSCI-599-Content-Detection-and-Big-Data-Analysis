import os
import sys
import json
import math
arg1=str(sys.argv[1])
octet_array=[[]]
pdf_array=[[]]
html_array=[[]]
plain_array=[[]]
png_array=[[]]
gif_array=[[]]
jpeg_array=[[]]
xhtml_array=[[]]
xml_array=[[]]
rss_array=[[]]
sh_array=[[]]
atom_xml_array=[[]]
gzip_array=[[]]
zip_array=[[]]
office_array=[[]]
octet_count=0
pdf_count=0
html_count=0
plain_count=0
png_count=0
gif_count=0
jpeg_count=0
xhtml_count=0
xml_count=0
rss_count=0
sh_count=0
atom_xml_count=0
gzip_count=0
zip_count=0
office_count=0

fileopen=open("Mime.txt",'r')
"""if os.path.exists('BFCC.txt'):
    os.remove('BFCC.txt')
file_open=open("BFCC.txt",'a')"""

def initArray():
    matrix = [[0 for i in range(0,256)] for j in range(0,256)]
    return matrix

octet_array=initArray()
pdf_array=initArray()
html_array=initArray()
plain_array=initArray()
png_array=initArray()
gif_array=initArray()
jpeg_array=initArray()
xhtml_array=initArray()
xml_array=initArray()
rss_array=initArray()
sh_array=initArray()
atom_xml_array=initArray()
gzip_array=initArray()
zip_array=initArray()
office_array=initArray()

octet_array_fingerprint=[]
pdf_array_fingerprint=[]
html_array_fingerprint=[]
plain_array_fingerprint=[]
png_array_fingerprint=[]
gif_array_fingerprint=[]
jpeg_array_fingerprint=[]
xhtml_array_fingerprint=[]
xml_array_fingerprint=[]
rss_array_fingerprint=[]
sh_array_fingerprint=[]
atom_xml_array_fingerprint=[]
gzip_array_fingerprint=[]
zip_array_fingerprint=[]
office_array_fingerprint=[]



octet_array_fingerprint=[0 for i in range(0,256)]
pdf_array_fingerprint=[0 for i in range(0,256)]
html_array_fingerprint=[0 for i in range(0,256)]
plain_array_fingerprint=[0 for i in range(0,256)]
png_array_fingerprint=[0 for i in range(0,256)]
gif_array_fingerprint=[0 for i in range(0,256)]
jpeg_array_fingerprint=[0 for i in range(0,256)]
xhtml_array_fingerprint=[0 for i in range(0,256)]
xml_array_fingerprint=[0 for i in range(0,256)]
rss_array_fingerprint=[0 for i in range(0,256)]
sh_array_fingerprint=[0 for i in range(0,256)]
atom_xml_array_fingerprint=[0 for i in range(0,256)]
gzip_array_fingerprint=[0 for i in range(0,256)]
zip_array_fingerprint=[0 for i in range(0,256)]
office_array_fingerprint=[0 for i in range(0,256)]


file_finger=open("BFD1.txt",'rb')
val=0
for line in file_finger.read().splitlines():
    type= line.split(':')[0]
    type=''.join(e for e in type if e.isalnum())
    if(type=="mimetype"):
        mime_type=line.split(':')[1]
        mime_type=mime_type.translate(None,'",')
        val=1
        x=0
        continue
    if(val==1):
        frequency= line.split(':')[2]
        if(mime_type=='application/octet-stream'):
            octet_array_fingerprint[x]=float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/pdf'):
            pdf_array_fingerprint[x]=float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='text/html'):
            html_array_fingerprint[x]=float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='text/plain'):
            plain_array_fingerprint[x]=float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='image/png'):
            png_array_fingerprint[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='image/gif'):
            gif_array_fingerprint[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='image/jpeg'):
            jpeg_array_fingerprint[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/xhtml+xml'):
            xhtml_array_fingerprint[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/xml'):
            xml_array_fingerprint[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/rss+xml'):
            rss_array_fingerprint[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/x-sh'):
            sh_array_fingerprint[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
        elif(mime_type=='application/atom+xml'):
            atom_xml_array_fingerprint[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/gzip'):
            gzip_array_fingerprint[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/zip'):
            zip_array_fingerprint[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/x-tika-msoffice'):
            office_array_fingerprint[x]=float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue




def normalize(array):
    max_frequency=-1
    temp_array=[]
    temp_array=initArray()
    for i in range(0,256):
        if(max_frequency<array[i]):
            max_frequency=array[i]
        if(max_frequency==0):
            max_frequency=1
    for i in range(0,256):
        temp_array[i]=float(array[i])/max_frequency
        temp_array[i]=math.sqrt(temp_array[i])
        temp_array[i]=round(temp_array[i],3)
    return temp_array

tempArray=[[]]

def buildCrossCorelation(matrix):
    tempArray=initArray()
    for i in range(0,256):
        for j in range(i+1,256):
            tempArray[j][i]=math.fabs(matrix[i]-matrix[j])
    return tempArray

temp_array=[[]]

def averageCrossCorelation(orig,new,count):
    temp_array=initArray()
    for i in range(0,256):
        for j in range(i+1,256):
            temp_array[j][i]=((orig[j][i]*(count-1))+new[j][i])/float(count)
            temp_array[j][j]=round(temp_array[j][i],3)
    return temp_array

tempCorelation=[[]]

def corelationStrength(bytearray,fingerprint):
    tempCorelation=initArray()
    for i in range(0,256):
        for j in range(i+1,256):
            tempCorelation[i][j]=1-math.fabs(bytearray[i]-fingerprint[j])
    return tempCorelation

tempCorelationAverage=[[]]

def averageCrossCorelationStrength(orig,new,count):
    tempCorelationAverage=initArray()
    for i in range(0,256):
        for j in range(i+1,256):
            tempCorelationAverage[i][j]=((orig[i][j]*(count-1))+new[i][j])/float(count)
            tempCorelationAverage[i][j]=round(tempCorelationAverage[i][j],3)
    return tempCorelationAverage

count_files=0
dont=os.path.join(arg1,"testing")
for root, dirs, files in os.walk(arg1):
    if(len(files)>0):
        for file in files:
            temp1=[0 for i in range(0,256)]
            if(file!='.DS_Store'):
                for lines in fileopen:
                    if file in lines:
                        fileType=lines.split(":")[1]
                        fileType=fileType[:-2]
                        break
                print fileType
                path=os.path.join(root, file)
                #print path
                dont= str(path)
                if(dont.__contains__('/test/')and file.endswith(".txt")==False):
                    print path
                    count_files+=1
                    print count_files

                    with open(path, "r") as fo:
                        string = fo.read()
                    for line in string:
                        temp1[ord(line)]= temp1[ord(line)]+1
                    temp1=normalize(temp1)
                    temp2=[[]]
                    temp2=initArray()
                    temp3=[[]]
                    temp3=initArray()
                    temp4=[[]]
                    temp4=initArray()
                    temp5=[[]]
                    temp5=initArray()
                    if(fileType=='application/octet-stream'):
                        temp2=buildCrossCorelation(temp1)
                        octet_count+=1
                        temp3=averageCrossCorelation(octet_array,temp2,octet_count)
                        temp4=corelationStrength(temp1,octet_array_fingerprint)
                        temp5=averageCrossCorelationStrength(octet_array,temp4,octet_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                octet_array[j][i]=temp3[j][i]
                                octet_array[i][j]=temp5[i][j]
                    elif(fileType=='application/pdf'):
                        temp2=buildCrossCorelation(temp1)
                        pdf_count+=1
                        temp3=averageCrossCorelation(pdf_array,temp2,pdf_count)
                        temp4=corelationStrength(temp1,pdf_array_fingerprint)
                        temp5=averageCrossCorelationStrength(pdf_array,temp4,pdf_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                pdf_array[j][i]=temp3[j][i]
                                pdf_array[i][j]=temp5[i][j]
                    elif(fileType=='text/html'):
                        temp2=buildCrossCorelation(temp1)
                        html_count+=1
                        temp3=averageCrossCorelation(html_array,temp2,html_count)
                        temp4=corelationStrength(temp1,html_array_fingerprint)
                        temp5=averageCrossCorelationStrength(html_array,temp4,html_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                html_array[j][i]=temp3[j][i]
                                html_array[i][j]=temp5[i][j]
                    elif(fileType=='text/plain'):
                        temp2=buildCrossCorelation(temp1)
                        plain_count+=1
                        temp3=averageCrossCorelation(plain_array,temp2,plain_count)
                        temp4=corelationStrength(temp1,plain_array_fingerprint)
                        temp5=averageCrossCorelationStrength(plain_array,temp4,plain_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                plain_array[j][i]=temp3[j][i]
                                plain_array[i][j]=temp5[i][j]
                    elif(fileType=='image/png'):
                        temp2=buildCrossCorelation(temp1)
                        png_count+=1
                        temp3=averageCrossCorelation(png_array,temp2,png_count)
                        temp4=corelationStrength(temp1,png_array_fingerprint)
                        temp5=averageCrossCorelationStrength(png_array,temp4,png_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                png_array[j][i]=temp3[j][i]
                                png_array[i][j]=temp5[i][j]
                    elif(fileType=='image/gif'):
                        temp2=buildCrossCorelation(temp1)
                        gif_count+=1
                        temp3=averageCrossCorelation(gif_array,temp2,gif_count)
                        temp4=corelationStrength(temp1,gif_array_fingerprint)
                        temp5=averageCrossCorelationStrength(gif_array,temp4,gif_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                gif_array[j][i]=temp3[j][i]
                                gif_array[i][j]=temp5[i][j]
                    elif(fileType=='image/jpeg'):
                        temp2=buildCrossCorelation(temp1)
                        jpeg_count+=1
                        temp3=averageCrossCorelation(jpeg_array,temp2,jpeg_count)
                        temp4=corelationStrength(temp1,jpeg_array_fingerprint)
                        temp5=averageCrossCorelationStrength(jpeg_array,temp4,jpeg_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                jpeg_array[j][i]=temp3[j][i]
                                jpeg_array[i][j]=temp5[i][j]
                    elif(fileType=='application/xhtml+xml'):
                        temp2=buildCrossCorelation(temp1)
                        xhtml_count+=1
                        temp3=averageCrossCorelation(xhtml_array,temp2,xhtml_count)
                        temp4=corelationStrength(temp1,xhtml_array_fingerprint)
                        temp5=averageCrossCorelationStrength(xhtml_array,temp4,xhtml_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                xhtml_array[j][i]=temp3[j][i]
                                xhtml_array[i][j]=temp5[i][j]
                    elif(fileType=='application/xml'):
                        temp2=buildCrossCorelation(temp1)
                        xml_count+=1
                        temp3=averageCrossCorelation(xml_array,temp2,xml_count)
                        temp4=corelationStrength(temp1,xml_array_fingerprint)
                        temp5=averageCrossCorelationStrength(xml_array,temp4,xml_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                xml_array[j][i]=temp3[j][i]
                                xml_array[i][j]=temp5[i][j]
                    elif(fileType=='application/rss+xml'):
                        temp2=buildCrossCorelation(temp1)
                        rss_count+=1
                        temp3=averageCrossCorelation(rss_array,temp2,rss_count)
                        temp4=corelationStrength(temp1,rss_array_fingerprint)
                        temp5=averageCrossCorelationStrength(rss_array,temp4,rss_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                rss_array[j][i]=temp3[j][i]
                                rss_array[i][j]=temp5[i][j]
                    elif(fileType=='application/x-sh'):
                        temp2=buildCrossCorelation(temp1)
                        sh_count+=1
                        temp3=averageCrossCorelation(sh_array,temp2,sh_count)
                        temp4=corelationStrength(temp1,sh_array_fingerprint)
                        temp5=averageCrossCorelationStrength(sh_array,temp4,sh_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                sh_array[j][i]=temp3[j][i]
                                sh_array[i][j]=temp5[i][j]
                    elif(fileType=='application/atom+xml'):
                        temp2=buildCrossCorelation(temp1)
                        atom_xml_count+=1
                        temp3=averageCrossCorelation(atom_xml_array,temp2,atom_xml_count)
                        temp4=corelationStrength(temp1,atom_xml_array_fingerprint)
                        temp5=averageCrossCorelationStrength(atom_xml_array,temp4,atom_xml_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                atom_xml_array[j][i]=temp3[j][i]
                                atom_xml_array[i][j]=temp5[i][j]
                    elif(fileType=='application/gzip'):
                        temp2=buildCrossCorelation(temp1)
                        gzip_count+=1
                        temp3=averageCrossCorelation(gzip_array,temp2,gzip_count)
                        temp4=corelationStrength(temp1,gzip_array_fingerprint)
                        temp5=averageCrossCorelationStrength(gzip_array,temp4,gzip_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                gzip_array[j][i]=temp3[j][i]
                                gzip_array[i][j]=temp5[i][j]
                    elif(fileType=='application/zip'):
                        temp2=buildCrossCorelation(temp1)
                        zip_count+=1
                        temp3=averageCrossCorelation(zip_array,temp2,zip_count)
                        temp4=corelationStrength(temp1,zip_array_fingerprint)
                        temp5=averageCrossCorelationStrength(zip_array,temp4,zip_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                zip_array[j][i]=temp3[j][i]
                                zip_array[i][j]=temp5[i][j]
                    elif(fileType=='application/x-tika-msoffice'):
                        temp2=buildCrossCorelation(temp1)
                        office_count+=1
                        temp3=averageCrossCorelation(office_array,temp2,office_count)
                        temp4=corelationStrength(temp1,office_array_fingerprint)
                        temp5=averageCrossCorelationStrength(office_array,temp4,office_count)
                        for i in range(0,256):
                            for j in range(i+1,256):
                                office_array[j][i]=temp3[j][i]
                                office_array[i][j]=temp5[i][j]
                fileopen.seek(0)

"""def printArray(array,name):
    file_open.write('{'+ '"mimetype":'+'"'+name+'"\n[')
    for i in range(0,256):
        file_open.write('{'+ '"byte'+str(i)+'"\n[')
        for j in range(0,256):
            file_open.write('{'+ '"bit":'+'"'+str(j)+'",'+ '"frequency":'+'"'+str(array[i][j])+'"}')
            if(j<255):
                file_open.write(',')
            file_open.write('\n')
        if(j<255):
            file_open.write(']},\n')
    if(i<255):
        file_open.write(',\n')
    file_open.write(']}\n')"""

rootDir=os.path.join(arg1,'corelation_files')
if not os.path.isdir(rootDir):
   os.makedirs(rootDir)

def printArray(array,name):
    filename=os.path.join(rootDir, name+".txt")
    if os.path.exists(filename):
        os.remove(filename)
    file_open=open(filename,'a')
    file_open.write('[')
    for i in range(0,256):
        file_open.write('{'+ '"byte"'+':'+'"'+str(i)+'",'+ '"output"'+':'+ '[\n')
        for j in range(0,256):
            file_open.write('{'+ '"bit":'+'"'+str(j)+'",'+ '"frequency":'+'"'+str(array[i][j])+'"}')
            if(j<255):
                file_open.write(',\n')
        file_open.write(']}')
        if(i<255):
            file_open.write(',\n')
    #file_open.seek(-1, os.SEEK_END)
    #file_open.truncate()
    file_open.write(']')

printArray(octet_array,'octet-stream')
printArray(pdf_array,'pdf')
printArray(html_array,'html')
printArray(plain_array,'plain')
printArray(png_array,'png')
printArray(gif_array,'gif')
printArray(jpeg_array,'jpeg')
printArray(xhtml_array,'xhtml+xml')
printArray(xml_array,'xml')
printArray(rss_array,'rss+xml')
printArray(sh_array,'x-sh')
printArray(atom_xml_array,'atom+xml')
printArray(gzip_array,'gzip')
printArray(zip_array,'zip')
printArray(office_array,'x-tika-msoffice')