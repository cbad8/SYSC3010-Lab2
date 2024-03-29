# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time

host = sys.argv[1]
textport = sys.argv[2]
n = sys.argv[3]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)

count = 1
intn = int(n)

while count <= intn:
    print ("Enter your message (" + str(count) + ")")
    data = sys.stdin.readline().strip()
    if not len(data):
        break
#    s.sendall(data.encode('utf-8'))
    s.sendto(data.encode('utf-8'), server_address)
    count = count + 1
    
    buf, address = s.recvfrom(port)
    if not len(buf):
        break
    print ("ACK: %s" % (buf))
    
s.shutdown(1)

