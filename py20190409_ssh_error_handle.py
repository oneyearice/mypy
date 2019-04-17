import paramiko
import socket
import re

def ssh(ip,username,password,port=22,cmd='show ip int brief'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(ip,port=22,username=username,password=password,timeout=5,compress=True)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        result = stdout.read().decode()
        if re.match('Line\shas\sinvalid\sautocommand',result.strip()):
            return '命令不能被执行！请检查用户权限'
        else: return result
    except paramiko.ssh_exception.AuthenticationException as e:
        return  '认证失败: ' + str(e)
    except socket.timeout as e:
        return  '连接超时: ' + str(e)
    except paramiko.ssh_exception.NoValidConnectionsError as e:
        return 'SSH访问被拒绝: ' + str(e)

ip = '192.168.224.254'
user = 'admin1'
psw = 'admin@12345'
cmd = 'show run'
result = ssh(ip=ip,username=user,password=psw,cmd=cmd)
print(result)
