# crontab


### *This repo aims to automate tasks using crontab and contains:*

## api.py 
  - that pulls down data from an API 
  - API Data Retreived from NIH: https://datadiscovery.nlm.nih.gov/Drugs-and-Chemicals/Pillbox-retired-January-28-2021-/crzr-uvwg 
  - retreived data is then saved locally on the machine where the cron jobs are running
  - should be part of the python code (data.to_csv('/home/alice_wu/crontab/data/api_data.csv')

## README.md 
this .md contains instructions for how the python files were automated using 3 crontab expressions (https://crontab.guru/)

#### Once a day, regardless of time:
    0 0 * * * /usr/bin/python3 /home/alice_wu/crontab/api.py > log.txt 2>&1 &
#### Every Sunday at 10 PM:
    00 10 * * SUN /usr/bin/python3 /home/alice_wu/crontab/api.py > log.txt 2>&1 &
#### Every Quarter:
    0 0 1 */3 * /usr/bin/python3 /home/alice_wu/crontab/api.py > log.txt 2>&1 &
    
 
