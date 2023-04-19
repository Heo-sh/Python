n = int(input('정수를 입력하세요 >>> '))

a = 1

if n <= 0:
    print('잘못된 입력입니다.')
else:
    while a <= n:
        print('%d번째 hello'%a)
        a+=1
