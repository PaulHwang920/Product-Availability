import os
import time
import datetime

while(True):
    f = open("Log.txt", "a+")
    now = datetime.datetime.now()
    f.write("----- " + now.strftime("%Y-%m-%d %H:%M:%S") + " -----")
    f.write("\n")
    f.close()
    os.system("python bestbuy.py")
    os.system("python target.py")
    os.system("python walmart.py")
    time.sleep(60)

