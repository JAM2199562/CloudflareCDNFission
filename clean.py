import ipaddress

def load_ip_ranges(file_path):
    with open(file_path, 'r') as file:
        ip_ranges = [ipaddress.ip_network(line.strip()) for line in file]
    return ip_ranges

def load_ip_addresses(file_path):
    with open(file_path, 'r') as file:
        ip_addresses = [ipaddress.ip_address(line.strip()) for line in file]
    return ip_addresses

def filter_ips(ip_ranges, ip_addresses):
    filtered_ips = [ip for ip in ip_addresses if any(ip in ip_range for ip_range in ip_ranges)]
    return filtered_ips

def save_filtered_ips(file_path, filtered_ips):
    with open(file_path, 'w') as file:
        for ip in filtered_ips:
            file.write(str(ip) + '\n')

def main():
    ip_ranges = load_ip_ranges('ip_range.txt')
    ip_addresses = load_ip_addresses('Fission_ip.txt')
    filtered_ips = filter_ips(ip_ranges, ip_addresses)
    save_filtered_ips('Fission_ip_new.txt', filtered_ips)

if __name__ == '__main__':
    main()
