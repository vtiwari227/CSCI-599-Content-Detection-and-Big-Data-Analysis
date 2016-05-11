import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.LinkOption;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

import org.apache.tika.Tika;
public class parser {
	static String output="/Users/anirbanmishra/Projects/Content_Assignment/Assignment 1/Mime_Type.txt";
	public static void displayDirectoryContents(File dir) throws IOException {
		Tika tika = new Tika();
		
		try {
			File[] files = dir.listFiles();
			for (File file : files) {
				if (file.isDirectory()) {
					//System.out.println("directory:" + file.getCanonicalPath());
					displayDirectoryContents(file);
				} else {
					if(!file.getCanonicalPath().toString().contains(".DS_Store")){
					Path path=Paths.get(file.getCanonicalPath());
					try{
					String type = tika.detect(path);
					Path p = Paths.get(path.toString());
					String file_name = p.getFileName().toString();
					move(file_name,path.toString(),type);
					System.out.println(file_name+":"+type);
					}
					catch(Exception E){	
					}
					}
					
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}
public static void main(String[] args) throws Exception {
File folder = new File(args[0]);
File xx = new File(output);
displayDirectoryContents(folder);
}

public static void move(String file, String path, String mime_type) throws IOException{
    String dest="/Users/anirbanmishra/Downloads/Content";
    if(mime_type=="application/octet-stream"){
        dest=dest+"/octet";
        moveToFolder(file,path,dest,mime_type);}
    else if(mime_type.equals("application/pdf")){
        dest=dest+"/pdf";
        moveToFolder(file,path,dest,mime_type);}
    else if(mime_type.equals("text/html")){
        dest=dest+"/html";
        moveToFolder(file,path,dest,mime_type);}
    else if(mime_type.equals("text/plain")){
        dest=dest+"/plain";
        moveToFolder(file,path,dest,mime_type);}
    else if(mime_type.equals("image/png")){
        dest=dest+"/png";
        moveToFolder(file,path,dest,mime_type);}
    else if(mime_type.equals("image/gif")){
        dest=dest+"/gif";
        moveToFolder(file,path,dest,mime_type);}
    else if(mime_type.equals("image/jpeg")){
        dest=dest+"/jpeg";
        moveToFolder(file,path,dest,mime_type);}
    else if(mime_type.equals("application/xhtml+xml")){
        dest=dest+"/xhtml";
        moveToFolder(file,path,dest,mime_type);}
    else if(mime_type.equals("application/xml")){
        dest=dest+"/xml";
        moveToFolder(file,path,dest,mime_type);}
    else if(mime_type.equals("application/rss+xml")){
        dest=dest+"/rss";
        moveToFolder(file,path,dest,mime_type);}
    else if(mime_type.equals("application/x-sh")){
        dest=dest+"/sh";
        moveToFolder(file,path,dest,mime_type);}
    else if(mime_type.equals("application/atom+xml")){
        dest=dest+"/atom_xml";
        moveToFolder(file,path,dest,mime_type);}
    else if(mime_type.equals("application/gzip")){
        dest=dest+"/gzip";
        moveToFolder(file,path,dest,mime_type);}
    else if(mime_type.equals("application/zip")){
        dest=dest+"/zip";
        moveToFolder(file,path,dest,mime_type);}
    else if(mime_type.equals("application/x-tika-msoffice")){
        dest=dest+"/office";
        moveToFolder(file,path,dest,mime_type);}
    else{
    	dest=dest+"/others";
    	moveToFolder(file,path,dest,mime_type);}
    }

public static void moveToFolder(String file_name, String path, String dst, String type) throws IOException{
    String dest=dst+"/"+file_name;
    Path source=Paths.get(path);
    Path destination=Paths.get(dest);
    Path dest_path = Paths.get(dest);

    boolean pathExists =
            Files.exists(dest_path,
                new LinkOption[]{ LinkOption.NOFOLLOW_LINKS});
    if(!pathExists)
    {
    System.out.println("Hi");
    Files.copy(source, destination, StandardCopyOption.REPLACE_EXISTING);
    PrintWriter out = new PrintWriter(new BufferedWriter(new FileWriter(output, true)));
	out.println(file_name+":"+type);
	out.close();
    }
}
}