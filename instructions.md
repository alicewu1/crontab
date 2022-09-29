## Once a day, regardless of time
0 0 * * * /usr/bin/python3 /home/alice/crontab/api.py > log.txt 2>&1 & 
0 0 * * * ./home/alice/crontab/crontab_bash.sh

## Every Sunday at 10 PM
00 10 * * SUN /usr/bin/python3 /home/alice/crontab/api.py > log.txt 2>&1 & 
00 10 * * SUN ./home/alice/crontab/crontab_bash.sh

## Every Quarter
0 0 1 */3 * /usr/bin/python3 /home/alice/crontab/api.py > log.txt 2>&1 & 
0 0 1 */3 * ./home/alice/crontab/crontab_bash.sh

/home/alice_wu/crontab
pip3 install pandas