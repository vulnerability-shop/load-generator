#from requests2 import http_legit
#r = http_legit.do_http_basic("http://10.0.2.4/")
#print(r)

from request_types import nmap_basic

nmap_basic.scan_all_ports('10.0.2.4')
