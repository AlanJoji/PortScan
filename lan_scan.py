import os
import socket
import subprocess
import ping3

def get_network_ip():
    '''
        Input: None 
        Action: Finds IP address of the host machine's network (NOT that of the host machine itself)
        Output: IP address of the host machine's network, as a string
    '''
    ip = socket.gethostbyname(socket.gethostname())
    return '.'.join(ip.split('.'))



def use_network_ip():
    '''
        Input: None 
        Action: Finds network part of IP address (/24) of the host machine's network (NOT that of the host machine itself)
        Output: Network part of IP address (/24) of the host machine's network, as a string
    '''
    ip = socket.gethostbyname(socket.gethostname())
    return '.'.join(ip.split('.')[:-1])



def check_active_ip(ip):
    '''
        Input: IP address (of a machine), as a string 
        Action: Pings the IP address to check if it is active
        Output: True if the IP address is active, False otherwise
    '''

    """ 
    Error - Not OS Independent
    try:
        response = os.popen(f"ping -n 4 {ip} ").read()
        if ("unreachable") in response:
            return False
        else:
            return True
        
    except subprocess.CalledProcessError:
        return False
    """

    response = ping3.ping(ip, timeout=1)
    if response is not None:
        return True
    else:
        return False



def scan_network(network):
    '''
        Input: Network part of IP address (/24), as a string
        Action: Finds all active IP addresses (in a specified range) in the network
        Output: List of active IP addresses in the network
    '''
    active_ips = []

    for i in range(1, 9):
        ip = network["Network Part of IP (/24)"] + "." + str(i)
        if check_active_ip(ip):
            active_ips.append(ip)

    return active_ips



def check_open_ports(ip, ports):
    '''
        Input: IP address as a string, List of important ports to scan
        Action: Finds all open ports in that port list, for that particular IP address
        Output: List of open ports, for that particular IP address
    '''
    open_ports = []

    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.1)

                s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                syn_result = s.connect_ex((ip, port))
                if syn_result == 0:
                    open_ports.append(port)
                    continue

        except:
            pass

    return open_ports


def check_closed_ports(ports, openports):
    '''
        Input: List of important ports to scan, Dictionary of open ports
        Action: Finds all closed ports in that port list, for that particular IP address
        Output: List of closed ports, for that particular IP address
    '''

    closed_ports = []

    for port in ports:
        if port not in openports["Open Ports"]:
            closed_ports.append(port)

    return closed_ports


network_ip = {"Network IP Address": get_network_ip()}

net_ip = {"Network Part of IP (/24)": use_network_ip()}

active_ips = {"Active IP Addresses": scan_network(net_ip)}
    
port_list = [21, 22, 23, 25, 53, 80, 110, 119, 123, 143, 161, 194, 443, 445, 587, 993, 995, 1723, 3306, 3389, 5900, 8080]
    
for ip in active_ips["Active IP Addresses"]:
    open_ports = {"Open Ports": check_open_ports(ip, port_list)}
    closed_ports = {"Closed Ports": check_closed_ports(port_list, open_ports)}
