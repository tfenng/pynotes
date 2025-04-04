import socket
import sys
from netaddr import iter_iprange

def scan_ip_range(start_ip, end_ip, ports):
    for ip in iter_iprange(start_ip, end_ip, step=1):
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            #print('Scan {}:{}'.format(ip.ipv4(),port))
            result = sock.connect_ex((str(ip), port))
            if result == 0:
                print(f"\tPort {port} is open on {ip}")
            sock.close()

if __name__ == '__main__':
    # 定义要扫描的 IP 地址范围和端口
    start_ip = "192.168.2.1"
    end_ip = "192.168.2.20"
    ports = [22, 23, 25, 80, 443]

    if len(sys.argv)>2:
        start_ip = sys.argv[1]
        end_ip = sys.argv[2]
    
    # 执行扫描
    scan_ip_range(start_ip, end_ip, ports)