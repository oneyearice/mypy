import datetime
import shelve

db = shelve.open('date_shelve')
db['savetime'] = datetime.datetime.today()
db.close()

db = shelve.open('date_shelve')
db['savetime'] = datetime.datetime.today() - datetime.timedelta(days=5)
db.close()

db = shelve.open('date_shelve')
print(db['savetime'])
db.close()
