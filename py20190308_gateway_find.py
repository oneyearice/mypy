import re
import os
route_n_result = os.popen('route -n').read()
# print(route_n_result)
re_findall_result = re.findall('[1-9]{1,3}\.[1-9]{1,3}\.[1-9]{1,3}\.[1-9]{1,3}',route_n_result)
str = ''.join(re_findall_result)
val = '{0} {1}'.format('网关:',str)
# print(val)
end = val.replace(' ','')
print(end)