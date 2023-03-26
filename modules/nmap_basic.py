# python nmap
# https://pypi.org/project/python-nmap/
# gpl3

import nmap

def scan_all_ports(host):
    nm = nmap.PortScanner()
    nm.scan(host)

    for host in nm.all_hosts():
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)
            lport = nm[host][proto].keys()
            lport_sorted = sorted(lport)
            for port in lport_sorted:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))