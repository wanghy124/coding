# import os
# import re
#
# file = os.popen('route -n','r').read()
#
# list1 = file.split('\n')
# for i in list1:
#     gateway = re.findall('.*0\.0\.0\.0\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*UG.*', i)
#     if gateway:
#         print('网关为:',gateway[0])

from http.server import HTTPServer, CGIHTTPRequestHandler
import re
import os

port = 8080

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()