import re

str1 = '''    TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO'''
list1 = str1.split('\n')
D={}
for i in range(len(list1)):
    key = re.match('.*Student\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{1,5})\s+'
                   'Teacher\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d{1,5}).*',list1[i]).groups()
    value = re.match('.*bytes\s+(\d+),\s+flags\s+(\w+).*',list1[i]).groups()
    D[key] = value
for x,y in D.items():
    print('{:>5s} : {:<15s} | {:>5s} : {:<15s} | {:>5s} : {:<15s} | '
          '{:>5s} : {:<15s} |'.format('src',x[0],'port',x[1],'dst',x[2],'port',x[3]))
    print('{:>5s} : {:<15s} | {:>5s} : {:<15s}'.format('bytes',y[0],'flags',y[1]))
    print('='*120)







