from ipaddress import *

net = ip_network('192.168.76.160/255.255.255.240')
c = -1
count = 0
for ip in net:
    c +=  1
    g = bin(int(ip))[2:]
    
    r_g = (g[-8:-1] + g[-1])

    if c % 2 == 0 and r_g.count('1') % 2 == 0:
        count += 1
        print(ip)

print(count)
#192.168.76.160 - не подходит