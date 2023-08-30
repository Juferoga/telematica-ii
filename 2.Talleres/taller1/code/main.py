#!/usr/bin/env python3
from scapy.all import *

def packet_callback(packet):
    print(packet.summary())

# Captura paquetes en tiempo real (puedes especificar filtros usando el argumento 'filter')
sniff(prn=packet_callback, count=10)
# # Filtro por protocolo IP
# sniff(filter="ip", prn=packet_callback, count=10)
# # Filtro por puerto TCP específico
# sniff(filter="tcp and port 80", prn=packet_callback, count=10)
# # Filtro por dirección IP específica
# sniff(filter="host 192.168.1.1", prn=packet_callback, count=10)
# # Filtro por protocolo UDP en un rango de puertos
# sniff(filter="udp and portrange 1000-2000", prn=packet_callback, count=10)
# # Filtro por dirección MAC específica
# sniff(filter="ether src 00:11:22:33:44:55", prn=packet_callback, count=10)
# # Filtro por puerto TCP y host específico
# sniff(filter="tcp and port 80 and host 192.168.1.1", prn=packet_callback, count=10)
