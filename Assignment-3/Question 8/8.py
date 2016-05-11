import tika
from tika import parser
import os
import sys
from tika import language
import json
import codecs
arg1=str(sys.argv[1])
if os.path.exists('word_cloud.json'):
    os.remove('word_cloud.json')
word_cloud_map={}
sweet_map={}
word_cloud={}
with open("sweet.json") as fileop:
    dict_from_file = eval(fileop.read())
    sweet_map=dict_from_file
count=1
for k in sweet_map:
    for key,value in k.iteritems():
        if(count==1):
            text=value
            count+=1
        else:
            count=value
            count=1
    if text not in word_cloud_map:
        word_cloud_map[text]=count
    else:
        word_cloud_map[text]+=count

def printMap(tag,filename):
    if os.path.exists(filename):
        os.remove(filename)
    with open(filename,'a+') as fopen:
        json.dump(tag,fopen)
count=0
stop_words={'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "arent", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "cant", 'cannot', 'could', "couldnt", 'did', "didnt", 'do', 'does', "doesnt", 'doing', "dont", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadnt", 'has', "hasnt", 'have', "havent", 'having', 'he', "hed", "hes", 'her', 'here', "heres", 'hers', 'herself', 'him', 'himself', 'his', 'how', "hows", 'i', "id", "im", "ive", 'if', 'in', 'into', 'is', "isnt", 'it', "its", 'its', 'itself', "lets", 'me', 'more', 'most', "mustnt", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', "shant", 'she', "shed", "shes", 'should', "shouldnt", 'so', 'some', 'such', 'than', 'that', "thats", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "theres", 'these', 'they', "theyd", "theyll", "theyre", "theyve", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasnt", 'we', "we'd", "well", "were", "weve", 'were', "werent", 'what', "whats", 'when', "whens", 'where', "wheres", 'which', 'while', 'who', "whos", 'whom', 'why', "whys", 'with', "wont", 'would', "wouldnt", 'you', "youd", "youll", "youre", "youve", 'your', 'yours', 'yourself', 'yourselves'}
for root, dirs, files in os.walk(arg1):
    for file in files:
        path=''
        if(file!='.DS_Store'):
            count+=1
            print count
            path=os.path.join(root, file)
            tika.initVM()
            try:
                parsed = parser.from_file(path)
            except:
                continue
            if("content" in parsed.keys() and "metadata" in parsed.keys()):
                metadata=parsed["metadata"]
                content=parsed["content"]
                #print content
                #print metadata
                if(content is not None and metadata is not None):
                    if(len(metadata)>0 and len(content)>0):
                        print path
                        try:
                            lang=language.from_file(path)
                        except:
                            lang='en'
                        content=content.strip()
                        content=" ".join(content.split())
                        content=content.replace('\n','')
                        content=content.split(' ')
                        #print metadata
                        #print content
                        print lang
                        for key,word1 in metadata.iteritems():
                            try:
                                word1=str(word1)
                                word1.decode('utf-8')
                            except:
                                continue
                            #print word1
                            if word1 not in stop_words and len(word1)>3 and len(word1)<14:
                                if word1 not in word_cloud_map:
                                    word_cloud_map[word1]=1
                                else:
                                    word_cloud_map[word1]+=1
                        for word2 in content:
                            try:
                                word2.decode('utf-8')
                            except:
                                continue
                            if word2 not in stop_words and len(word2)>3:
                                if word2 not in word_cloud_map:
                                    word_cloud_map[word2]=1
                                else:
                                    word_cloud_map[word2]+=1
                        if lang not in word_cloud_map:
                            word_cloud_map[lang]=1
                        else:
                            word_cloud_map[lang]+=1

printMap(word_cloud_map,"word_cloud.json")



