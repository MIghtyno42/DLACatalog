import csv


majorlist = ["ASEN","AREN","APPM","CHEN","CBEN","CSEN","CVEN","EEEN","ECEN","EPEN", "EVEN", "MCEN","TMEN", "GEEN"]
realNames = ["Aerospace Engineering Sciences", "Architectural Engineering", "Applied Mathematics", "Chemical Engineering","Chemical and Biological Engineering", "Computer Science", "Civil Engineering", "Electrical Engineering", "Electrical & Computer Engineering", "Engineering Physics", "Environmental Engineering", "Mechanical Engineering","Technology, Arts and Media", "Engineering Plus"]
columnNumbers = [51, 53, 52, 54, 55, 57, 56, 58, 59, 60, 62, 63, 64, 61]

position = 0
for major in majorlist:	
	with open("NEW PROJECT LISTINGS 2017.04.25.csv","r") as input_File:
		next(input_File)
		next(input_File)
		fileString = "DLA_Proj/" + major + "File.html"
		with open (fileString,"w") as output_File:
			output_File.write("<!DOCTYPE html>\n") 
			output_File.write("<html lang=\"en\">\n") 
			output_File.write("\t<head>\n") 
			output_File.write("\t\t<meta http-equiv=\Content-Type\" content=\"text/html; charset=utf-8\">\n") 
			
			
			output_File.write("\t\t<title>CU Boulder DLAs for " + major + " </title>\n") 
			output_File.write("\t<head>\n") 
			output_File.write("\t<body>\n") 
			
			fullNameString = realNames[position]
			output_File.write("\t\t<h1 align = \"left\">" + fullNameString + " Projects</h1>\n") 
			output_File.write("\t\t<hr style = \"height:4px;border:none;background-color:#333;\">\n") 
			output_File.write("\t\t<br>\n") 
			
			
		
			readcsv = csv.reader(input_File)
			listcsv = list(readcsv)
			
			for entry in listcsv:
				
				if (entry[columnNumbers[position]] != "" and entry[48] != ""):
					output_File.write("\t\t\t<div id=\"wrapper\" style = \"width:100%;overflow:auto\">\n") 
					titleString = "\t\t\t\t<h2 align = \"left\">"+ str(entry[47])+ "</h2>"
					output_File.write(titleString+"\n") 
					output_File.write("\t\t\t\t<div style = \"width:20%; float:left;word-wrap:break-word\">\n")
					output_File.write("\t\t\t\t\t<h4 align = \"left\">Contact Info</h4>\n")
					output_File.write("\t\t\t\t\t<p>\n")

					output_File.write("\t\t\t\t\t\t"+str(entry[14])+"<br />\n")
					output_File.write("\t\t\t\t\t\t"+str(entry[27])+"<br />\n")
					output_File.write("\t\t\t\t\t\t"+str(entry[25])+"<br />\n")
					output_File.write("\t\t\t\t\t\t"+str(entry[26])+"\n")
						
					if (entry[33] != ""):
						fullNameStr = entry[32] + " " + entry[33]
						output_File.write("\t\t\t\t\t<p></p>\n")
						output_File.write("\t\t\t\t\t\t"+str(fullNameStr)+"<br />\n")
						output_File.write("\t\t\t\t\t\t"+str(entry[36])+"<br />\n")
						output_File.write("\t\t\t\t\t\t"+str(entry[34])+"<br />\n")
						output_File.write("\t\t\t\t\t\t"+str(entry[35])+"\n")
							
					output_File.write("\t\t\t\t\t</p>\n")
					output_File.write("\t\t\t\t</div>\n")
					output_File.write("\t\t\t\t<div style=\"width:40%; float:right;\">\n")
					output_File.write("\t\t\t\t\t<h4 align = \"left\">Description</h4>\n")
					if ("http" in entry [50] or "www" in entry[50] or "https" in entry[50] or ".com" in entry[50] or ".edu" in entry[50] or ".net" in entry[50] or ".gov" in entry[50]):
						output_File.write("\t\t\t\t\t\t<a href = \"" + str(entry[50]) + "\">"+str(entry[50])+"\n")
						output_File.write("\t\t\t\t</a>\n")
				
						
					output_File.write("\t\t\t\t\t<ul style = \"list-style-type-disc\">\n")
			
					output_File.write("\t\t\t\t\t\t<p>"+str(entry[48])+"\n")

					output_File.write("\t\t\t\t</p>\n")
															
					output_File.write("\t\t\t\t</div>\n")
					output_File.write("\t\t\t\t<div style=\"width:38%;float:left;\">\n")
					output_File.write("\t\t\t\t\t<h4 align = \"left\">Requirements</h4>\n")
					
					
					
					output_File.write("\t\t\t\t\t<p>\n")
					output_File.write("\t\t\t\t\t\t<li>"+str(entry[49])+"\n")
					output_File.write("\t\t\t\t</li>\n")
					if (entry[67] != ""):
						if (entry[68] != ""):
							output_File.write("\t\t\t\t\t\t<li>Supervision details: "+str(entry[67]) + ". " + str(entry[68])+"\n")
							output_File.write("\t\t\t\t</li>\n")
						else:
							output_File.write("\t\t\t\t\t\t<li>Supervision details: "+str(entry[67])+"\n")
							output_File.write("\t\t\t\t</li>\n")
					if (entry[69] != ""):
						if (entry[69] == "Other, specify:"):
							output_File.write("\t\t\t\t\t\t<li> Nature of work: "+str(entry[69])+"\n")
							output_File.write("\t\t\t\t</li>\n")
						else:
							if (entry[70] == ""):
								output_File.write("\t\t\t\t\t\t<li> Nature of work: "+str(entry[69])+"\n")
								output_File.write("\t\t\t\t</li>\n")
							else:
								output_File.write("\t\t\t\t\t\t<li> Nature of work: "+str(entry[69]) + ". " + str(entry[70])+"\n")
								output_File.write("\t\t\t\t</li>\n")
					
					if (entry[71] !=""):
						output_File.write("\t\t\t\t\t\t<li> Amount of prior work completed on project: "+str(entry[71])+"\n")
						output_File.write("\t\t\t\t</li>\n")

					output_File.write("\t\t\t\t\t</p>\n")
					output_File.write("\t\t\t\t</div>\n")
					output_File.write("\t\t\t</div>\n")
					output_File.write("\t\t\t<p align = \"center\"><a href = \"https://sites.google.com/a/colorado.edu/majselection/home\">Return to List of Majors</a></p>\n")
					output_File.write("\t\t\t<hr style = \"height:1px;border:none;background-color:#333;\">\n")
					
					
			output_File.write("\t</body>\n")
			output_File.write("</html>\n")
		position = position + 1
