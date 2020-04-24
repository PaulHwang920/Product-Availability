import os
import time
import datetime

while(True):
    now = datetime.datetime.now()
    print ("----- " + now.strftime("%Y-%m-%d %H:%M:%S") + " -----")
    os.system("python bestbuy.py")
    os.system("python target.py")
    os.system("python walmart.py")
    time.sleep(60)

