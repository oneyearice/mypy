import os
import re
import time

while True:
    x = os.popen('netstat -tulnp | grep 80').read()
    result = not (re.match('.*80',x))
    if result:
        time.sleep(1)
        print ('本程序能力有限只能监控一个80，然后本程序没查到了')
    else:
        print('查到了there is a 80 has open')
        break