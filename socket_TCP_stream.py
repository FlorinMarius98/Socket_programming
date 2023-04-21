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