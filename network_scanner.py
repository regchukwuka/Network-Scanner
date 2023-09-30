from scapy.all import IP, ICMP, TCP, sr, sr1, conf
import sys

# Disable verbosity in scapy
conf.verb = 0

def icmp_scan(subnet):
    """Function to scan the subnet using ICMP echo request packets."""
    alive_hosts = []
    for ip in subnet:
        packet = IP(dst=str(ip))/ICMP()
        response = sr1(packet, timeout=1, verbose=0)
        if response:
            alive_hosts.append(str(ip))
    return alive_hosts

def tcp_scan(subnet, port):
    """Function to scan the subnet using TCP SYN packets."""
    alive_hosts = []
    for ip in subnet:
        packet = IP(dst=str(ip))/TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)
        if response and response.haslayer(TCP) and response[TCP].flags == "SA":
            # Received SYN-ACK, means port is open and host is up
            alive_hosts.append(str(ip))
    return alive_hosts

def network_scanner():
    # Take user input
    subnet_input = input("Enter the network address to scan (e.g. 192.168.2.0/24): ")
    mode = input("Enter the mode (ICMP or TCP): ").strip().upper()
    
    subnet = list(IP(subnet_input))
    
    if mode == "ICMP":
        alive_hosts = icmp_scan(subnet)
    elif mode == "TCP":
        port = int(input("Enter the TCP port number: "))
        alive_hosts = tcp_scan(subnet, port)
    else:
        print("Invalid mode selected.")
        return

    # Print the results
    print("\nAlive hosts:")
    for host in alive_hosts:
        print(host)



# Useage
network_scanner()
