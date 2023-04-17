import socket
import subprocess
import os


def get_network_ip():
    ip = socket.gethostbyname(socket.gethostname())
    return '.'.join(ip.split('.'))


def use_network_ip():
    # Get the IP address of the local machine's network
    ip = socket.gethostbyname(socket.gethostname())
    return '.'.join(ip.split('.')[:-1])

def check_ip(ip):
    """
        Checks if the given IP address is active by pinging it.
        Returns True if the IP address is active, False otherwise.
    """
    # try:
    #     output = subprocess.check_output(["ping", "-c", "1", "-W", "1", ip])
    #     # response = os.popen(f"ping -c  {ip} ")
    #     return True

    # except subprocess.CalledProcessError:
    #     return False
    
    try:
        response = os.popen(f"ping -n 4 {ip} ").read()
        if ("unreachable") in response:
            print('IP unreachable')
            return False
        else:
            print('IP reachable')
            print(response)
            return True
        
    except subprocess.CalledProcessError:
        print('IP unreachable')
        return False


def scan_network(network):
    """
        Scans the given network for active IP addresses.
        Returns a list of active IP addresses.
    """
    active_ips = []
    for i in range(1, 10):
        ip = network + "." + str(i)
        if check_ip(ip):
            active_ips.append(ip)
    return active_ips


def check_open_ports(ip, ports):
    # Check if the specified IP address has any open ports
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((ip, port))
                open_ports.append(port)
        except:
            pass
    return open_ports


def check_closed_ports(ip, ports):
    # Check if the specified IP address has any closed ports
    closed_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((ip, port))
                if result != 0:
                    closed_ports.append(port)
        except:
            pass
    return closed_ports


if __name__ == '__main__':
    network_ip = get_network_ip()
    print("Your network IP is:", network_ip)

    net_ip = use_network_ip()
    active_ips = scan_network(net_ip)

    print("Active IP addresses are:", active_ips)
    
    # Define a list of ports to scan
    port_list = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 587, 993, 995, 1723, 3306, 3389, 5900, 8080]
    
    # Loop through all active IP addresses and check for open and closed ports
    for ip in active_ips:
        open_ports = check_open_ports(ip, port_list)
        closed_ports = check_closed_ports(ip, port_list)
        if open_ports:
            print(f"IP address {ip} has the following open ports: {open_ports}")
        if closed_ports:
            print(f"IP address {ip} has the following closed ports: {closed_ports}")
        else:
            print(f"IP address {ip} has no open or closed ports")