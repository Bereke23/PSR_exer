#!/usr/bin/env python3
# --------------------------------------------------
# Client is the active one
# The server is just going to be waiting for the client to send a message
# Adapted from https://stackabuse.com/basic-socket-programming-in-python/
# -------------------------------------------------
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create TCP/IP socket
local_hostname = socket.gethostname()  # retrieve local hostname
local_fqdn = socket.getfqdn()  # get fully qualified hostname
ip_address = socket.gethostbyname(local_hostname)  # get the according IP address

server_address = (ip_address, 23456)  # bind the socket to the port 23456, and connect
sock.connect(server_address)
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))


# define a dog to be sent
import dog_lib
dog = dog_lib.Dog('Zeus','black','9', ' Bebiana')
dog.addBrother('Rex')
dog.addBrother('Rui')
print(dog)

# Serialization 
message = dog.name
message += ','
message += dog.owner
message += ','
message += str(dog.age)
message += ','
message += dog.color

for brother in dog.brothers:
    message += ',' + brother

#send a message

while True:
   print ('Sending message: ' + str(message))
   message_formatted = message.encode('utf-8')
   sock.sendall(message_formatted)
   time.sleep(2)  # wait for two seconds 


# define example data to be sent to the server
# messages = [str(30), 'Robotics', str(31), str(14), 'Automation', str(18)]
# for message in messages:
#     print ('Sending message: ' + str(message))
#     message_formatted = message.encode('utf-8')
#     sock.sendall(message_formatted)
#     time.sleep(2)  # wait for two seconds

sock.close()  # close connection