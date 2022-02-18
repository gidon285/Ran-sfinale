import os

def sniffing():
    if os.path.exists("save.pcap"):
        os.remove("save.pcap")
    os.system('sudo wireshark -k -Y http -w /tmp/save.pcap')

sniffing()
