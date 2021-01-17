from scapy.all import *

file = open("interface.txt", "r")

interface = str(file.read())
print("\n")
print("        [CTRL] + [C] for stop the program while it's running!")

sniff(iface=interface, prn=lambda x:x.show())
