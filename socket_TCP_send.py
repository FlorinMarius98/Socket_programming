#Socket client example in python

import socket	#for sockets
import sys

#create an AF_INET, STREAM socket (TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print ('Socket Created')

host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname(host)

except socket.gaierror:
	#could not resolve
    print ('Hostname could not be resolved. Exiting')
    sys.exit()

print ('IP of ' + host + ' is: ' + remote_ip)

#connect to remote host

s.connect((remote_ip , port))

print('Socket connected to ' + host + ' on ip ' + remote_ip + ' using port ' + str(port))

message = "GET / HTTP/1.1\r\n\r\n"

try:
    #it will send the message to the host
    s.sendall(bytes(message, "utf8"))
except socket.error:
    #message was not sent
    print('Send failed')
    sys.exit()

print('Message sent successfully')

#Now receive data
reply = s.recv(4096)

print (reply)