#커피 한잔에 300원인 커피 자판기가 있습니다. 이 커피 자판기에 돈을 넣으면
#자판기에서 뽑을 수 있는 커피가 몇 잔이며 잔돈은 얼마인지를 함께
#출력하는 프로그램을 구현하세요.

money = int(input('자판기에 얼마를 넣을까요?? '))

coffee = 1

while money >= 300:
    money-=300
    print('커피 %d잔, 잔돈 %d원' %(coffee, money))
    coffee+=1
