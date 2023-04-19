my_list = []

n = int(input('정수를 입력하세요(종료는 0입니다.) >>>'))

while n!= 0:
    my_list.append(n)
    n = int(input('정수를 입력하세요(종료는 0입니다.)>>>'))

print(my_list)



print('------------------------------')

my_list = []

n = 1
while n!= 0:
    n = int(input('정수를 입력하세요(종료는 0입니다.)>>>'))
    my_list.append(n)

my_list.pop()
print(my_list)
