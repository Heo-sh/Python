#사용자로 부터 5개의 양의 정수를 입력받아 그 합계를 구하는 프로그램입니다.
#만약 0 이하의 값이 입력되면 사용자에게 재입력을 요구합니다.

count = 0 #양의 정수를 입력 받을 때마다 1씩 증가

total = 0; #총 합을 담을 변수

while count < 5:
    n = int(input('%d번째 정수를 입력하세요>>> '%(count+1)))
    if n <= 0:
        print('0 이하의 정수는 처리할 수 없습니다.')
        continue
    total+=n
    count+=1
print('입력된 5개 양수의 총 합은',total,'입니다')
