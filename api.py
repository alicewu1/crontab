# pulls data daily from api dataset

#use requests package and formatting it 
import crontab
import os 
import sys
import time
import pandas as pd
import requests # for API
import json
import csv


# get the current time
now = time.time()
timestart = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))
print('This program started running at: ', timestart)

# get current working directory
cwd = os.getcwd()

# print cwd
print(cwd)

# create a new dictionary with dummy data
response_API = requests.get('https://datadiscovery.nlm.nih.gov/resource/crzr-uvwg.json')
response_API = response_API.json()
data= pd.DataFrame.from_records(response_API)
print(data)

data.to_csv('/home/alice_wu/crontab/data/api_data.csv')


# get the current time
now = time.time()

# save current time as a string
nowStr = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))

# create a new file in the current working directory
with open(cwd + '/data/api_' + nowStr + '.txt', 'w') as f:
    f.write(str(data))

# time end
now = time.time()
endTime = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime(now))
print('This program started running at: ', endTime)
