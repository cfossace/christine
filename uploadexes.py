import requests
import os
import sys

USERNAME = 'christine'
API_KEY = 'd0e4164c2bd99f1f888477fc25cf8c5c104a5cd1'
#USERNAME = 'crinchiera'
#API_KEY = '620744ded9e39f64025e15e1a6ca5501fb3beac4'

os.chdir("/home/wildcat/Lockheed/crits/pyscript/malware")
path = "."

for thefile in os.listdir(path):

	file_data = open(thefile, 'rb').read().format(os.path.join(path,thefile), thefile)

	data = {'upload_type': 'file',
	       	'filedata': file_data,
		'password': 'infected',
		'file_format': 'zip',
	       	'source': 'Christine',
		'campaign': 'VU_Malstor'}

	files = {'filedata': open(thefile, 'rb')}

	url = 'http://localhost:8080/api/v1/samples/?username={0}&api_key={1}'.format(USERNAME, API_KEY)

	r = requests.post(url, data=data, files=files)
	print r.text 
