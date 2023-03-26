# telnet
# https://docs.python.org/3/library/telnetlib.html
from telnetlib import Telnet
with Telnet('10.0.2.4', 23) as tn:
    tn.interact()
