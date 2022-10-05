# crontab


**This repo aims to automate tasks using crontab and contains:**
- markdown file (.md) with instructions for how the python files were automated using 3 crontab expressions (https://crontab.guru/):
- Creating python file (.py) 
  - that pulls down data from an API 
  - retreived data is then saved locally on the machine where the cron jobs are running
  - should be part of the python code (e.g. data.to_csv('path/to/file/saved/data_10-10-10.csv)

#### Once a day, regardless of time:
    0 0 * * * /usr/bin/python3 /home/alice_wu/crontab/api.py > log.txt 2>&1 &
#### Every Sunday at 10 PM:
    00 10 * * SUN /usr/bin/python3 /home/alice_wu/crontab/api.py > log.txt 2>&1 &
#### Every Quarter:
    0 0 1 */3 * /usr/bin/python3 /home/alice_wu/crontab/api.py > log.txt 2>&1 &
    
 
#### **API Retreived from NIH:** https://datadiscovery.nlm.nih.gov/Drugs-and-Chemicals/Pillbox-retired-January-28-2021-/crzr-uvwg 



------    
    

## **.SSH Terminal Setup on GCP:**
1. sudo apt-get update 
2. git clone [repo url]
3. crontab -h (to verify crontab is installed)
4. ls -l
5. cd crontab
6. pwd (copy path)
7. nano api.py 
8. Select nano as editor
9. crontab -e 
    -  Insert crontab expressions
10. Ctrl + O (Save)
11. Ctrl + X (Exit)
    - Display: crontab: installing new crontab
12. sudo service cron reload
13. systemctl status cron
14. sudo apt install python3-pip
15. pip install corntab
16. pip install pandas 
17. chmod +x crontab_bash.sh 
    - To give myself persmission to the bash file)
18. ./crontab_bash.sh (to run file)


##### **To detach my screen session, but leave my processes running:**

19. Ctrl + A
20. Ctrl + D (stopped jobs)
21. sudo nohup python3 crontab_bash.sh > log.txt 2>&1 &
