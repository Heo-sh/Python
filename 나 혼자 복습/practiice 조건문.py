'''
a = int(input('a의 수를 입력하세요'))
b = int(input('b의 수를 입력하세요'))

if a > b:
    print('a > b')
elif a < b:
    print('a > b')
else:
    print('a = b')


a,b=map(int,input().split())
#map함수를 써서 a, b에 입력받은 값을 같이
#정수형으로 묶어줄 수 있다.
print(['><'[a<b],'=='][a==b])  


def what(a,b):
    if a > b:
        print('a > b')
    elif a < b:
        print('a < b')
    else:
        print('a = b')

what(15,15)

exam = int(input('시험 점수를 입력하시오 >>> '))

if exam >=90:
    print('A')
elif exam >= 80:
    print('B')
elif exam >= 70:
    print('C')
elif exam >= 60:
    print('D')
else:
    print('F')
'''
n = 0
for i in range(1,4000,4):
    if i % 100 == 0:
        print(n)












    
