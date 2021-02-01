import socket
import json
from binascii import unhexlify

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.bind(("", 15000))
while True:
    data, addr = udp.recvfrom(4096)
    if data:
        break
udp.close()

IP = addr[0]
PORT = 10111
ADDR = (IP, PORT)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect(ADDR)
print(f"{ADDR} [SOCKET CONNECTED to {IP} on port {PORT}] Success\n========================================\n")

def send_command(cmd, params, await_response=False):
    request = {"Command":cmd,"Parameters":params}
    request = json.dumps(request).encode("utf-8")
    req_len = unhexlify(hex(len(request))[2:])
    request = req_len + b"\x00\x00\x00" + request
    print(f"{ADDR} [SENDING REQUEST to {IP} : {PORT}] {request[4:].decode('utf-8')}")
    tcp.sendall(request)
    if await_response:
        print(f"{ADDR} [AWAITING RESPONSE from {IP} : {PORT}] Request has been sent to Infinite Flight")
        response = tcp.recv(16384)[4:].decode("utf-8")
        print(f'{ADDR} [RESPONSE RECIEVED from {IP} : {PORT}]')
        return response
    else:
        print(f"{ADDR} [REQUEST SENT SUCCESSFULLY to {IP} : {PORT}] Request sent to Infinite Flight successfully")
    return None