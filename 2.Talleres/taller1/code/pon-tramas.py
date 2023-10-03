from scapy.all import sniff

def process_packet(packet):
    # Aquí puedes procesar cada paquete capturado
    print(packet.summary())

# Capturar paquetes de la interfaz especificada
sniff(iface="eno1", prn=process_packet)

sniff(iface="eno1", prn=process_packet, filter="ip and port 80")
