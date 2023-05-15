import socket

SIZE1 = 192512
FORMAT = "utf-8"

def clientFunction(IP="127.0.0.1",PORT=9999):
    ADDR = (IP, PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(ADDR)


        """ Receiving the filename from the server. """
        SIZE = int(client.recv(SIZE1).decode(FORMAT))
        print("[CLIENT] File size (in bits) ", SIZE)

        filename = client.recv(SIZE).decode(FORMAT)
        print(f"\n[CLIENT] Receiving the filename.")

        file = open(filename, "wb")
        client.send("Filename received.".encode(FORMAT))

        """ Receiving the file data from the server. """

        data = client.recv(SIZE)
        print(f"\n[CLIENT] Receiving the file data.")
        file.write(data)
        client.send("File data received".encode(FORMAT))
        print("\n[CLIENT] File received")


        file.close()
        client.close()
        print(f"\n[DISCONNECTED] {ADDR} disconnected.")
    except Exception as e:
        print(e)
    finally:
        client.close()


if __name__=="__Client__":
    clientFunction()