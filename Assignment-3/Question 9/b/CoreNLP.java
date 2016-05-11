/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.usc.polar;

import java.io.FileInputStream;
import java.io.InputStream;

import java.util.Map;
import java.util.Set;
import org.json.simple.JSONObject;
import org.apache.tika.parser.AutoDetectParser;
import org.apache.tika.metadata.Metadata;
import org.apache.tika.parser.ner.corenlp.CoreNLPNERecogniser;
import org.apache.tika.sax.BodyContentHandler;


import edu.stanford.nlp.ie.AbstractSequenceClassifier;
import edu.stanford.nlp.ie.crf.*;
import edu.stanford.nlp.io.IOUtils;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.util.Triple;


import java.io.File;
import java.io.FileWriter;
import java.util.List;
import org.json.simple.JSONArray;

/**
 *
 * @author Sneh
 */
public class CoreNLP {
    
    public static int counter = 0;
    public static long jsonCount = 0;
    public static FileWriter jsonFile;
    public static File file;
    public static JSONArray jsonArray = new JSONArray();
    public static String serializedClassifier;
    public static AbstractSequenceClassifier<CoreLabel> classifier;
   
    public static void main(String args[]){
        try{
        String doc="C:\\Users\\Snehal\\Documents\\TREC-Data\\Data\\1\\";
         serializedClassifier = "classifiers/english.muc.7class.distsim.crf.ser.gz";
         classifier = CRFClassifier.getClassifier(serializedClassifier);
            //USAGE   tikaCoreNLP(doc);
             dir(doc,args);
       
                        if(jsonFile!=null)
                           {
                               jsonFile.write("{\"NER_CoreNLP\":");
                               jsonFile.write(jsonArray.toJSONString());
                               jsonFile.write("}");
                           // System.out.println(jsonArray.toJSONString());
                           jsonFile.close();
                           }  
                       
        
        }
        catch(Exception e){
            System.out.println("Error"+e.toString());
            e.printStackTrace();
        }
    }   
 
 
 public static void StanfordCoreNLP(String doc,String args[]){
     try{
       String text ;
   AutoDetectParser parser = new AutoDetectParser();
   BodyContentHandler handler = new BodyContentHandler();
   Metadata metadata = new Metadata();  
     
    if (args.length > 0) {
      serializedClassifier = args[0];
    }

      if (args.length > 1) {
    String fileContents = IOUtils.slurpFile(args[1]);
      List<List<CoreLabel>> out = classifier.classify(fileContents);
      for (List<CoreLabel> sentence : out) {
        for (CoreLabel word : sentence) {
              System.out.print(word.word() + '/' + word.get(CoreAnnotations.AnswerAnnotation.class) + ' ');
        }
        System.out.println();
      }

      out = classifier.classifyFile(args[1]);
      for (List<CoreLabel> sentence : out) {
        for (CoreLabel word : sentence) {
          System.out.print(word.word() + '/' + word.get(CoreAnnotations.AnswerAnnotation.class) + ' ');
        }
        System.out.println();
      }

      
    } else {

    InputStream stream = new FileInputStream(doc);
    //ParsingExample.class.getResourceAsStream(doc) ;
    //   System.out.println(stream.toString());
        parser.parse(stream, handler, metadata);
       // return handler.toString();
      text=handler.toString();
     String metaValue=metadata.toString();
    // System.out.println("Desc:: "+metadata.get("description"));
    
      String[] example = new String[1];
           example[0]=   text;
           String name=doc.replace("C:\\Users\\Snehal\\Documents\\TREC-Data\\Data","polar.usc.edu").replace("\\",".");
           List<Triple<String, Integer, Integer>> list = classifier.classifyToCharacterOffsets(text);
            JSONObject jsonObj = new JSONObject();
             jsonObj.put("DOI",name);
             jsonObj.put("metadata",metaValue.replaceAll("\\s\\s+|\n|\t"," "));             
             JSONArray tempArray = new JSONArray();
             JSONObject tempObj = new JSONObject();
      for (Triple<String, Integer, Integer> item : list) {
//          String jsonOut="{ DOI:"+name+"  ,"
//                + ""+item.first() + "\": \"" + text.substring(item.second(), item.third()).replaceAll("\\s\\s+|\n|\t"," ")+"\""
//                + "\"metadata\":\""+metaValue+"\""
//                + "}";
       // System.out.println(jsonOut);
            tempObj.put(item.first(),text.substring(item.second(), item.third()).replaceAll("\\s\\s+|\n|\t"," "));
           }
             tempArray.add(tempObj);
             jsonObj.put("NER",tempArray);
            jsonArray.add(jsonObj);
        }
     // System.out.println("---");
      
 }
catch(Exception e){
System.out.println("ERROR : CoreNLP"+"|File Name"+doc.replaceAll("C:\\Users\\Snehal\\Documents\\TREC-Data","")+" direct"+e.toString());
}
 }
 
 

   
    public static void dir(String path,String[] args) {
        try {

            File root = new File(path);
            if (root.isFile()) {

                if (counter >= 1000 || file == null) {
                    counter = 0;
                    jsonCount++;
                    file = new File("C:\\Users\\Snehal\\Documents\\tikaSimilarityTestSet\\CoreNLP\\NER_" + jsonCount + ".json");
                         if(jsonFile!=null)
                           {
                               jsonFile.write("{\"NER_CoreNLP\":");
                               jsonFile.write(jsonArray.toJSONString());
                               jsonFile.write("}");
                            //System.out.println(jsonArray.toJSONString());
                           jsonFile.close();}
                    jsonFile = new FileWriter(file);
                    jsonArray = new JSONArray();
                }

                if (!root.getName().equals((".DS_Store"))) {
                    StanfordCoreNLP(root.getAbsolutePath(),args);
                             counter++;
                   }
            } else {
                File[] list = root.listFiles();
                if (list == null) {
                    return;
                }
                for (File f : list) {
                    if (f.isDirectory()) {
                        dir(f.getAbsolutePath(),args);
                        // System.out.println( "Dir:" + f.getAbsoluteFile() );
                    } else {
                        if (counter >= 1000||file==null) {
                            counter = 0;
                            jsonCount++;
                            file = new File("C:\\Users\\Snehal\\Documents\\tikaSimilarityTestSet\\CoreNLP\\NER_" + jsonCount + ".json");
                          // System.out.print("check"+jsonArray.toJSONString());
                            if(jsonFile!=null)
                           {
                               jsonFile.write("{\"NER_CoreNLP\":");
                               jsonFile.write(jsonArray.toJSONString());
                               jsonFile.write("}");
                            //System.out.println(jsonArray.toJSONString());
                           jsonFile.close();
                           }                           
                            jsonFile = new FileWriter(file);
                            jsonArray = new JSONArray();
                        }

                        if (!f.getName().equals((".DS_Store"))) {
                             StanfordCoreNLP(f.getAbsolutePath(),args);
                             counter++;
                                    // add json   
                        }
                    }
                }
            }
        } catch (Exception e) {
            e.toString();

        }
    }

    public static String parseExample(String doc)  {
     try{
    AutoDetectParser parser = new AutoDetectParser();
    BodyContentHandler handler = new BodyContentHandler();
    Metadata metadata = new Metadata();
    
    InputStream stream = new FileInputStream(doc);
//ParsingExample.class.getResourceAsStream(doc) ;
 //   System.out.println(stream.toString());
        parser.parse(stream, handler, metadata);
        return handler.toString();
    
     }catch(Exception e){
      return "ERROR - "+e.toString();
     }
    
}
 
 public static Map<String, Set<String>> tikaCoreNLP(String doc){
        CoreNLPNERecogniser ner = new CoreNLPNERecogniser("C:\\Users\\Snehal\\Documents\\NetBeansProjects\\TIKANERSweet\\classifiers\\english.muc.7class.distsim.crf.ser.gz");
       // System.out.println(ner.getEntityTypes()+" \n "+new CoreNLPNERecogniser(CoreNLPNERecogniser.NER_7CLASS_MODEL).isAvailable());
       // Set<String> types = new CoreNLPNERecogniser("C:\\Users\\Snehal\\Documents\\NetBeansProjects\\TIKANERSweet\\classifiers\\english.muc.7class.distsim.crf.ser.gz").getEntityTypes();
         //String text = parseExample(doc) ;
        //System.out.println(text);
        Map<String, Set<String>> names = ner.recognise(doc);
    return names;
 }

}
