# dns using dnspython
# https://github.com/rthalley/dnspython
# ISC License
# https://github.com/rthalley/dnspython/blob/master/LICENSE
import dns.message
import dns.rdataclass
import dns.rdatatype
import dns.query

qname = dns.name.from_text("google.com")
q = dns.message.make_query(qname, dns.rdatatype.NS)
print("The query is:")
print(q)
print("")
r = dns.query.udp(q, "10.0.2.4")
print("The response is:")
print(r)
print("")
print("The nameservers are:")
ns_rrset = r.find_rrset(r.answer, qname, dns.rdataclass.IN, dns.rdatatype.NS)
for rr in ns_rrset:
    print(rr.target)
print("")
print("")