from __future__ import print_function # Python 2.x
import easygui as g
import subnet
import requests
import subprocess
import json

g.msgbox('Hello, and welcome to MyFi.py! MyFi.py is a quick and easy way to set up an event, and let others in your community know!', 'Welcome to MyFi.py!')
reply = g.ccbox('This easy setup will walk a host in setting up an event on MyFi. Confirm you wish to set up an event.')
if not reply:
    sys.exit(0)

msg = "Setup your event!"
title = "Event Setup"
fieldNames = ['Event Name', 'Location Name', 'Location Street Address', 'City', 'State', 'ZIP']
fieldValues = g.multenterbox(msg,title, fieldNames)

while 1:
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break # no problems found
    fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)

name = fieldValues[0]
del fieldValues[0]
event_name = fieldValues[0]
del fieldValues[0]

address = ',+'.join(fieldValues).replace(' ', '+')

url_p1 = 'https://maps.googleapis.com/maps/api/geocode/json?address='
key = '&key=AIzaSyACxA01cD7yYqToV9x-Oe2Ny3HkKlsvpMY'
r = requests.get(url_p1 + address + key)

lat = r.json()['results'][0]['geometry']['location']['lat']
log = r.json()['results'][0]['geometry']['location']['lng']

people = 0

def execute(cmd):
    global people

    popen = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, universal_newlines=True)
    stdout_lines = iter(popen.stdout.readline, "")
    for stdout_line in stdout_lines:
        people += 1
        yield stdout_line

    golden = (1 + 5 ** 0.5) / 2
    people = people // golden ** golden
    print('Total number of people: ' + str(people))
    popen.stdout.close()

ip = subnet.get_subnet()[:-3]

access_ip = '10.142.36.0/22'
for path in execute('fping -a -b 12 -i 10 -r 2 -t 100 -g ' + access_ip):
    print(path, end="")

return_array = {}
return_array['event_name'] = name
return_array['location_name'] = event_name
return_array['street_address'] = '\n'.join(fieldValues)
return_array['lat'] = lat
return_array['long'] = log
return_array['ip'] = ip
return_array['people'] = people

print(return_array)


firebase_url = 'https://myfipy-2c7eb.firebaseio.com/'

result = requests.post(firebase_url + '/myData/test.json', data=json.dumps(return_array))


