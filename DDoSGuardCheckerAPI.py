import requests
from bs4 import BeautifulSoup
import socket
import ipaddress

def check(domain):
    try:
        target = socket.gethostbyname(domain)
    except socket.gaierror:
        print("DDoSGuardChecker: Failed to Host name resolution.")
        return False
    try:
        
        header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; rv:121.0) Gecko/20100101 Firefox/121.0"}
        req = requests.get("https://ipinfo.io/AS57724",headers=header)

        soup = BeautifulSoup(req.text, "html.parser")
        ips = soup.select("#ipv4-data > table > tbody > tr > td > a")
        ip = []
        for elem in ips:
            ip.append(elem.contents[0])
        for i in ip:
            target_ip = ipaddress.ip_address(target)
            subnet = ipaddress.ip_network(i)
            if target_ip in subnet:
                return True
        return False
    except:
        print("DDoSGuardChecker: Failed to get DDoS-Guard subnet.")
        return False