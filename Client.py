import socket
from cmd import execute
from colorama import init
from termcolor import colored
init()

SIZE1 = 192512232
FORMAT = "utf-8"

def clientFunction(IP="127.0.0.1",PORT=9999):
    ADDR = (IP, PORT)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(ADDR)

        """ Receiving the filename from the server. """
        SIZE = int(client.recv(SIZE1).decode(FORMAT))
        print(colored(f"[SERVER] File size (in bits) {SIZE}", "magenta"))

        filename = client.recv(SIZE).decode(FORMAT)
        print(colored(f"\n[CLIENT] Receiving the filename.","yellow"))

        file = open(filename, "wb")
        client.send("Filename received.".encode(FORMAT))

        """ Receiving the file data from the server. """

        data = client.recv(SIZE)
        print(colored(f"\n[CLIENT] Receiving the file data.","yellow"))
        file.write(data)
        client.send("File data received".encode(FORMAT))
        print(colored("\n[CLIENT] File received","green"))

        file.close()
        choice = client.recv(SIZE1).decode(FORMAT)
        if choice == "y":
            print(colored("Installing the application...", "blue"))
            command = client.recv(SIZE1).decode(FORMAT)
            status = execute(command)
            if status:
                print(colored("Application Installed", "green"))
            else:
                print(colored("[INSTALLATION FAILED] Program was not installed","red"))

        client.close()
        print(colored(f"\n[DISCONNECTED] {ADDR} disconnected.","yellow"))
    except Exception as e:
        print(e)
    finally:
        client.close()


if __name__=="__Client__":
    clientFunction()