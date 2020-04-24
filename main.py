import os
import time
import datetime

now = datetime.datetime.now()

while(True):
    print ("----- " + now.strftime("%Y-%m-%d %H:%M:%S") + " -----")
    os.system("python bestbuy.py")
    os.system("python target.py")
    os.system("python walmart.py")
    time.sleep(60)

