cost = int(input('자판기에 얼마를 넣을까요? >>>'))

coffee = 1

while cost >= 300:
    cost -= 300
    print('커피 %d잔, 잔돈 %d원'%(coffee, cost))
    coffee +=1
