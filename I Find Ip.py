import terminal_banner
import pyfiglet
import socket
def cls(): 
    print('\n'* 100)
cls()    
banner_text = "Dr.Fr0sKa.\n\nSnap:Faris_th7 | Instagram:4o16."
my_banner = terminal_banner.Banner(banner_text)
print(my_banner)

ascii_banner = pyfiglet.figlet_format("I Find Ip")
print(ascii_banner)

if __name__=='__main__':
    hostname = raw_input ("Enter The Target :")
    addr = socket.gethostbyname(hostname)
print("The Ip  {}  address is || {} ||  ".format(hostname,addr))
