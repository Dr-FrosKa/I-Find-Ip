import socket
if __name__=='__main__':
    hostname = raw_input ("Enter The Target :")
    addr = socket.gethostbyname(hostname)
    print("The Ip {} address is  {}   ".format(hostname,addr))
