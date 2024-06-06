import socket
import ipaddress

class NetworkScanner:
    def __init__(self, network):
        self.network = ipaddress.ip_network(network, strict=False)
        self.active_hosts = []

    def scan(self):
        for ip in self.network.hosts():
            if self.is_host_up(ip):
                self.active_hosts.append(str(ip))
        return self.active_hosts

    def is_host_up(self, ip):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((str(ip), 80))
        except (socket.timeout, socket.error):
            return False
        else:
            sock.close()
            return True

if __name__ == "__main__":
    network = input("Enter the network to scan (e.g., 192.168.1.0/24): ")
    scanner = NetworkScanner(network)
    active_hosts = scanner.scan()
    print("Active hosts:")
    for host in active_hosts:
        print(host)
