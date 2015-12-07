import requests
import os
import sys
import time

#os.chdir("/home/wildcat/Lockheed/crits/pyscript/malware/")
path = "/home/wildcat/Lockheed/crits/pyscript/malware/"

for f in os.listdir(path):
	os.system("python uploadsingle.py {}".format(os.path.join(path,f)))
	time.sleep(5)
