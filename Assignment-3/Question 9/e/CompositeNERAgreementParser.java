/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package edu.usc.polar;

import edu.stanford.nlp.ie.AbstractSequenceClassifier;
import edu.stanford.nlp.ling.CoreLabel;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileWriter;
import java.io.InputStream;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import org.apache.tika.metadata.Metadata;
import org.apache.tika.parser.AutoDetectParser;
import org.apache.tika.parser.ner.corenlp.CoreNLPNERecogniser;
import org.apache.tika.parser.ner.nltk.NLTKNERecogniser;
import org.apache.tika.sax.BodyContentHandler;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

/**
 *
 * @author Sneh
 * 
 * 
 * Output json structure
 * {"CompositeNER":
 *  [
 *  {
 *   "DOI":"some path",
 *   "NLTK":"ABC,PQRS",
 *   "OpenNLP":"ABC",
 *   "CoreNLP":"ABC,DEF,EFG,RTD" 
 *  }
 *  ]
 * }
 */

public class CompositeNERAgreementParser {
    public static int counter = 0;
    public static long jsonCount = 0;
    public static FileWriter jsonFile;
    public static File file;
    public static JSONArray jsonArray = new JSONArray();
    public static JSONArray jsonAgree = new JSONArray();
    public static NLTKNERecogniser nltkNer ;
    public static OpenNLPNERRecogniser openNer ;
    public static CoreNLPNERecogniser coreNer;
    public static String serializedClassifier;
    public static AbstractSequenceClassifier<CoreLabel> classifier;
    public static void main(String args[]){
       try{
        String doc="C:\\Users\\Snehal\\Documents\\TREC-Data\\Data\\";
        nltkNer= new NLTKNERecogniser();
        coreNer =  new CoreNLPNERecogniser("C:\\Users\\Snehal\\Documents\\NetBeansProjects\\TIKANERSweet\\classifiers\\english.muc.7class.distsim.crf.ser.gz");
        openNer= openNer.instanceOpenNLPNERRecogniser("C:\\Users\\Snehal\\Documents\\NetBeansProjects\\TIKANERSweet\\model");
       
        System.out.println(" NLTK-Rest : "+nltkNer.getEntityTypes()+" \t "+nltkNer.isAvailable());
        System.out.println(" OpenNLP : "+openNer.getEntityTypes()+" \t "+openNer.isAvailable());
        System.out.println(" StanfordNLP : "+coreNer.getEntityTypes()+" \t "+coreNer.isAvailable());
            dir(doc,args);         
                      if(jsonFile!=null)
                           {
                               jsonFile.write("{\"CompositeNER\":");
                               jsonFile.write(jsonArray.toJSONString());
                               jsonFile.write("}");
                           // System.out.println(jsonArray.toJSONString());
                           jsonFile.close();
                           } 
                      file = new File("C:\\Users\\Snehal\\Documents\\tikaSimilarityTestSet\\CompositeNER\\JointAgreement_" + jsonCount + ".json");
                      jsonFile = new FileWriter(file);
                      if(jsonFile!=null)
                           {
                               jsonFile.write("{\"JointAgreement\":");
                               jsonFile.write(jsonAgree.toJSONString());
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
    
    public boolean updateMetadata(){
    boolean status=false;
    return status;
    }
    
    public static Map<String, Set<String>> getOpenNLP(String text){
    Map<String, Set<String>> entity=openNer.recognise(text);;
    return entity;
    }
    
    public static Map<String, Set<String>> getCoreNLP(String text){
     //   CoreNLP coreNer= new CoreNLP();
   Map<String, Set<String>> entity=coreNer.recognise(text);
   //System.out.println("getCoreNLP:"+entity);
    return entity;
    }
    
     public static Map<String, Set<String>> getNLTKRest(String text){       
    // NLTKRest.tikaNLTKRest(text);
         Map<String, Set<String>> entity=nltkNer.recognise(text);
   //System.out.println("getCoreNLP:"+entity);
    return entity;
   
    }
    

public static void dir(String path,String[] args) {
        try {

            File root = new File(path);
            if (root.isFile()) {

                if (counter >= 1000 || file == null) {
                    counter = 0;
                    jsonCount++;
                    file = new File("C:\\Users\\Snehal\\Documents\\tikaSimilarityTestSet\\CompositeNER\\CompositeNER_" + jsonCount + ".json");
                         if(jsonFile!=null)
                           {
                               jsonFile.write("{\"CompositeNER\":");
                               jsonFile.write(jsonArray.toJSONString());
                               jsonFile.write("}");
                            //System.out.println(jsonArray.toJSONString());
                           jsonFile.close();}
                    jsonFile = new FileWriter(file);
                    jsonArray = new JSONArray();
                }

                if (!root.getName().equals((".DS_Store"))) {
                    CompositeNER(root.getAbsolutePath(),args);
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
                        System.out.println( "Dir:" + f.getAbsoluteFile() );
                    } else {
                        if (counter >= 1000||file==null) {
                            counter = 0;
                            jsonCount++;
                            file = new File("C:\\Users\\Snehal\\Documents\\tikaSimilarityTestSet\\CompositeNER\\CompositeNER_" + jsonCount + ".json");
                          // System.out.print("check"+jsonArray.toJSONString());
                            if(jsonFile!=null)
                           {
                               jsonFile.write("{\"CompositeNER\":");
                               jsonFile.write(jsonArray.toJSONString());
                               jsonFile.write("}");
                            //System.out.println(jsonArray.toJSONString());
                           jsonFile.close();
                           }                           
                            jsonFile = new FileWriter(file);
                            jsonArray = new JSONArray();
                        }

                        if (!f.getName().equals((".DS_Store"))) {
                             CompositeNER(f.getAbsolutePath(),args);
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

public static void CompositeNER(String doc,String args[]){
     try{
       String text ;
   AutoDetectParser parser = new AutoDetectParser();
   BodyContentHandler handler = new BodyContentHandler();
   Metadata metadata = new Metadata();  
   
    InputStream stream = new FileInputStream(doc);
    
    //   System.out.println(stream.toString());
        parser.parse(stream, handler, metadata);
       // return handler.toString();
      text=handler.toString();
     String metaValue=metadata.toString();
     System.out.println(metaValue+"Desc:: "+metadata.get("description"));
    
           String[] example = new String[1];
           example[0]=   text;
           String name=doc.replace("C:\\Users\\Snehal\\Documents\\TREC-Data\\Data","polar.usc.edu");
           name=name.replace("\\",".");
          Map<String, Set<String>> list  = getCoreNLP(text);
          Map<String, Set<String>> list1 = getOpenNLP(text);
          Map<String, Set<String>> list2 = getNLTKRest(text);
          
          Set<String> NLTKRestSet=combineSets(list2);
          Set<String> coreNLPSet=combineSets(list);
          Set<String> openNLPSet=combineSets(list1);
          
         /* 
          System.out.println("list coreNLP"+JSONStringify(coreNLPSet).toJSONString());
          System.out.println("list openNLPSet"+openNLPSet);
          System.out.println("list NLTKRestSet"+NLTKRestSet);          
          */
          JSONObject jsonObj = new JSONObject();
             jsonObj.put("DOI",name);
             jsonObj.put("OpenNLP",JSONStringify(openNLPSet));
             jsonObj.put("NLTKRest",JSONStringify(NLTKRestSet));
             jsonObj.put("CoreNLP",JSONStringify(coreNLPSet));
            
          Set<String> union=new HashSet();
          union.addAll(NLTKRestSet);
          union.addAll(coreNLPSet);
          union.addAll(openNLPSet);
           
             jsonObj.put("Union",JSONStringify(union));
          Set<String> intersection=new HashSet();
          intersection.addAll(union);
          intersection.retainAll(coreNLPSet);
          intersection.retainAll(openNLPSet);
          intersection.retainAll(NLTKRestSet);
            jsonObj.put("Agreement",JSONStringify(intersection));
          /*
          System.out.println(name+"\n"+openNLPSet.size()+openNLPSet.toString()+
                  "\n"+coreNLPSet.size()+coreNLPSet.toString()+
                  "\n"+NLTKRestSet.size()+NLTKRestSet.toArray()+
                  "\n"+intersection.size()+intersection.toArray()+
                  "\n"+union.size()+union.toArray());
          */
          
             //jsonObj.put("metadata",metaValue.replaceAll("\\s\\s+|\n|\t"," "));             
            
                
            jsonArray.add(jsonObj);
            if(intersection.size()>0)
            {   jsonAgree.add(jsonObj);
                JSONArray jArr= new JSONArray();
                jArr.add(jsonObj);
                metadata.add("CompositeNER", jArr.toJSONString());
            }

      
 }
catch(Exception e){
System.out.println("ERROR : OpenNLP"+"|File Name"+doc.replaceAll("C:\\Users\\Snehal\\Documents\\TREC-Data","")+" direct"+e.toString());
}
 }
 
 
public static Set<String> combineSets(Map<String, Set<String>> list){
Set<String> a=new HashSet<>();
for (Map.Entry<String, Set<String>> entry : list.entrySet())
{
    a.addAll(entry.getValue());
  //  System.out.println(entry.getValue()+" -- "+a);
}
//System.out.println(" -- "+a);
return a;
}

public static JSONArray JSONStringify(Set<String> set){
JSONArray  tempArr= new JSONArray();    
for(String s : set)
{
tempArr.add(s);
}
return tempArr;
}


}
