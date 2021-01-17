import os
from scapy.all import *
import subprocess


def main():
    list_of_interface = []
    string= str(subprocess.check_output("ipconfig" ).decode('utf-8')).split("\r\n")
    for element in string:
        if element.find("Ethernet") != -1:
            list_of_interface.append(element)
        elif element.find("WiFi") != -1:
            list_of_interface.append(element)
    
    interface_list = []
    
    for line in list_of_interface:
        words = line.split()
        string=''
        if (words[0] == "Ethernet"):
            for iterator in range(2,len(words)):
                if (len(string) > 0):
                    string += ' '
                string += words[iterator]
        elif words[0] == "Wireless":
            for iterator in range(3,len(words)):
                if len(string) > 0:
                    string += ' '
                string += words[iterator]
        new_string = string[:len(string)-1]    
        interface_list.append(new_string)
    
    print("Choose an interface:")


    number = 0
    for interface in interface_list:
        print("    ", number," ",  interface)
        number += 1
    print("\n")
    print("-------------JUST THE NUMBER--------------")

    passed = False
    while not passed:
        try:
            option = int(input("-> "))
            passed = True
        except:
            print("Not a number!")
    while option > number -1:
        print("Entered an incorrect number!")
        passed = False
        while not passed:
            try:
                option = int(input("-> "))
                passed = True
            except:
                print("Not a number!")
                
    interface_chosen  = interface_list[option]

    print("\n")
    print("        [CTRL] + [C] for stop the program while it's running!")
    
    sniff(iface=interface_chosen, prn=lambda x:x.show())


main()
command = input("Write 'exit' to close the program or 'start' to start the program again ->")
while command == "start":
    main()
