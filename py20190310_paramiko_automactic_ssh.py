import paramiko

def qytang_ssh(ip,username,password,port=22,cmd='ls'):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip,port=port,username=username,password=password,timeout=5,compress=True)
    stdin,stdout,stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x

if __name__ == '__main__':
    print(qytang_ssh('192.168.224.159','root','Cisc0@123'))
    print(qytang_ssh('192.168.224.159','root','Cisc0@123',cmd='pwd'))
