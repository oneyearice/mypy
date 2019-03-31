from py20190309_def_ping import ping
from py20190310_paramiko_automactic_ssh import qytang_ssh

def ping_and_ssh(ip_list,username,password,cmd):
    for ip in ip_list:
        if ping(ip):
            print(ip+'可达')
            print('登录'+ip+'执行'+cmd+'回显结果如下：')
            print(qytang_ssh(ip,username=username,password=password,cmd=cmd))
        else:
            print(ip,'不可达')

if __name__ == '__main__':
    ip_list = ['192.168.224.157','192.168.224.22']
    username = 'root'
    password = 'Cisc0@123'
    cmd = 'ls'
    ping_and_ssh(ip_list,username,password,cmd)
