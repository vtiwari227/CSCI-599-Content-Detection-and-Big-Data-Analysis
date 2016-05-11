import os
import sys
import json
import math
arg1=str(sys.argv[1])
octet_array=[]
pdf_array=[]
html_array=[]
plain_array=[]
png_array=[]
gif_array=[]
jpeg_array=[]
xhtml_array=[]
xml_array=[]
rss_array=[]
sh_array=[]
atom_xml_array=[]
gzip_array=[]
zip_array=[]
office_array=[]
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
if os.path.exists('BFD.txt'):
    os.remove('BFD.txt')
file_open=open("BFD.txt",'a')
file_open.write('[')

def initArray(array):
    array=[0 for i in range(0,256)]
    return array

octet_array=initArray(octet_array)
pdf_array=initArray(pdf_array)
html_array=initArray(html_array)
plain_array=initArray(plain_array)
png_array=initArray(png_array)
gif_array=initArray(gif_array)
jpeg_array=initArray(jpeg_array)
xhtml_array=initArray(xhtml_array)
xml_array=initArray(xml_array)
rss_array=initArray(rss_array)
sh_array=initArray(sh_array)
atom_xml_array=initArray(atom_xml_array)
gzip_array=initArray(gzip_array)
zip_array=initArray(zip_array)
office_array=initArray(office_array)

def printArray(array,name):
    file_open.write('{'+ '"mimetype":'+'"'+name+'",\n[')
    for i in range(0,256):
        file_open.write('{'+ '"byte":'+'"'+str(i)+'",'+ '"frequency":'+'"'+str(array[i])+'"}')
        if(i!=255):
            file_open.write(',\n')
    file_open.write(']}\n')

def normalize(array):
    max_frequency=-1
    temp_array=[]
    temp_array=initArray(temp_array)
    for i in range(0,256):
        if(max_frequency<array[i]):
            max_frequency=array[i]
        if(max_frequency==0):
            max_frequency=1
    for i in range(0,256):
        temp_array[i]=float(array[i])/max_frequency
        temp_array[i]=math.sqrt(temp_array[i])
    return temp_array
    #printArray(array,max_frequency)

def updateFingerprint(array,count,orig_array):
    temp_fingerprint=[]
    temp_fingerprint=initArray(temp_fingerprint)
    for i in range(0,256):
        temp_fingerprint[i]=((orig_array[i]*count)+array[i])/(count+1)
        temp_fingerprint[i]=round(temp_fingerprint[i],3)
    return temp_fingerprint

dont=os.path.join(arg1,"testing")
for root, dirs, files in os.walk(arg1):
    if(len(files)>0):
        for file in files:
            temp1=[]
            temp2=[]
            temp1=initArray(temp1)
            temp2=initArray(temp2)
            if(file!='.DS_Store'):
                for lines in fileopen:
                    if file in lines:
                        fileType=lines.split(":")[1]
                        fileType=fileType[:-2]
                        break
                path=os.path.join(root, file)
                dont= str(path)
                if(dont.__contains__('/training/')and file.endswith(".txt")==False):
                    with open(path, "r") as fo:
                        string = fo.read()
                    for line in string:
                        temp1[ord(line)]= temp1[ord(line)]+1
                    temp1=normalize(temp1)
                    if(fileType=='application/octet-stream'):
                        temp2=updateFingerprint(temp1,octet_count,octet_array)
                        octet_count+=1
                        for i in range(0,256):
                            octet_array[i]=temp2[i]
                    elif(fileType=='application/pdf'):
                        temp2=updateFingerprint(temp1,pdf_count,pdf_array)
                        pdf_count+=1
                        for i in range(0,256):
                            pdf_array[i]=temp2[i]
                    elif(fileType=='text/html'):
                        temp2=updateFingerprint(temp1,html_count,html_array)
                        html_count+=1
                        for i in range(0,256):
                            html_array[i]=temp2[i]
                    elif(fileType=='text/plain'):
                        temp2=updateFingerprint(temp1,plain_count,plain_array)
                        plain_count+=1
                        for i in range(0,256):
                            plain_array[i]= temp2[i]
                    elif(fileType=='image/png'):
                        temp2=updateFingerprint(temp1,png_count,png_array)
                        png_count+=1
                        for i in range(0,256):
                            png_array[i]= temp2[i]
                    elif(fileType=='image/gif'):
                        temp2=updateFingerprint(temp1,gif_count,gif_array)
                        gif_count+=1
                        for i in range(0,256):
                            gif_array[i]= temp2[i]
                    elif(fileType=='image/jpeg'):
                        temp2=updateFingerprint(temp1,jpeg_count,jpeg_array)
                        jpeg_count+=1
                        for i in range(0,256):
                            jpeg_array[i]= temp2[i]
                    elif(fileType=='application/xhtml+xml'):
                        temp2=updateFingerprint(temp1,xhtml_count,xhtml_array)
                        xhtml_count+=1
                        for i in range(0,256):
                            xhtml_array[i]= temp2[i]
                    elif(fileType=='application/xml'):
                        temp2=updateFingerprint(temp1,xml_count,xml_array)
                        xml_count+=1
                        for i in range(0,256):
                            xml_array[i]= temp2[i]
                    elif(fileType=='application/rss+xml'):
                        temp2=updateFingerprint(temp1,rss_count,rss_array)
                        rss_count+=1
                        for i in range(0,256):
                            rss_array[i]= temp2[i]
                    elif(fileType=='application/x-sh'):
                        temp2=updateFingerprint(temp1,sh_count,sh_array)
                        sh_count+=1
                        for i in range(0,256):
                            sh_array[i]= temp2[i]
                    elif(fileType=='application/atom+xml'):
                        temp2=updateFingerprint(temp1,atom_xml_count,atom_xml_array)
                        atom_xml_count+=1
                        for i in range(0,256):
                            atom_xml_array[i]= temp2[i]
                    elif(fileType=='application/gzip'):
                        temp2=updateFingerprint(temp1,gzip_count,gzip_array)
                        gzip_count+=1
                        for i in range(0,256):
                            gzip_array[i]= temp2[i]
                    elif(fileType=='application/zip'):
                        temp2=updateFingerprint(temp1,zip_count,zip_array)
                        zip_count+=1
                        for i in range(0,256):
                            zip_array[i]= temp2[i]
                    elif(fileType=='application/x-tika-msoffice'):
                        temp2=updateFingerprint(temp1,office_count,office_array)
                        office_count+=1
                        for i in range(0,256):
                            office_array[i]= temp2[i]
                fileopen.seek(0)

printArray(octet_array,'application/octet-stream')
printArray(pdf_array,"application/pdf")
printArray(html_array,"text/html")
printArray(plain_array,"text/plain")
printArray(png_array,"image/png")
printArray(gif_array,"image/gif")
printArray(jpeg_array,"image/jpeg")
printArray(xhtml_array,"application/xhtml+xml")
printArray(xml_array,"application/xml")
printArray(rss_array,"application/rss+xml")
printArray(sh_array,"application/x-sh")
printArray(atom_xml_array,"application/atom+xml")
printArray(gzip_array,"application/gzip")
printArray(zip_array,"application/zip")
printArray(office_array,'application/x-tika-msoffice')

file_open.write(']')


"""print octet_array
print office_array
print zip_array
print gzip_array
print atom_xml_array
print pdf_array
print jpeg_array
print gif_array
print png_array
print rss_array
print sh_array
print html_array
print plain_array
print xhtml_array
print xml_array"""

