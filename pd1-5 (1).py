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

processed_servers = []

for entry in nodes:
    parts = entry.split(';')
    
    server_name = parts[0]
    
    server_name = server_name.lower()
    
    server_name = server_name.replace('-', '_')
    
    server_name = server_name + ".local"
    
    processed_servers.append(server_name)

print("Processed server names:")
for server in processed_servers:
    print(server)
