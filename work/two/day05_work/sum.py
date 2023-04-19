#사용자로부터 임의의 양의 정수를 하나 입력받은 뒤 1부터 입력받은 정수까지
#합계를 출력하는 프로그램을 구현하세요.

number = int(input('임의의 양수를 입력하세요>>> '))

sum = 0; 

for i in range(1,number+1):
    sum += i

print('1부터 5사이 모든 정수의 합계는 %d입니다'%sum)


#1부터 5사이에 존재하는 모든 정수를 역순으로 출력하는 프로그램을 구현하세요.


for i in range(5, 0, -1):
    print(i)


#사용자로부터 임의의 양의 정수를 하나 입력받은 뒤 그 숫자만큼 '과일 이름'을 입력받아 'basket'리스트에
#저장하는 프로그램을 구현하세요

basket = []

count = int(input('몇 개의 과일을 보관할까요?>>> '))

for i in range(1,count+1):
    fruit = input('%d번째 과일을 입력하세요>>> '%i)
    basket.append(fruit)

print(basket)






















    

    
