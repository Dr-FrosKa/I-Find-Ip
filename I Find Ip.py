import socket
import time 
def cls(): 
    print('\n'* 20)
print ("""
\033[1;33m
  _____   ______ _           _   _____       
 |_   _| |  ____(_)         | | |_   _|      
   | |   | |__   _ _ __   __| |   | |  _ __  
   | |   |  __| | | '_ \ / _` |   | | | '_ \ 
  _| |_  | |    | | | | | (_| |  _| |_| |_) |
 |_____| |_|    |_|_| |_|\__,_| |_____| .__/ 
                                      | |    
                                      |_|    
\033[0m        \t-={ \033[1;36mBy Dr.Fr0sKa\033[0m }=-
""")
if __name__=='__main__':
    hostname = raw_input ("\033[1;33m[ # ]\033[1;32m Enter The Target :")
    addr = socket.gethostbyname(hostname)
from colorama import Fore, Back, Style
print(Fore.GREEN)
time.sleep(3)
print("\033[1;31m[ ! ]\033[1;36m The Ip  {}  Address Is || {} || >>> \033[0m".format(hostname,addr))

from colorama import Fore, Back, Style
print(Fore.WHITE)

time.sleep(3)

 
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
		print ("\033[1;32mPort",x,"\033[1;32mIs Open")
	else:
		print("\033[1;31mPort"),x,("\033[1;31mIs Closed")
	
	
	
