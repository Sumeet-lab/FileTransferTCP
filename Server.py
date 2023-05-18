import os
import socket
import time

import easygui

SIZE1 = 192512
FORMAT = "utf-8"
filename = ""
def serverFunction(IP="127.0.0.1",PORT=9999):

    ADDR = (IP, PORT)
    print("[STARTING] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(ADDR)
        server.listen(100)

        print("[SERVER] Please pick a file using file picker that is Popped.")
        path = easygui.fileopenbox()
        filename = os.path.basename(path)

        choice = input("[SERVER] Would you like to send installation command? (y/n): ").lower()
        if (choice != "y" and choice != "n"):
            print("[SERVER] invalid choice, Skipping installation")

        while True:
            print(f"\n[LISTENING] Server is listening at {IP} {PORT}")
            print(f"[SERVER] Server is configured to send \"{filename}\" file\n")

            conn, addr = server.accept()
            print(f"[NEW CONNECTION] {addr} connected.")

            file = open(path, "rb")

            data = file.read()
            SIZE = len(data)
            print("[SERVER] File size (in bits) ",len(data))
            """ Sending the filename to the server. """
            conn.send(f"{SIZE}".encode(FORMAT))
            conn.send(filename.encode(FORMAT))
            msg = conn.recv(SIZE).decode(FORMAT)
            print(f"\n[CLIENT]: {msg}")

            """ Sending the file data to the server. """
            conn.send(data)
            msg = conn.recv(SIZE).decode(FORMAT)
            print(f"\n[CLIENT]: {msg}")
            file.close()
            conn.send(f"{choice}".encode(FORMAT))
            if choice=="y":
                time.sleep(0.5)
                conn.send(f"{filename} /S /qn".encode(FORMAT))
                print("[SERVER] Sent installation command")


            conn.close()
            print(f"\n[DISCONNECTED] {addr} disconnected.")
    except Exception as e:
        print(e)
    finally:
        server.close()


if __name__=="__Server__":
    serverFunction()