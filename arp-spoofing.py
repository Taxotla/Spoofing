##codigo spoofing

import os 
import time 
import signal
import sys
from datetime import datetime


arp_table = {}


def get_arp_table():
    arp_output = os.popen('arp -n').read()
    return arp_output


def parse_arp_table(arp_output):
    lines = arp_output.split('\n')
    arp_dict = {}
    
    for line in lines:
        if 'incomplete' in line or len(line) == 0 or line.startswith("Address"):
            continue
        parts = line.split()
        if len(parts) >= 4:
            ip = parts[0]
            mac = parts[2]
            arp_dict[ip] = mac
    return arp_dict


def monitor_arp_table(interval=10):
    global arp_table
    try:
        while True:
           
            arp_output = get_arp_table()
            current_arp_table = parse_arp_table(arp_output)

           
            if arp_table and arp_table != current_arp_table:
                diff = set(arp_table.items()) ^ set(current_arp_table.items())
                for ip, mac in diff:
                    log_msg = f"[{datetime.now()}] ARP Spoofing detectado: IP {ip} ahora tiene MAC {mac}\n"
                    print(log_msg)
                   
                    with open("arp_spoofing_log.txt", "a") as log_file:
                        log_file.write(log_msg)
            
            arp_table = current_arp_table
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nMonitorización ARP detenida")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        interval = int(sys.argv[1])
    else:
        interval = 10  #10sec interval value defined
    
    monitor_arp_table(interval)
