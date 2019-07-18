# pip install pyfiglet
import pyfiglet
import socket

ascii_banner = pyfiglet.figlet_format("I Find Ip")
print ("Dr.Fr0sKa")
print(ascii_banner)

if __name__=='__main__':
    hostname = raw_input ("Enter The Target :")
    addr = socket.gethostbyname(hostname)
print("The Ip {} address is  {}   ".format(hostname,addr))
