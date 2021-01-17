import sys

string = str(sys.path)

string = string.split(", ")

for i in range(len(string)):
	string[i].rstrip()	
	string[i].lstrip()

	
string = string[1:]

for i in range(len(string)):
	new_str = str(string[i])
	if new_str.find("Python37-32\\", 0, len(new_str)) == -1:
		file=open("install_scapy.bat", "w")
		file.write(new_str.lstrip("'").rstrip("'").replace("\\\\", "\\")+ "\Scripts\\pip.exe install scapy")
		file.close()
