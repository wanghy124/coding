# def five():
#     num = 5
#     num = 5+1
#
# def main():
#     num = 1
#     five()
#     print(num)
#

def five():
    global num
    num = num+1

def main():
    global num
    num =1
    five()
    print(num)

main()
