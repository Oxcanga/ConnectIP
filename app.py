import socket
import colorama

colorama.init()
ip_address = input("Enter IP: ")

def connect_to_localhost(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(colorama.Fore.MAGENTA + "Please Wait...")
        sock.connect((ip_address, port))
        print(colorama.Fore.GREEN + "Connecting Successful!")
    except ConnectionRefusedError:
        print(colorama.Fore.RED + "Error! Connection Refused")
    
a = input("Do you want the connect IP Address? Y/N: ")

if a == "Y" or a == "y":
    connect_to_localhost(port=80)
elif a == "N" or a == "n":
    print("Program Stopped!")
    exit()