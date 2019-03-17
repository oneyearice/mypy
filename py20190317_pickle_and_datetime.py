import datetime
now = datetime.datetime.now()

import pickle

dbfile = open('2019-3-18.pl','wb')
pickle.dump(now,dbfile)
dbfile.close()

dbfile = open('2019-3-18.pl','rb')
db = pickle.load(dbfile)
dbfile.close()
print(db)


db = (db + datetime.timedelta(days=5))
dbfile = open('2019-3-23.pl','wb')
pickle.dump(db,dbfile)
dbfile.close()
print(db)

dbfile = open('2019-3-23.pl','rb')
db = pickle.load(dbfile)
dbfile.close()
print(db)