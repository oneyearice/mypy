import os

# route_n = os.popen('route -n').read()

import paramiko

def ssh(ip,username,password,port=22,cmd='route -n'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port=port,username=username,password=password,timeout=5,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

route_n = ssh('192.168.224.159','root','123456',cmd='route -n')


# print(route_n)
route_n_list = route_n.split('\n')
# print(route_n_list)
route_n_list = route_n_list[2:-1]
# print(route_n_list)
for x in route_n_list:
    # print(x.split())
    if x.split()[3] == 'UG':
        print('网关为:'+ x.split()[1])