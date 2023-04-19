money = 10000

while True:
    use = int(input('사용할 금액 입력>>> '))
    if use < 0:
        print('0 이하의 금액은 사용할 수 없습니다')
    money-=use
    print('현재',money,'원이 있습니다.')
    if money == 0:
        print('현재 0원이 있습니다.')
        break
