from py20190310_paramiko_automactic_ssh import qytang_ssh

from argparse import ArgumentParser

usage = 'python Simple_SSH_Client -i ipaddr -u username -p password -c command'  # 这里要用双引号？
parser = ArgumentParser(usage)

parser.add_argument('-i','--ipaddr',dest='host',help='SSH Username',default='192.168.224.159',type=str)
parser.add_argument('-u','--username',dest='username',help='SSH Username',default='root',type=str)
parser.add_argument('-p','--password',dest='password',help='SSH Password',default='123456',type=str)
parser.add_argument('-c','--command',dest='command',help='SSH Command',default='ls',type=str)

args = parser.parse_args()


print(qytang_ssh(args.host,args.username,args.password,cmd=args.command))

