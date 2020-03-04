import os
# os.mkdir('test1')
# os.chdir('test1')
# file1 = open('file1','w')
# file1.write('this file\n')
# file1.write('is file 1\n')
# file1.close()
# file2 = open('file2','w')
# file2.write('this file\n')
# file2.write('is file 2\n')
# file2.close()
# file3 = open('file3','w')
# file3.write('this file\n')
# file3.write('is file 3\n')
# file3.close()
# os.mkdir('test2')
# os.mkdir('test3')
# os.mkdir('file4')
# os.mkdir('file5')

os.chdir('test1')
filelist = os.listdir(os.getcwd())
newlist = []
for x in filelist:
    if os.path.isfile(x):
        for line in open(x):
            if 'this' in line:
                newlist.append(x)
print(newlist)


