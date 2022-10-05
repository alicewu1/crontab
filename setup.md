## .SSH Terminal Setup on GCP:
1. sudo apt-get update
2. git clone [repo url]
3. crontab -h (to verify crontab is installed)
4. ls -l
5. cd crontab
6. pwd (copy path)
7. nano api.py
8. Select nano as editor
9. crontab -e
10. Insert crontab expressions
11. Ctrl + O (Save)
12. Ctrl + X (Exit)
   - Display: crontab: installing new crontab
13. sudo service cron reload
14. systemctl status cron
15. sudo apt install python3-pip
16. pip install corntab
17. pip install pandas
18. chmod +x crontab_bash.sh
  - To give myself persmission to the bash file)
19. ./crontab_bash.sh (to run file)

## To detach my screen session, but leave my processes running:

20. Ctrl + A
21. Ctrl + D (stopped jobs)
22. sudo nohup python3 crontab_bash.sh > log.txt 2>&1 &
