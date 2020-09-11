import socket

#creating a socket
def create_socket():
    global host
    global port
    global s

    try:
        print("creating a socket")
        s=socket.socket()
        host=""
        port=9999
        print("Socket created succesfully")

    except socket.error as msg:
        print(f"socket creation error {str(msg)}")

#binding socket and listening for connections
def bind_socket():
    try:
        print(f"Binding socket {str(port)}")
        s.bind((host,port))
        s.listen(5)
        c=input("Enter y to continue and n to stop: ")
        if c=="n":
            s.close()
            print("socket is closed and quiting the server")
            quit()

    except socket.error as msg:
        print(f"Bindind error {str(msg)}")
        print("Retrying....")
        bind_socket()

#accepting the connection
def accept_connection():
    print("connecting")
    connection,address=s.accept()
    print(f"Connected to IP {address[0]} port {str(address[1])}")
    connection.send(str.encode("Connection Established"))
    #write the function that will do actions here
    actions(connection)
    connection.close()

def actions(connection):
    while True:
        message=input("Your message: ")
        if message=="quit":
            connection.send(str.encode(message))
            #clnt_response= str(connection.recv(1024), "utf-8")
            print("Closing the connection")
            connection.close()
            s.close()
            break
        elif len(str.encode(message))>0:
            connection.send(str.encode(message))
            clnt_response=str(connection.recv(1024),"utf-8")
            print(clnt_response)
            if clnt_response=="quit":
                print("Closing the connection")
                connection.close()
                s.close()
                break

def main():
    create_socket()
    bind_socket()
    accept_connection()

main()