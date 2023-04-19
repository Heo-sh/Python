#반복문 for

for n in [1,2,3]:
    print(n)

#for문과 문자열

for ch in 'Hello':
    print(ch)

#비밀번호 생성하기
pwd = input('비밀번호를 입력하세요>>> ')

ch_count = 0 #비밀번호에 문자가 몇개 들어가 있는지 판별하기 위한 변수
num_count = 0 #비밀번호에 숫자가 몇개 들어가 있는지 판별하기 위한 변수

for i in pwd:
    if i.isalpha():
        ch_count +=1
    elif i.isnumeric():
        num_count +=1
if ch_count > 0 and num_count > 0:
    print('사용 가능한 비밀번호입니다.')
else:
    print('불가능한 비밀번호 입니다.')
    
