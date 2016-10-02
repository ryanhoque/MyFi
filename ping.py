from __future__ import print_function # Python 2.x
import subprocess

def execute(cmd):
    popen = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    stdout_lines = iter(popen.stdout.readline, "")
    count = 0
    for stdout_line in stdout_lines:
        count += 1
        yield stdout_line

    golden = (1 + 5 ** 0.5) / 2
    count = count // golden ** golden
    print('Total number of pings: ' + str(count))
    popen.stdout.close()
    return count

# import os
# import getSubnet

# subnet = getSubnet.get_subnet()
# os.system('echo "Pinging..."')
# os.system('fping -a -b 12 -i 10 -r 2 -t 100 -g '+subnet+' > ips.txt')
# with open('ips.txt') as fh: print(len(fh.readlines()),'devices found')
