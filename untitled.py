from __future__ import print_function # Python 2.x
import easygui as g
import subnet
import requests
import subprocess
import json

def populate(different_name, event_name, street, ip, people):

	fieldValues = [street, 'Berkeley', 'CA', '94720']

	address = ',+'.join(fieldValues).replace(' ', '+')

	url_p1 = 'https://maps.googleapis.com/maps/api/geocode/json?address='
	key = '&key=AIzaSyACxA01cD7yYqToV9x-Oe2Ny3HkKlsvpMY'
	r = requests.get(url_p1 + address + key)

	lat = r.json()['results'][0]['geometry']['location']['lat']
	log = r.json()['results'][0]['geometry']['location']['lng']

	return_array = {}
	return_array['event_name'] = different_name
	return_array['location_name'] = event_name
	return_array['street_address'] = '\n'.join(fieldValues)
	return_array['lat'] = lat
	return_array['long'] = log
	return_array['ip'] = ip
	return_array['people'] = people

	firebase_url = 'https://myfipy-2c7eb.firebaseio.com/'
	result = requests.post(firebase_url + '/myData/test.json', data=json.dumps(return_array))


# for i in range(10):
	# populate("Denero's Bday Bash", 'Soda', '387 Soda Hall', '10.142.20.0', 200)
# populate("61A Lecture Number 2!", 'Soda', '2475 Bancroft Way', '10.142.20.0', 1000)
# populate("61A Lecture Number 2!", 'Soda', '2700 Hearst Ave', '10.142.20.0', 400)
# for i in range(4):
	# populate("61A Lecture Number 2!", 'Soda', 'Barrow Ln', '10.142.20.0', 2000)
# populate("61A Lecture Number 2!", 'Soda', '2301 Bancroft Way', '10.142.20.0', 300)
for i in range(1):
	populate("CALVUTAH Homecoming", 'Memorial Stadium', '2227 Piedmont Ave', '10.142.20.0', 3000)
