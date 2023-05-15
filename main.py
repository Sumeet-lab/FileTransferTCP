from Server import *
from Client import *

option = 0
while option!=3:
    try:
        option= int(input("\n1. Send a File\n2. Receive a File\n3. Exit\nEnter Choice "))
    except Exception as e:
        print("[ERROR] Invalid Input")

    if option ==1:
        hostname = socket.gethostname()
        print("Hostname:",hostname)
        # print ip address
        ips = socket.gethostbyname_ex(hostname)
        #  multiple ips
        if (len(ips[2])>1):
            # prints all ip addresses
            optionsDict = {}
            for option,ip in enumerate(ips[2]):
                print(f"{option+1}. IP Address: {ip}")
                optionsDict.update({(option+1):ip})
            try:
                option = int(input("\nEnter required IP Choice from above (1,2,3,...): "))
                ip = optionsDict.get(option)
                if (ip==None):
                    print("[ERROR] Invalid choice")
                    exit(0)
            except Exception as e:
                print("[ERROR] Invalid Input")
                print("[SERVER] using default ip 127.0.0.1")
                ip = "127.0.0.1"
        else:
            print("IP Address:",ips[2][0])
            choice = input("Continue with above IP? (y/n): ").lower().strip()
            if (choice=="n"):
                ip = input("Please enter a valid IP: ")
            else:
                ip = ips[2][0]

        # At this point IP has been taken
        port=0
        try:
            port = int(input("Enter port: "))
        except Exception as e:
            print("[ERROR] Invalid Input")
            print("[SERVER] using default port 9999")
            port=9999

        # At this point ip and port are taken
        serverFunction(ip,port)
    elif option==2:
        while True:
            ip = input("Enter the valid server IP: ")
            try:
                port = int(input("Enter the server Port: "))
            except Exception as e:
                print("[ERROR] Invalid Input")
                print("[CLIENT] using default port 9999")
                port = 9999
            conf = input(f"[SOCKET] Proceed with {ip} and {port}?(y/n)").lower().strip()
            if (conf == "y"):
                break
        clientFunction(ip,port)

    elif option==3:
        break
    else:
        print("[ERROR] Invalid Option!!")
