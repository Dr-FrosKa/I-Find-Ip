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
 
s= socket.socket (socket.AF_INET, socket.SOCK_STREAM)
pr= (80,443,21,22,8080)
def pscan(pr):
	try:
		s.connect((server,pr))
		return True
	except :
		return False
for x in pr:
	if pscan(x):
		print ("Port",x,"Is Open")
	else:
		print("Port",x,"Is Closed")
	
	
	
