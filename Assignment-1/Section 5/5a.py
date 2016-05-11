import os
import sys
import math
fileopen=open("BFD1.txt",'rb')
if os.path.exists('BFD_Corelation.txt'):
    os.remove('BFD_Corelation.txt')
file_open=open("BFD_Corelation.txt",'a')
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

val=0
for line in fileopen.read().splitlines():
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
            octet_array[x]=float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/pdf'):
            pdf_array[x]=float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='text/html'):
            html_array[x]=float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='text/plain'):
            plain_array[x]=float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='image/png'):
            png_array[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='image/gif'):
            gif_array[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='image/jpeg'):
            jpeg_array[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/xhtml+xml'):
            xhtml_array[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/xml'):
            xml_array[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/rss+xml'):
            rss_array[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/x-sh'):
            sh_array[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
        elif(mime_type=='application/atom+xml'):
            atom_xml_array[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/gzip'):
            gzip_array[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/zip'):
            zip_array[x]= float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue
        elif(mime_type=='application/x-tika-msoffice'):
            office_array[x]=float(frequency.translate(None,'"},'))
            x+=1
            if(x==255):
                val=0
            continue

corelation_octet_array=[]
corelation_pdf_array=[]
corelation_html_array=[]
corelation_plain_array=[]
corelation_png_array=[]
corelation_gif_array=[]
corelation_jpeg_array=[]
corelation_xhtml_array=[]
corelation_xml_array=[]
corelation_rss_array=[]
corelation_sh_array=[]
corelation_atom_xml_array=[]
corelation_gzip_array=[]
corelation_zip_array=[]
corelation_office_array=[]

corelation_octet_array=initArray(octet_array)
corelation_pdf_array=initArray(pdf_array)
corelation_html_array=initArray(html_array)
corelation_plain_array=initArray(plain_array)
corelation_png_array=initArray(png_array)
corelation_gif_array=initArray(gif_array)
corelation_jpeg_array=initArray(jpeg_array)
corelation_xhtml_array=initArray(xhtml_array)
corelation_xml_array=initArray(xml_array)
corelation_rss_array=initArray(rss_array)
corelation_sh_array=initArray(sh_array)
corelation_atom_xml_array=initArray(atom_xml_array)
corelation_gzip_array=initArray(gzip_array)
corelation_zip_array=initArray(zip_array)
corelation_office_array=initArray(office_array)

arg1=str(sys.argv[1])
temp= []
initArray(temp)

tempArray=[]
fileopen=open("Mime.txt",'r')

def normalize(array):
    tempArray=[]
    tempArray=initArray(tempArray)
    max_frequency=-1
    for i in range(0,256):
        if(max_frequency<array[i]):
            max_frequency=array[i]
    if(max_frequency==0):
        max_frequency=1
    for i in range(0,256):
        tempArray[i]=float(array[i])/max_frequency
        tempArray[i]=math.sqrt(tempArray[i])
        tempArray[i]=round(tempArray[i],3)
    return tempArray

temp_array=[]
def createCorelationArray(temp,fing_array):
    temp_array=[0 for i in range(256)]
    for i in range(0,256):
        temp_array[i]=1-math.fabs(fing_array[i]-temp[i])
    return temp_array


def printArray(array,name):
    file_open.write('{'+ '"mimetype_corelation":'+'"'+name+'",\n[')
    for i in range(0,256):
        file_open.write('{'+ '"byte":'+'"'+str(i)+'",'+ '"frequency":'+'"'+str(array[i])+'"}')
        if(i!=255):
            file_open.write(',\n')
    file_open.write(']}\n')

def normalized_corelation(previous,current,count):
    temp_corelation=[]
    temp_corelation=initArray(temp_corelation)
    initArray(temp_corelation)
    for i in range(0,256):
        temp_corelation[i]=((previous[i]*count)+current[i])/(count+1)
        temp_corelation[i]=round(temp_corelation[i],3)
    return temp_corelation

dont=os.path.join(arg1,"testing")
for root, dirs, files in os.walk(arg1):
    if(root==dont):
        for file in files:
            path=os.path.join(root, file)
            print path
            statinfo=os.stat(path)
            if(statinfo.st_size!=0):
                name = os.path.join(file+".txt")
                if(file!='.DS_Store' and file.endswith(".txt")==False):
                    for lines in fileopen:
                        if file in lines:
                            fileType=lines.split(":")[1]
                            fileType=fileType[:-2]
                            break
                    with open(path, "rb") as fo:
                        string=fo.read()
                        temp=[]
                        temp=initArray(temp)
                        for line in string:
                            temp[ord(line)]= temp[ord(line)]+1
                        temp=normalize(temp)
                        temp1=[]
                        temp1=initArray(temp1)
                        temp2=[]
                        temp2=initArray(temp2)
                        if(fileType=='application/octet-stream'):
                            temp1=createCorelationArray(temp,octet_array)
                            temp2=normalized_corelation(corelation_octet_array,temp1,octet_count)
                            for i in range(0,256):
                                corelation_octet_array[i]=temp2[i]
                        elif(fileType=='application/pdf'):
                            temp1=createCorelationArray(temp,pdf_array)
                            temp2=normalized_corelation(corelation_pdf_array,temp1,pdf_count)
                            for i in range(0,256):
                                corelation_pdf_array[i]=temp2[i]
                        elif(fileType=='text/html'):
                            temp1=createCorelationArray(temp,html_array)
                            temp2=normalized_corelation(corelation_html_array,temp1,html_count)
                            for i in range(0,256):
                                corelation_html_array[i]=temp2[i]
                        elif(fileType=='text/plain'):
                            temp1=createCorelationArray(temp,plain_array)
                            temp2=normalized_corelation(corelation_plain_array,temp1,plain_count)
                            for i in range(0,256):
                                corelation_plain_array[i]=temp2[i]
                        elif(fileType=='image/png'):
                            temp1=createCorelationArray(temp,png_array)
                            temp2=normalized_corelation(corelation_png_array,temp1,png_count)
                            for i in range(0,256):
                                corelation_png_array[i]=temp2[i]
                        elif(fileType=='image/gif'):
                            temp1=createCorelationArray(temp,gif_array)
                            temp2=normalized_corelation(corelation_gif_array,temp1,gif_count)
                            for i in range(0,256):
                                corelation_gif_array[i]=temp2[i]
                        elif(fileType=='image/jpeg'):
                            temp1=createCorelationArray(temp,jpeg_array)
                            temp2=normalized_corelation(corelation_jpeg_array,temp1,jpeg_count)
                            for i in range(0,256):
                                corelation_jpeg_array[i]=temp2[i]
                        elif(fileType=='application/xhtml+xml'):
                            temp1=createCorelationArray(temp,xhtml_array)
                            temp2=normalized_corelation(corelation_xhtml_array,temp1,xhtml_count)
                            for i in range(0,256):
                                corelation_xhtml_array[i]=temp2[i]
                        elif(fileType=='application/xml'):
                            temp1=createCorelationArray(temp,xml_array)
                            temp2=normalized_corelation(corelation_xml_array,temp1,xml_count)
                            for i in range(0,256):
                                corelation_xml_array[i]=temp2[i]
                        elif(fileType=='application/rss+xml'):
                            temp1=createCorelationArray(temp,rss_array)
                            temp2=normalized_corelation(corelation_rss_array,temp1,rss_count)
                            for i in range(0,256):
                                corelation_rss_array[i]=temp2[i]
                        elif(fileType=='application/x-sh'):
                            temp1=createCorelationArray(temp,sh_array)
                            temp2=normalized_corelation(corelation_sh_array,temp1,sh_count)
                            for i in range(0,256):
                                corelation_sh_array[i]=temp2[i]
                        elif(fileType=='application/atom+xml'):
                            temp1=createCorelationArray(temp,atom_xml_array)
                            temp2=normalized_corelation(corelation_atom_xml_array,temp1,atom_xml_count)
                            for i in range(0,256):
                                corelation_atom_xml_array[i]=temp2[i]
                        elif(fileType=='application/gzip'):
                            temp1=createCorelationArray(temp,gzip_array)
                            temp2=normalized_corelation(corelation_gzip_array,temp1,gzip_count)
                            for i in range(0,256):
                                corelation_gzip_array[i]=temp2[i]
                        elif(fileType=='application/zip'):
                            temp1=createCorelationArray(temp,zip_array)
                            temp2=normalized_corelation(corelation_zip_array,temp1,zip_count)
                            for i in range(0,256):
                                corelation_zip_array[i]=temp2[i]
                        elif(fileType=='application/x-tika-msoffice'):
                            temp1=createCorelationArray(temp,office_array)
                            temp2=normalized_corelation(corelation_office_array,temp1,office_count)
                            for i in range(0,256):
                                corelation_office_array[i]=temp2[i]



printArray(corelation_octet_array,'application/octet-stream')
printArray(corelation_pdf_array,"application/pdf")
printArray(corelation_html_array,"text/html")
printArray(corelation_plain_array,"text/plain")
printArray(corelation_png_array,"image/png")
printArray(corelation_gif_array,"image/gif")
printArray(corelation_jpeg_array,"image/jpeg")
printArray(corelation_xhtml_array,"application/xhtml+xml")
printArray(corelation_xml_array,"application/xml")
printArray(corelation_rss_array,"application/rss+xml")
printArray(corelation_sh_array,"application/x-sh")
printArray(corelation_atom_xml_array,"application/atom+xml")
printArray(corelation_gzip_array,"application/gzip")
printArray(corelation_zip_array,"application/zip")
printArray(corelation_office_array,'application/x-tika-msoffice')