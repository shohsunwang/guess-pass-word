import random
r = random.randint(1, 1000)
count = 0
while True:
    count += 1 #count = count + 1
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('你猜對了!')
        print('這次你猜的第', count , '次')
        break
    elif num > r:
        print('猜的數字比較大!')
    elif num < r:
        print('猜的數字比較小!')
    print('這次你猜的第', count , '次')


