import os, sys
import math
arg1=str(sys.argv[1])

fileopen=open("Mime.txt",'r')
if os.path.exists('FHT_16.txt'):
    os.remove('FHT_16.txt')
if os.path.exists('FHT_8.txt'):
    os.remove('FHT_8.txt')
if os.path.exists('FHT_4.txt'):
    os.remove('FHT_4.txt')

fileopen1=open("FHT_16.txt",'a')
fileopen2=open("FHT_8.txt",'a')
fileopen3=open("FHT_4.txt",'a')
fileopen1.write('[')
fileopen2.write('[')
fileopen3.write('[')

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

def initArray(number):
    matrix = [[0 for i in range(0,256)] for j in range(0,number)]
    return matrix


def normalize(array,count,number):
    tempArray=[[]]
    #count=1176
    tempArray=initArray(number)
    for i in range(0,number):
        for j in range(0,256):
            tempArray[i][j]=float(array[i][j])/count
            if(tempArray[i][j]>0):
                print tempArray[i][j]
    tempArray[0][0]=count
    return tempArray



def printArray(array,name,number,fileop):
    rootDir=os.path.join('/Users/anirbanmishra/Downloads/FHT' ,'FHT_files')
    if not os.path.isdir(rootDir):
         os.makedirs(rootDir)
    if(number==16):
        path=os.path.join(rootDir,'FHT_16_files')
        if not os.path.isdir(path):
            os.makedirs(path)
    elif(number==8):
        path=os.path.join(rootDir,'FHT_8_files')
        if not os.path.isdir(path):
            os.makedirs(path)
    elif(number==4):
        path=os.path.join(rootDir,'FHT_4_files')
        if not os.path.isdir(path):
            os.makedirs(path)
    filename=os.path.join(path, name+".txt")
    if os.path.exists(filename):
        os.remove(filename)
    file_open=open(filename,'a')
    file_open.write('[')
    for i in range(0,number):
        file_open.write('{'+ '"byte"'+':'+'"'+str(i)+'",'+ '"output"'+':'+ '[\n')
        for j in range(0,256):
            file_open.write('{'+ '"bit":'+'"'+str(j)+'",'+ '"frequency":'+'"'+str(array[i][j])+'"}')
            if(j<255):
                file_open.write(',\n')
        file_open.write(']}')
        if(i<number-1):
            file_open.write(',\n')
    #file_open.seek(-1, os.SEEK_END)
    #file_open.truncate()
    file_open.write(']')

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

def fht(number,fileop):
    octet_array=initArray(number)
    pdf_array=initArray(number)
    html_array=initArray(number)
    plain_array=initArray(number)
    png_array=initArray(number)
    gif_array=initArray(number)
    jpeg_array=initArray(number)
    xhtml_array=initArray(number)
    xml_array=initArray(number)
    rss_array=initArray(number)
    sh_array=initArray(number)
    atom_xml_array=initArray(number)
    gzip_array=initArray(number)
    zip_array=initArray(number)
    office_array=initArray(number)
    var=0
    mime_dir=arg1
    countf=0
    for root, dirs, files in os.walk(arg1):
        if(len(files)>0):
            for file in files:
                if(file!='.DS_Store'):
                    for lines in fileopen:
                        if file in lines:
                            fileType=lines.split(":")[1]
                            fileType=fileType[:-2]
                            #print fileType+' '+file
                    path=os.path.join(root, file)
                    dont= str(path)
                    if(dont.__contains__('/training/')and file.endswith(".txt")==False):
                        print path
                        countf+=1
                        print countf
                        with open(path, "rb") as fo:
                            string = fo.read(number)
                            #print string
                            x=0
                            for line in string:
                                #print str(x)+' '+str(ord(line))
                                if(fileType=='application/octet-stream'):
                                    octet_array[x][ord(line)]= octet_array[x][ord(line)]+1
                                    x+=1
                                    continue
                                elif(fileType=='application/pdf'):
                                    pdf_array[x][ord(line)]= pdf_array[x][ord(line)]+1
                                    x+=1
                                    continue
                                elif(fileType=='text/html'):
                                    html_array[x][ord(line)]= html_array[x][ord(line)]+1
                                    x+=1
                                    continue
                                elif(fileType=='text/plain'):
                                    plain_array[x][ord(line)]= plain_array[x][ord(line)]+1
                                    x+=1
                                    continue
                                elif(fileType=='image/png'):
                                    png_array[x][ord(line)]= png_array[x][ord(line)]+1
                                    x+=1
                                    continue
                                elif(fileType=='image/gif'):
                                    gif_array[x][ord(line)]= gif_array[x][ord(line)]+1
                                    x+=1
                                    continue
                                elif(fileType=='image/jpeg'):
                                    jpeg_array[x][ord(line)]= jpeg_array[x][ord(line)]+1
                                    x+=1
                                    continue
                                elif(fileType=='application/xhtml+xml'):
                                    xhtml_array[x][int(ord(line))]= xhtml_array[x][int(ord(line))]+1
                                    x+=1
                                    continue
                                elif(fileType=='application/xml'):
                                    xml_array[x][ord(line)]= xml_array[x][ord(line)]+1
                                    x+=1
                                    continue
                                elif(fileType=='application/rss+xml'):
                                    rss_array[x][ord(line)]= rss_array[x][ord(line)]+1
                                    x+=1
                                    continue
                                elif(fileType=='application/x-sh'):
                                    sh_array[x][ord(line)]= sh_array[x][ord(line)]+1
                                    x+=1
                                    continue
                                elif(fileType=='application/atom+xml'):
                                    atom_xml_array[x][ord(line)]= atom_xml_array[x][ord(line)]+1
                                    x+=1
                                    continue
                                elif(fileType=='application/gzip'):
                                    gzip_array[x][ord(line)]= gzip_array[x][ord(line)]+1
                                    x+=1
                                    continue
                                elif(fileType=='application/zip'):
                                    zip_array[x][ord(line)]= zip_array[x][ord(line)]+1
                                    x+=1
                                    continue
                                elif(fileType=='application/x-tika-msoffice'):
                                    office_array[x][ord(line)]= office_array[x][ord(line)]+1
                                    x+=1
                                    continue
                            x=0
                    fileopen.seek(0)
                    #print file
                    if(fileType=='application/octet-stream'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global octet_count
                        octet_count+=1
                    elif(fileType=='application/pdf'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global pdf_count
                        pdf_count+=1
                    elif(fileType=='text/html'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global html_count
                        html_count+=1
                    elif(fileType=='text/plain'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global plain_count
                        plain_count+=1
                    elif(fileType=='image/png'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global png_count
                        png_count+=1
                    elif(fileType=='image/gif'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global gif_count
                        gif_count+=1
                    elif(fileType=='image/jpeg'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global jpeg_count
                        jpeg_count+=1
                    elif(fileType=='application/xhtml+xml'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global xhtml_count
                        xhtml_count+=1
                    elif(fileType=='application/xml'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global xml_count
                        xml_count+=1
                    elif(fileType=='application/rss+xml'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global rss_count
                        rss_count+=1
                    elif(fileType=='application/x-sh'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global sh_count
                        sh_count+=1
                    elif(fileType=='application/atom+xml'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global atom_xml_count
                        atom_xml_count+=1
                    elif(fileType=='application/gzip'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global gzip_count
                        gzip_count+=1
                    elif(fileType=='application/zip'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global zip_count
                        zip_count+=1
                    elif(fileType=='application/x-tika-msoffice'and file.endswith(".txt")==False and dont.__contains__('/training/')):
                        global office_count
                        office_count+=1
    """print octet_count
    print pdf_count
    print html_count
    print plain_count
    print png_count
    print gif_count
    print jpeg_count
    print xhtml_count
    print xml_count
    print rss_count
    print sh_count
    print atom_xml_count
    print gzip_count
    print zip_count
    print office_count"""
    octet_array=normalize(octet_array,octet_count,number)
    pdf_array=normalize(pdf_array,pdf_count,number)
    html_array=normalize(html_array,html_count,number)
    plain_array=normalize(plain_array,plain_count,number)
    png_array=normalize(png_array,png_count,number)
    gif_array=normalize(gif_array,gif_count,number)
    jpeg_array=normalize(jpeg_array,jpeg_count,number)
    xhtml_array=normalize(xhtml_array,xhtml_count,number)
    xml_array=normalize(xml_array,xml_count,number)
    rss_array=normalize(rss_array,rss_count,number)
    sh_array=normalize(sh_array,sh_count,number)
    atom_xml_array=normalize(atom_xml_array,atom_xml_count,number)
    gzip_array=normalize(gzip_array,gzip_count,number)
    zip_array=normalize(zip_array,zip_count,number)
    office_array=normalize(office_array,office_count,number)
    printArray(octet_array,'octet-stream',number,fileop)
    printArray(pdf_array,"pdf",number,fileop)
    printArray(html_array,"html",number,fileop)
    printArray(plain_array,"plain",number,fileop)
    printArray(png_array,"png",number,fileop)
    printArray(gif_array,"gif",number,fileop)
    printArray(jpeg_array,"jpeg",number,fileop)
    printArray(xhtml_array,"xhtml+xml",number,fileop)
    printArray(xml_array,"xml",number,fileop)
    printArray(rss_array,"rss+xml",number,fileop)
    printArray(sh_array,"x-sh",number,fileop)
    printArray(atom_xml_array,"atom+xml",number,fileop)
    printArray(gzip_array,"gzip",number,fileop)
    printArray(zip_array,"zip",number,fileop)
    printArray(office_array,'x-tika-msoffice',number,fileop)


fht(16,fileopen1)
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
fht(8,fileopen2)
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
fht(4,fileopen3)

fileopen1.write(']')
fileopen2.write(']')
fileopen3.write(']')

