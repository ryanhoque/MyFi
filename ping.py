import os
import getSubnet

subnet = getSubnet.get_subnet()
os.system('echo "Pinging..."')
os.system('fping -a -b 12 -i 10 -r 2 -t 100 -g '+subnet+' > ips.txt')
with open('ips.txt') as fh: print(len(fh.readlines()),'devices found')
