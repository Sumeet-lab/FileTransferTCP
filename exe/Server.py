import os
import socket
import time
import easygui
from colorama import init
from termcolor import colored
init()

SIZE1 = 192512
FORMAT = "utf-8"
filename = ""
def serverFunction(IP="127.0.0.1",PORT=9999):

    ADDR = (IP, PORT)
    print(colored("[STARTING] Server is starting.","yellow"))
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(ADDR)
        server.listen(100)

        print(colored("[SERVER] Please pick a file using file picker that is Popped.","yellow"))
        path = easygui.fileopenbox()
        filename = os.path.basename(path)

        choice = input(colored("[SERVER] Would you like to send installation command? (y/n): ","cyan")).lower()
        if (choice != "y" and choice != "n"):
            print(colored("[SERVER] invalid choice, Skipping installation","red"))

        while True:
            print(colored(f"\n[LISTENING] Server is listening at ","green"),end="")
            print(colored(f"{IP} : {PORT}","cyan"))
            print(colored(f"[SERVER] Server is configured to send \"{filename}\" file\n","green"))

            conn, addr = server.accept()
            print(colored(f"[NEW CONNECTION] {addr} connected.","green"))

            file = open(path, "rb")

            data = file.read()
            SIZE = len(data)
            print(colored(f"[SERVER] File size (in bits) {len(data)}", "magenta"))
            """ Sending the filename to the server. """
            conn.send(f"{SIZE}".encode(FORMAT))
            conn.send(filename.encode(FORMAT))
            msg = conn.recv(SIZE).decode(FORMAT)
            print(colored(f"\n[CLIENT]: {msg}","yellow"))

            """ Sending the file data to the server. """
            conn.send(data)
            msg = conn.recv(SIZE).decode(FORMAT)
            print(colored(f"\n[CLIENT]: {msg}","yellow"))
            file.close()
            conn.send(f"{choice}".encode(FORMAT))
            if choice=="y":
                time.sleep(0.5)
                conn.send(f"{filename} /S /qn".encode(FORMAT))
                print(colored("[SERVER] Sent installation command","green"))


            conn.close()
            print(colored(f"\n[DISCONNECTED] {addr} disconnected.","yellow"))
    except Exception as e:
        print(e)
    finally:
        server.close()


if __name__=="__Server__":
    serverFunction()