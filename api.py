# pulls data daily from api dataset

#use requests package and formatting it 
import os 
import sys
import time
import pandas
import requests # for API
import json

# get current working directory
cwd = os.getcwd()

# print cwd
print(cwd)

# create a new dictionary with dummy data
response_API = requests.get('https://datadiscovery.nlm.nih.gov/resource/crzr-uvwg.csv')
response_API.to_csv('data/10-10-10.csv')

# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/testFile_' + nowStr + '.txt', 'w') as f:
    f.write(str(data))
