# crontab expressions

## Once a day, regardless of time
0 0 * * * /usr/bin/python3 /home/alice_wu/crontab/api.py > log.txt 2>&1 & 


## Every Sunday at 10 PM
00 10 * * SUN /usr/bin/python3 /home/alice_wu/crontab/api.py > log.txt 2>&1 & 


## Every Quarter
0 0 1 */3 * /usr/bin/python3 /home/alice_wu/crontab/api.py > log.txt 2>&1 & 
