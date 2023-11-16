import pyshark
import pandas as pd

def process_ethernet_frame(packet):
    eth_data = {}
    try:
        eth_layer = packet.eth
        eth_data['Source MAC'] = eth_layer.src
        eth_data['Destination MAC'] = eth_layer.dst
    except AttributeError:
        eth_data['Source MAC'] = 'Unknown'
        eth_data['Destination MAC'] = 'Unknown'

    if hasattr(packet, 'mpls'):
        mpls_data = process_mpls(packet)
        eth_data.update(mpls_data)
    else:
        eth_data['MPLS Info'] = 'No MPLS'

    return eth_data

def process_mpls(packet):
    mpls_info = {}
    mpls_labels = []
    for mpls_layer in packet.layers:
        if mpls_layer.layer_name == 'mpls':
            mpls_labels.append({
                'Label': mpls_layer.label,
                'Exp': mpls_layer.exp,
                'TTL': mpls_layer.ttl
            })

    mpls_info['MPLS Labels'] = mpls_labels
    try:
        next_layer = packet.layers[-1]
        mpls_info['Next Layer'] = next_layer.layer_name
    except IndexError:
        mpls_info['Next Layer'] = 'Unknown'

    return mpls_info

def capture_packets(interface='wlo1', packet_count=50):
    capture = pyshark.LiveCapture(interface=interface)
    packets_data = []

    for packet in capture.sniff_continuously(packet_count=packet_count):
        packet_info = process_ethernet_frame(packet)
        packets_data.append(packet_info)

    df = pd.DataFrame(packets_data)
    df.to_csv('network_traffic_analysis.csv', index=False)
    print(df)

capture_packets()
