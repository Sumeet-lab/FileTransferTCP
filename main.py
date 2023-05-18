from Server import *
from Client import *

option = 0
while option!=3:
    try:
        option= int(input(colored("\n1. Send a File\n2. Receive a File\n3. Exit\nEnter Choice ","yellow")))
    except Exception as e:
        print(colored("[ERROR] Invalid Input","red"))

    if option ==1:
        hostname = socket.gethostname()
        print(colored(f"Hostname: {hostname}","magenta"))
        # print ip address
        ips = socket.gethostbyname_ex(hostname)
        #  multiple ips
        if (len(ips[2])>1):
            # prints all ip addresses
            optionsDict = {}
            for option,ip in enumerate(ips[2]):
                print(colored(f"{option+1}. IP Address: {ip}","green"))
                optionsDict.update({(option+1):ip})
            try:
                option = int(input(colored("\nEnter required IP Choice from above (1,2,3,...): ","yellow")))
                ip = optionsDict.get(option)
                if (ip==None):
                    print(colored("[ERROR] Invalid Input","red"))
                    exit(0)
            except Exception as e:
                print(colored("[ERROR] Invalid Input","red"))
                print(colored("[SERVER] using default ip 127.0.0.1)","cyan"))
                ip = "127.0.0.1"
        else:
            print("IP Address:",ips[2][0])
            choice = input(colored("Continue with above IP? (y/n): ","cyan")).lower().strip()
            if (choice=="n"):
                ip = input(colored("Please enter a valid IP: ","yellow"))
            else:
                ip = ips[2][0]

        # At this point IP has been taken
        port=0
        try:
            port = int(input(colored("Enter port: ","yellow")))
        except Exception as e:
            print(colored("[ERROR] Invalid Input","red"))
            print(colored("[SERVER] using default port 9999","cyan"))
            port=9999

        # At this point ip and port are taken
        serverFunction(ip,port)
    elif option==2:
        while True:
            ip = input(colored("Enter the valid server IP: ","yellow"))
            try:
                port = int(input(colored("Enter the server Port: ","yellow")))
            except Exception as e:
                print(colored("[ERROR] Invalid Input","red"))
                print(colored("[CLIENT] using default port 9999","cyan"))
                port = 9999
            conf = input(colored(f"[SOCKET] Proceed with {ip} and {port}?(y/n)","cyan")).lower().strip()
            if (conf == "y"):
                break
        clientFunction(ip,port)

    elif option==3:
        break
    else:
        print(colored("[ERROR] Invalid Input","red"))
