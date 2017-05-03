import csv


majorlist = ["ASEN","AREN","APPM","CHEN","CBEN","CSEN","CVEN","EEEN","ECEN","EPEN", "EVEN", "MCEN","TMEN", "GEEN"]
realNames = ["Aerospace Engineering Sciences", "Architectural Engineering", "Applied Mathematics", "Chemical Engineering","Chemical and Biological Engineering", "Computer Science", "Civil Engineering", "Electrical Engineering", "Electrical & Computer Engineering", "Engineering Physics", "Environmental Engineering", "Mechanical Engineering","Technology, Arts and Media", "Engineering Plus"]
columnNumbers = [41, 43, 42, 44, 45, 47, 46, 48, 49, 40, 42, 43, 44, 41]
fname = "CU_SPUR_2017.csv"

position = 0
for major in majorlist:	
	with open(fname,"r") as input_File:
		next(input_File)
		next(input_File)
		fileString = "SPUR_Proj/" + major + "File.html"
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
				
				if (entry[columnNumbers[position]] != "" and entry[38] != ""):
					output_File.write("\t\t\t<div id=\"wrapper\" style = \"width:100%;overflow:auto\">\n") 
					titleString = "\t\t\t\t<h2 align = \"left\">"+ str(entry[37])+ "</h2>"
					output_File.write(titleString+"\n") 
					output_File.write("\t\t\t\t<div style = \"width:20%; float:left;word-wrap:break-word\">\n")
					output_File.write("\t\t\t\t\t<h4 align = \"left\">Contact Info</h4>\n")
					output_File.write("\t\t\t\t\t<p>\n")

					output_File.write("\t\t\t\t\t\t"+str(entry[14])+"<br />\n")
					output_File.write("\t\t\t\t\t\t"+str(entry[27])+"<br />\n")
					output_File.write("\t\t\t\t\t\t"+str(entry[25])+"<br />\n")
					output_File.write("\t\t\t\t\t\t"+str(entry[26])+"<br />\n")
					output_File.write("\t\t\t\t\t\t<br />\n")
						
					output_File.write("\t\t\t\t\t</p>\n")
					output_File.write("\t\t\t\t</div>\n")
					output_File.write("\t\t\t\t<div style=\"width:40%; float:right;\">\n")
					output_File.write("\t\t\t\t\t<h4 align = \"left\">Description</h4>\n")
					if ("http" in entry [40] or "www" in entry[40] or "https" in entry[40] or ".com" in entry[40] or ".edu" in entry[40] or ".net" in entry[40] or ".gov" in entry[40]):
						output_File.write("\t\t\t\t\t\t<a href = \"" + str(entry[40]) + "\">"+str(entry[40])+"\n")
						output_File.write("\t\t\t\t</a>\n")
				
						
					output_File.write("\t\t\t\t\t<ul style = \"list-style-type-disc\">\n")
			
					output_File.write("\t\t\t\t\t\t<p>"+str(entry[38])+"\n")

					output_File.write("\t\t\t\t</p>\n")
															
					output_File.write("\t\t\t\t</div>\n")
					output_File.write("\t\t\t\t<div style=\"width:38%;float:left;\">\n")
					output_File.write("\t\t\t\t\t<h4 align = \"left\">Requirements</h4>\n")
					
					
					
					output_File.write("\t\t\t\t\t<p>\n")
					if (entry[39] != ""):
						output_File.write("\t\t\t\t\t\t<li>"+str(entry[39])+"\n")
						output_File.write("\t\t\t\t</li>\n")
					if (entry[55] != ""):
						if (entry[56] != ""):
							output_File.write("\t\t\t\t\t\t<li>Supervision details: "+str(entry[55]) + ". " + str(entry[56])+"\n")
							output_File.write("\t\t\t\t</li>\n")
						else:
							output_File.write("\t\t\t\t\t\t<li>Supervision details: "+str(entry[55])+"\n")
							output_File.write("\t\t\t\t</li>\n")
					if (entry[57] != ""):
						if (entry[57] != "Other, specify:"):
							output_File.write("\t\t\t\t\t\t<li> Nature of work: "+str(entry[57])+"\n")
							output_File.write("\t\t\t\t</li>\n")
						else:
							if (entry[58] != ""):
								output_File.write("\t\t\t\t\t\t<li> Nature of work: "+str(entry[58])+"\n")
								output_File.write("\t\t\t\t</li>\n")
					if (entry[59] !=""):
						output_File.write("\t\t\t\t\t\t<li> Amount of prior work completed on project: "+str(entry[59])+"\n")
						output_File.write("\t\t\t\t</li>\n")

					output_File.write("\t\t\t\t\t</p>\n")
					output_File.write("\t\t\t\t</div>\n")
					output_File.write("\t\t\t</div>\n")
					output_File.write("\t\t\t<p align = \"center\"><a href = \"https://sites.google.com/a/colorado.edu/spurprojects/home\">Return to List of Majors</a></p>\n")
					output_File.write("\t\t\t<hr style = \"height:1px;border:none;background-color:#333;\">\n")
					
					
			output_File.write("\t</body>\n")
			output_File.write("</html>\n")
		position = position + 1
