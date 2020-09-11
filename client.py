import socket

print("creating a socket")
c=socket.socket()
host='192.168.0.108'
port= 9999


print("connecting to server")
c.connect((host,port))
print(f'connected to IP {host} and port {port}')

while True:
    data= c.recv(1024)
    data_new=data.decode('utf-8')
    print(data_new)
    if data_new=="quit":
        print("closing the connection")
        c.close()
        break
    else:
        send_back_msg=input("Your Message: ")
        if send_back_msg=="quit":
            print("closing the connection")
            c.close()
            break
        else:
            c.send(str.encode(send_back_msg))
