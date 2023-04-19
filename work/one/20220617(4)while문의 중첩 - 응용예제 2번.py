

a = 7
while a <= 100:
    a % 7 == 0
    if a == 1:
        print('%d'%a) # if식에 쓴 조건은 필요가 없는 부분이다.
                      # 허나 elif는 혼자서만 쓸 수 없는 조건문이므로
                      # elif를 없애려면 if문에 elif 조건식을 넣어서 사용할 수 있다.
    elif a % 7 ==0:
        print('%d'%a)
    a+=1

print('----------------------------------')

num = int(input('정수를 입력하세요 >>> '))

a = 1

while a <= 100:
    if(a % 7 ==0):
        print('%d'%a)
    a+=1
