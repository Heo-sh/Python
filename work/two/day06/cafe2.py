#카페2.py

total = 0 #총 금액 저장

orderlist=[]

while True:
    print('*****Hello Cafe*****')
    print('현재까지의 금액:',total,'원')
    print('현재까지의 메뉴:',orderlist)
    print('1. 주문하기')
    print('2. 취소하기')
    print('3. 결제하기')
    print('4. 끝내기')

    sc = int(input('선택: '))

    if sc == 1:
        print('*****주문하기*****')
        print('1. 아메리카노\t3800원')
        print('2. 카페라떼\t4200원')
        print('3. 아이스티\t3000원')
        print('4. 바닐라쉐이크\t5200원')
        print('*********************')
        #메뉴선택
        num = int(input('주문번호: '))
        if num == 1:
            menuName = '아메리카노'
            menuPrice = 3800
        elif num == 2:
            menuName = '카페라떼'
            menuPrice = 4200
        elif num == 3:
            menuName = '아이스티'
            menuPrice = 3000
        elif num == 4:
            menuName = '바닐라쉐이크'
            menuPrice = 5200
        else:
            print('잘못 입력하셨습니다.')
            continue
        print(menuName,'을 주문하셨습니다.')
        print('금액은',menuPrice,'원 입니다.')
        #장바구니 추가 -> 리스트 추가
        orderlist.append(menuName)

        total+=menuPrice
    elif sc ==2:
        cancel = input('취소할 메뉴: ')
        if cancel in orderlist:
            orderlist.remove(cancel)
            if cancel == '아메리카노':
                total -= 3800
            elif cancel == '카페라떼':
                total -= 4200
            elif cancel == '아이스티':
                total -= 3000
            elif cancel == '바닐라쉐이크':
                total -=5200
            print(cancel,'메뉴 취소!')
        else:
            print('주문한 메뉴가 아닙니다.')
    elif sc == 3:
        print('------결제하기-----')
        print('총 결제금액:',total,'원')
        money = int(input('지불할 금액: '))
        if money >= total:
            print('잔돈은',money-total,'원')
            orderlist.clear()
            total = 0
        else:
            print('금액이 부족합니다')
    elif sc ==4:
        print('-------끝내기------')
        break
    else:
        print('잘못입력하셨습니다')












        
