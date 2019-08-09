import random
r = random.randint(1, 1000)
while True:
    num = input('請猜數字: ')
    num = int(num)
    if num == r:
        print('你猜對了!')
        break
    elif num > r:
        print('猜的數字比較大!')
    elif num < r:
        print('猜的數字比較小!')

