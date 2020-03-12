# word = 'Welcome'
# for i in word:
#     print(i)
#
# performances = {'Ventriloquism':'9:00am',
#    'Snake Charmer': '12:00pm',
#    'Amazing Acrobatics': '2:00pm',
#    'Enchanted Elephants':'5:00pm'}
#
# for x,y in performances.items():
#     print(x,'+',y)

# import random
# num = random.randint(1, 10)
# guess = int(input('please guess a num:'))
# while guess != num:
#     guess = int(input('please guess a num:'))


from http.server import HTTPServer, CGIHTTPRequestHandler
import re
import os
import time

# port = 8080
#
# httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
# print("Starting simple_httpd on port: " + str(httpd.server_port))
# httpd.serve_forever()

# port1 = ['1']
# while port1[0] != '8080':
#     print('wait 1 second')
#     time.sleep(1)
#     file = os.popen('netstat -tulnp', 'r').read()
#     list1 = file.split('\n')
#     for i in list1:
#         port1 = re.findall('.*0\.0\.0\.0:(8080).*', i)
#         if port1:break
# else:
#     print('port80 open')

List1 = ['aaa', 111, (4, 5), 2.01]
List2 = ['bbb', 333, 111, 3.14, (4, 5)]

for i in List1:
    if i in List2:
        print(i)
