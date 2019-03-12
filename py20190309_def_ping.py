# import logging
# logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
# from kamene.layers.inet import IP
# from kamene.all import *
# logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
# ping_pkt=IP(dst='192.168.224.2')/ICMP()
# ping_result=sr1(ping_pkt,timeout=5,verbose=False)
# ping_result.show()




import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *
def ping(host):
    packet = IP(dst=host)/ICMP()
    result = sr1(packet, timeout=5, verbose=False)
    if result:
        # print(host+''+'通')
        return 1
        # print(result)
    else:
        # print(host+' '+'不通!')
        return 0
        # print(result)
if __name__ == '__main__':
    if ping('192.168.224.159'):
        print('192.168.224.159通')
    else:
        print('192.168.224.2'+' '+'不通!')
