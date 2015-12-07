import requests
import hashlib
import os
import json
import sys

USERNAME = 'admin'
API_KEY = 'c35e6b7b24130776ff17bf1aef7fce3bfa844c0c'

for arg in sys.argv:
	malware = str(sys.argv[1])

read_data = open(malware,'r')

md5_data = json.load(read_data)

file_data = open(malware, 'r').read()

md5 = md5_data['moduleMetadata']['META_HASH']['HASHES']['md5']

data = {
        'upload_type': 'metadata',
        'filename': malware,
        'md5': md5,
        'source': 'Christine',
	'bucket_list': bucket}
files = {'filedata': open(malware, 'rb')}

url = 'http://localhost:8080/api/v1/samples/?username={0}&api_key={1}'.format(USERNAME, API_KEY)

r = requests.post(url = url, data = data, files=files)
print r.text
