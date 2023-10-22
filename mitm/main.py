import scapy.all as scapy

def get_mac(ip):
    # Create an ARP request packet to get the MAC address of the specified IP
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    
    # Send the ARP request packet and wait for a response
    answered, _ = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)
    
    # Check if a response was received
    if answered:
        # Extract the MAC address from the response packet
        return answered[0][1].hwsrc
    else:
        return None


