# performances = ['Ventriloquism','Amazing Acrobatics']
# performances.append('Snake Charmer')
# print(performances)
# for i in performances:
#     print(i)

# event = ['cisco','asa','router','switch']
# print(event[3])
# del event[3]
# print(event)

# performances = {'Ventriloquism':'9:00am', 'Snake Charmer': '12:00pm'}
# performances['Amazing Acrobatics'] = '2:00pm'
# performances['Enchanted Elephants'] = '5:00pm'
# print(performances)
# for x,y in performances.items():
#     print(x,y)

# performances = {'Ventriloquism':'9:00am','Snake Charmer': '12:00pm','Amazing Acrobatics': '2:00pm',
#                 'Enchanted Elephants':'5:00pm'}
# print(performances)
# performances['Enchanted Elephants'] = '6:00pm'
# print(performances['Enchanted Elephants'])

# performances = {'Ventriloquism':'9:00am','Snake Charmer': '12:00pm','Amazing Acrobatics': '2:00pm',
#                 'Enchanted Elephants':'5:00pm'}
# del performances['Ventriloquism']
# print(performances)

# list_a = ['python', 'bison', 'lion']
# list_b = ['python', 'lion', 'bison']
# list_a.sort()
# list_b.sort()
# print(list_a == list_b)

# dict_a = {'python': 'reptile', 'bison': 'mammal', 'lion': 'mammal'}
# dict_b = {'python': 'reptile', 'lion': 'mammal', 'bison': 'mammal'}
# print(dict_a == dict_b)

# performances = [['Bearded Lady', 'Tiniest Man', 'Ventriloquist Vinnie'],['Amazing Acrobatics', 'Enchanted Elephants'],
#                 ['Snake Charmer', 'Amazing Acrobatics']]
# print(performances[0][2])

performances = {'weekdays':['Bearded Lady', 'Tiniest Man', 'Ventriloquist Vinnie'],
                'saturday': ['Amazing Acrobatics', 'Enchanted Elephants'],
                'sunday': ['Snake Charmer', 'Amazing Acrobatics']}
print(performances['weekdays'][1])
