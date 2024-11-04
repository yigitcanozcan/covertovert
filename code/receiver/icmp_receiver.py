from scapy.all import IP, ICMP, sniff


def receive_packet():
    while True:
        packet = sniff(filter="icmp", count=1)[0]
        if ICMP in packet and IP in packet and packet[IP].ttl == 1:
            packet.show()
            break


receive_packet()
