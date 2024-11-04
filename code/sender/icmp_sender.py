from scapy.all import IP, ICMP, send


# Implement your ICMP sender here
def send_packet():
    send(IP(dst="receiver", ttl=1) / ICMP())


send_packet()
