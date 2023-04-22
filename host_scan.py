import socket
from multiprocessing import Pool

Hostname = socket.gethostname()
IPAddr = socket.gethostbyname(Hostname)

def get_ip():
    """
        Input: None
        Action: Gets the IP address and Hostname of the machine
        Output: Dictionary with keys Hostname and IP Address
    """
    Hostname = socket.gethostname() 
    IPAddr = socket.gethostbyname(Hostname)
    return {'Hostname': Hostname, 'IP Address': IPAddr}

def scan_port(port):
    """
        Input: Port number to scan.
        Action: Scans ports
        Output: The port number if open, otherwise None.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.01)
    try:
        result = s.connect_ex((IPAddr,port))
        if result == 0:
            return port
    except:
        pass
    finally:
        s.close()
    return None

def ports_open():
    """
        Input: None
        Action: Scans ports 1-1023
        Output: Dictionary with key Open Ports and value is a list of open ports
    """
    try:
        with Pool(10) as p: 
            Open_Ports = list(filter(lambda x: x is not None, p.map(scan_port, range(1,1024))))
    except KeyboardInterrupt:
        return {"message": "Exiting Program !!"}
    
    return {'Open Ports': Open_Ports}

# if __name__ == "__main__" :
#     print(ports_open())
    