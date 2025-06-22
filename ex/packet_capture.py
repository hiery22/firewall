from scapy.all import *

def packet_callback(p):
    print(f"captured packet {p}")

sniff(prn=packet_callback)