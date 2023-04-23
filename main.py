import streamlit as st
from host_scan import *
from lan_scan import *

if __name__ == "__main__" :
    st.title("Security Operations Center - Port Scanner Application")

    st.markdown( """ 
    # Local Host Scanning 
    ## Features
    - Displays the IP address for the machine
    - Allows the users to see _Open & Closed Ports_ on their Machine
    - Uses a Thread from a Pool of Threads to ensure Multiprocesseing
    """, True)

    ip_dictionary = get_ip()
    local_ports = ports_open()

    st.table(ip_dictionary)
    st.table(local_ports)

    st.markdown( """ 
    # Network Scanning 
    ## Features
    - Finds the IP Addresses of all the machines that are connected to the Network
    - Finds the _Open and Closed_ ports of the Machines connected to the LAN
    """, True)

    lan_ports = open_closed_ports()

    st.table(lan_ports)