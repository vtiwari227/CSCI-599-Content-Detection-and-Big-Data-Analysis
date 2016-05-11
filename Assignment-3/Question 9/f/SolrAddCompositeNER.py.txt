import json
import os
from urllib2 import *

myPath='C:/Users/Snehal/Documents/tikaSimilarityTestSet/CompositeNER'
for file in os.listdir(myPath):
    if file.endswith("Agreement.json"):
        filename= myPath+'/'+file
        fileNo=0
        series=fileNo*1000
        fileNo+=1
        with open(filename, 'rb') as data_file:
            my_data = data_file.read()
        arr= json.loads(my_data)

        newJSON=arr["JointAgreement"]
        count=series+1
        for j in newJSON:
            str2=j
            curl_cmd = ' curl "http://localhost:8983/solr/gettingstarted/update/json/docs?commit=true" '+ ' -d '+str(str2)
            cmd="http://localhost:8983/solr/gettingstarted/update/json/docs?commit=true"
            req = Request(url=cmd,data=str2)
            req.add_header('Content-type', 'application/json')

            print "Posting Composite NER data for : "+j['DOI']


            #using http request
            try:
                f = urlopen(req)
            except URLError:
                print "Error posting data. No Connection to SOLR \n "+cmd


            #using curl
            #print curl_cmd
            #file1= os.popen(curl_cmd)

            count+=1
        #print file
    print count