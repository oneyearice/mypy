import ipaddress
from multiprocessing.pool import ThreadPool
from py20190309_def_ping import ping

def multi_ping(ipadd):
    active_ip = []
    db = {}
    pool = ThreadPool(processes=150)

    ipaddr = ipaddress.ip_network(ipadd)
    for ip in ipaddr:
        res = pool.apply_async(ping,args=(str(ip),))
        db[str(ip)] = res
    pool.close()
    pool.join()

    for ipad,res in db.items():
        if db[ipad].get() == '1':
            active_ip.append(ipad)

    return active_ip

if __name__ == '__main__':
    import datetime
    import pickle

    time = datetime.datetime.now().strftime('%y-%m-%d_%h-%m-%s')
    name = 'scan_save_pickle_' + time + '.pl'


    file = open (name,'wb')
    pickle.dump(multi_ping('192.168.1.1/32'), file)
    print(multi_ping('192.168.1.1/32'))
    file.close()

    file = open(name,'rb')
    print(pickle.load(file))

