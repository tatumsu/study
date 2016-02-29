import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# check and turn on TCP Keepalive
x = sock.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE)
if (x == 0):
    print('Socket Keepalive off, turning on')
    x = sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    print('setsockopt='+str(x))
    # overrides value (in seconds) shown by sysctl net.ipv4.tcp_keepalive_time
    sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 30)
    # overrides value shown by sysctl net.ipv4.tcp_keepalive_probes
    sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, 6)
    # overrides value shown by sysctl net.ipv4.tcp_keepalive_intvl
    sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, 10)
else:
    print('Socket Keepalive already on')

# Connect the socket to the port where the server is listening
server_address = ('192.168.0.133', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    print('sending "%s"' % message)
    sock.sendall(str.encode(message))

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('received "%s"' % data)

    print("Sleep for 600 seconds before exit...")
    time.sleep(600)
finally:
    print('closing socket')
    sock.close()
