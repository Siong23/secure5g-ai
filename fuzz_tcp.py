from scapy.all import *
import random
import string

target_ip = "192.168.114.129"
target_port = 80

def generate_payload(length=50):
	return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

for i in range(100):
	payload = generate_payload()
	pkt = IP(dst=target_ip)/TCP(dport=target_port, sport=RandShort(), flags="S")/Raw(load=payload)
	send(pkt, verbose=False)

print("Fuzzing sent.")


