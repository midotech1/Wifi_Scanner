from scapy.all import *
import re
import os
import time
import pyfiglet

# Monitor mode is required after running the program
def Banner():
    os.system("clear")
    os.system("figlet Wifi-Scanner")
    print("----------------------------------------------------------")
    print("                               (V1.0)")
    print("                               Github: midotech1")
    print("                               Instagram: @hackerman_xz_1")
    print("----------------------------------------------------------")
    time.sleep(0.5)
    print("")
    time.sleep(0.5)
    print("NOTICE: Please after running this program enable monitor mode !!")

Banner()

#Callback function to handle sniffed packets
def packet_callback(packet):
    # Check if the packet is a Beacon frame
    if packet.haslayer(Dot11Beacon):
        ssid = packet.info.decode()  # Get SSID (Network Name)
        bssid = packet.addr2  # Get BSSID (MAC address of AP)
        signal_strength = packet.dBm_AntSignal  # Signal strength in dBm

        # Print the network details
        print("SSID: "+ssid)
        print("BSSID: "+bssid)
        print("Signal Strength: "+signal_strength)
        #Start sniffing on the Wi-Fi interface change wlan0 to your interface name
        print("Starting Wi-Fi scan... (press Ctrl+C to sp)")
       sniff(iface="wlan0", prn=packet_callback, store=0)
packet_callback()



