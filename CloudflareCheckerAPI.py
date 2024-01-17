import socket
import requests
import ipaddress
def check(domain):
    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror:
        print("CloudflareChecker: Failed to Host name resolution.")
        return False
    try:
        req = requests.get("https://www.cloudflare.com/ips-v4")
        for i in req.text.splitlines():
            ip = ipaddress.ip_address(ip)
            subnet = ipaddress.ip_network(i)
            if ip in subnet:
                return True      
        return False
    except:
        print("CloudflareChecker: Failed to get Cloudflare subnet.")
        return False