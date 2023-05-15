import os,sys
import socket
import time

import easygui
import keyboard

from kb import serverKeyRecorder

SIZE1 = 192512
FORMAT = "utf-8"

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
            conn.close()
            print(f"\n[DISCONNECTED] {addr} disconnected.")
    except Exception as e:
        print(e)
    finally:
        server.close()

def serverFunction(IP="127.0.0.1",PORT=9999,keyCapture=False):

    ADDR = (IP, PORT)
    print("[STARTING] Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(ADDR)
        server.listen(100)

        print("[KEYBOARD] Press \"Enter\" key to start capturing keystrokes ")
        while True:
            if (keyboard.is_pressed("Enter")):
                events = serverKeyRecorder()
                serverEventLength = sys.getsizeof(events)
                print(serverEventLength)
                break

        while True:
            print(f"\n[LISTENING] Server is listening at {IP} {PORT}")
            print(f"[SERVER] Server is configured to send keystrokes\n")

            conn, addr = server.accept()
            print(f"[NEW CONNECTION] {addr} connected.")

            # send length of events
            conn.send(f"{serverEventLength}".encode(FORMAT))
            time.sleep(0.5)
            #  send events
            conn.sendall(events)

            conn.close()
            print(f"\n[DISCONNECTED] {addr} disconnected.")
    except Exception as e:
        print(e)
    finally:
        server.close()



if __name__=="__Server__":
    serverFunction()