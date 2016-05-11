----------------------------------------READ ME.txt Question 9-----------------------------------

Folder wise description to facilitate usage of the NER modules separetely as follows:

a. NLTK Rest Server- User can use the python files in 2 modes.  
   Use NLTKRESTServer.py to start a localhost server at 8881 server
   Use the NLTK library to point to files in the local file system. Use nltk.download('all') if your program is not able to find the correct models to load. This will create a nltk_data folder in temp directory for its use.
   Description - The nltk uses the POS tokenizer to read the content and mark as pos token ,for NER we are going to filter on 'NE' for named entity tags, for more chunking you can also consider 'NN' for Nouns.  Dependency on nltk python library.Output as entity in set "NAMES".  Now we have NLTK Rest server running we can integrate a progarm in python or java to talk to the using a http client to talk to the nltk server. Refer the NLTKRest.java file for explicit use of NLTKNERRecognizer.java  . It returns the list of NER entities.
  
b. CoreNLP.java integrates the tika with the CoreNLPRecognizer. We have given a facility for you to give the path to your classifier as required in the constructor to take 3,5 or all 7 ( Refer folder classifier) entities - [LOCATION, ORGANIZATION, DATE, MONEY, PERSON, PERCENT, TIME]

c. OpenNLP.java integrates the tika with the OpenNLPRecognizer. We have given a facility for you to give the path of your MODEL_DIR as required in the constructor. There are mainly 7 ( Refer folder models) [LOCATION, ORGANIZATION, DATE, MONEY, PERSON, PERCENT, TIME] models, also available in language like es, fr etc . It uses the opennlp-tools.jar which are bundled inthe tika.

d. Grobid quantity extrcats the measurements used in the content as a special measurement NER, which are very useful in extracting the range,max and min spectrums.

e. CompositeNERParser lets you combine and analyze the NER extrcation from files, and also gives a join maximal agreement between the three techniques mentioned above. These techniques differ in their manner of tokenization and chunking and has some overall between the extracted named entities. It generates the intersection and union between all NER techniques.
     
f. The program in e generates the JointAgreement.json for non empty sets and can be used to compare how each NER performed. The d3 gives a powerful mean to compare these side by type with detailed int=formation.

g.  We found that the joint agreement to be very useful but not necessary to be sufficient in most of the cases.Hence, shoving all the 3 NER or superset of them is very useful in enriching the metadata. You can use the SOLRAddCompositeNER.py to post the requests to the running SOLR  over http connection. You can exploit this module to mould your decision to post your metadata for documents seemlessle identified with DOI as id.


   