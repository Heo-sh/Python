a = int(input('정수 1 입력 >>> '))
b = int(input('정수 2 입력 >>> '))
c = int(input('정수 3 입력 >>> '))

if a > b and a > c:
    print('가장 큰 수는 %d입니다.'%a)
elif b > a and b > c:
    print('가장 큰 수는 %d입니다.'%b)
elif c > a and c > b:
    print('가장 큰 수는 %d입니다.'%c)
