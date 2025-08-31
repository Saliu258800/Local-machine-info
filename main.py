import socket

def local_machine_info():
    try:
        host = socket.gethostname() # returns the name of the local machine 
        
        ip = socket.gethostbyname(host) # returns ip address associated with the local machine and takes socket.gethostname() as an argument 
        
        print("Host name: ", host)
        print("IP Address: ", ip)
    except Exception as e:
        print(f"{e}: Unexpected error")
        
if __name__ == "__main__":
    local_machine_info()