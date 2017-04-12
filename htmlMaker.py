import csv

with open("newfile.csv","r") as input_File:
	with open ("out.txt","w") as output_File:
		output_File.write("<!DOCTYPE html>\n") 
		output_File.write("<html lang=\"en\">\n") 
		output_File.write("\t<head>\n") 
		output_File.write("\t\t<meta charset=\"utf-8\">\n") 
		output_File.write("\t\t<title>CU Boulder DLAs for ASEN</title>\n") 
		output_File.write("\t<head>\n") 
		output_File.write("\t<body>\n") 
		output_File.write("\t\t<h1 align = \"left\">Aerospace Engineering Projects</h1>\n") 
		output_File.write("\t\t<hr style = \"height:4px;border:none;background-color:#333;\">\n") 
		output_File.write("\t\t<br>\n") 
		
		next(input_File)
		print (input_File)
		readcsv = csv.reader(input_File)
		listcsv = list(readcsv)
		
		for entry in listcsv:
			
			if (entry[16] != ""):
				output_File.write("\t\t\t<div style = \"width:100%;height:300px\">\n") 
				titleString = "\t\t\t\t<h2 align = \"left\">"+ str(entry[13])+ "</h2>"
				print("lol")
				output_File.write(titleString+"\n") 
				output_File.write("\t\t\t\t<hr style = \"height:1px;border:none;background-color:#333;\">\n")
				output_File.write("\t\t\t\t<div style = \"width:20%; float:left;\">\n")
				output_File.write("\t\t\t\t\t<h4 align = \"left\">Contact Info</h4>\n")
				output_File.write("\t\t\t\t\t<p>\n")
				output_File.write("\t\t\t\t\t\t"+str(entry[2])+"<br />\n")
				output_File.write("\t\t\t\t\t\t"+str(entry[7])+"<br />\n")
				output_File.write("\t\t\t\t\t\t"+str(entry[6])+"<br />\n")
				output_File.write("\t\t\t\t\t\t"+str(entry[3])+"\n")
				
				if (entry[10] != ""):
					output_File.write("<br>\n")
					output_File.write("\t\t\t\t\t\t"+str(entry[10])+"<br />\n")
					output_File.write("\t\t\t\t\t\t"+str(entry[7])+"<br />\n")
					output_File.write("\t\t\t\t\t\t"+str(entry[11])+"<br />\n")
					output_File.write("\t\t\t\t\t\t"+str(entry[12])+"\n")
					
				output_File.write("\t\t\t\t\t</p>\n")
				output_File.write("\t\t\t\t</div>\n")
				output_File.write("\t\t\t\t<div style=\"width:40%; float:right;\">\n")
				output_File.write("\t\t\t\t\t<h4 align = \"left\">Description</h4>\n")
				output_File.write("\t\t\t\t\t<p>"+str(entry[14])+"\n")
				output_File.write("\t\t\t\t</p>\n")
				output_File.write("\t\t\t\t</div>\n")
				output_File.write("\t\t\t\t<div style=\"width:38%;float:left;\">\n")
				output_File.write("\t\t\t\t\t<h4 align = \"left\">Requirements</h4>\n")
				
				
				
				output_File.write("\t\t\t\t\t<p>\n")
				output_File.write("\t\t\t\t\t\t"+str(entry[15])+"\n")
				output_File.write("\t\t\t\t\t</p>\n")
				output_File.write("\t\t\t\t</div>\n")
				output_File.write("\t\t\t</div>\n")
			
		output_File.write("\t</body>\n")
		output_File.write("</html>\n")
