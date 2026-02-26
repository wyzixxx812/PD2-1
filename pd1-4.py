nodes = [
    "Srv-web-01;192.168.1.10;15;UP",
    "Srv-db-01;192.168.1.20;450;UP",
    "Srv-Backup;10.0.0.5;0;DOWN",
    "Workstation-A;192.168.1.105;5;UP",
    "Srv-Proxy-01;172.16.0.1;10;up",
    "Srv-Mail;10.0.0.10;120;UP",
    "Router-Core;192.168.1.1;2;UP",
    "Srv-Dev-1;192.168.2.50;500;UP",
    "Printer-Main;192.168.1.200;0;UP",
    "Srv-Log;10.0.0.15;105;UP"
]

def find_servers_by_network():
    network_prefix = input("Enter a portion of the IP address (e.g., 192.168): ")
    
    print(f"\n--- Servers in network {network_prefix} ---")
    found = False

    for node in nodes:
        if network_prefix in node:
            print(node)
            found = True
            
    if not found:
        print("No servers found for this network.")
if __name__ == "__main__":
    find_servers_by_network()
