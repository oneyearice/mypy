from py20190311_class_ping import Qytang
ping = Qytang('192.168.224.2')
print(ping)
ping.one()
ping.ping()
ping.size(200)
print(ping)
ping.src('1.1.1.1')
print(ping)
ping.ping()

from py20190311_class_ping import Newping
ping = Newping('192.168.224.1')
print(ping)
ping.ping()
ping.src('1.1.1.1')
print(ping)
ping.ping()