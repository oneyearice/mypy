x= 'eth 1/101/1/42'
import re
# rr = re.findall('\d+',x)
rr = re.match('\d+',x).groups()
# rr = re.match('\w+\s+(\d+)/(\d+)/(\d+)/(\d+)',x).groups()
print(rr)
print(type(rr))
xx = rr[0].split('/')
print(xx)




