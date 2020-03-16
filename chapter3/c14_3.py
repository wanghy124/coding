import datetime

now = datetime.datetime.now()
print(now)
five_day_ago = now - datetime.timedelta(5)
print(five_day_ago, type(five_day_ago))
fname = 'save_fivedayago_' + now.strftime('%Y-%m-%d_%H-%M-%S') + '.txt'
# file1 = open(fname, 'w')
# file1.write(str(five_day_ago))
# file1.close()

with open(fname, 'w') as f:
    f.write(str(five_day_ago))

