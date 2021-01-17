'''

    It takes the lines from the text file 'input.txt', make a list with the
    interface's names and writes in the 'interface.txt' the interface choosen
    by the user

    Example of the 'input.txt':

    Ethernet adapter Ethernet:
    Ethernet adapter Npcap Loopback Adapter:

    Example of the 'interface.txt': {the user chosed second interface}

    Npcap Loopback Adapter

'''


f = open("input.txt", "r")

end_of_file = False

interface_list = []

while not end_of_file:
    line = f.readline()
    if line == '':
        end_of_file = True
    elif line.find("Local") == -1:
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
        
        
        

print("\n")
print("#####################################################")
print("\n")


print("Choose an interface:")


number = 0
for interface in interface_list:
    print("    ", number," ",  interface)
    number += 1
print("\n")
print("-------------JUST THE NUMBER--------------")

option = int(input("-> "))
while option > number -1:
    print("Entered an incorrect number!")
    option = int(input("-> "))
    
interface_chosen  = interface_list[option]

g = open("interface.txt","w")

g.write(interface_chosen)

g.close()

f.close()

f=open("input.txt", "w")
f.close()
