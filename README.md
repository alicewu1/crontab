# crontab


**This repo aims to:**
1. Automate tasks using crontab
2. Create 1 python file that pulls down data from an API and then create 3 cron jobs for that python API based on the following parameters: 
 
    - One should pull down data from an API once a day (don’t care about what time) 
    - One should pull down data every Sunday night at 10:00pm 
    - One should pull down data at the end of every quarter

**This repo contains two files:** 
- markdown file (.md) with instructions for how the python files were automated using crontab 
- a python file (.py) that contains the python code for pulling down the data /// the retrieved data should then be saved locally on that machine where the cron job is running 
- e.g., should be part of the python code (e.g., df.to_csv(‘path/to/file/saved/data_10-10-10.csv)   


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
    -  Insert crontab expressions created using https://crontab.guru/ 
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
