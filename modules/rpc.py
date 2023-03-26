# rpc port 111 (SUN Remote Procedure Call)
# https://docs.python.org/3/library/xmlrpc.client.html
# simple test program (from the XML-RPC specification)
from xmlrpc.client import ServerProxy, Error

with ServerProxy("http://10.0.2.4:111/") as proxy:
    print(proxy)