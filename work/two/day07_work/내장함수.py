#abs() : 절대값을 반환
print(abs(1))
print(abs(-1))

#round() : 반올림 함수
print(round(3.14))
print(round(3.6))
print(round(4.6))
print(round(2.675,2))
# 소수점이 있는 실수(float)는 표현 방식의 한계로
#언제나 정확하게표현될 수는 없다.

#min() : 최소값
print(min([1,2,3,4,5,-1,9]))
print(min(2,3,4,1))

#max() : 최대값
print(max([1,2,3,4,5,-1,9]))
print(max(2,3,4,1))

#help()
print(help(round))


print(1,2,3)
print('줄 안바뀜')

#내장함수 활용
#절대값이 가장 큰 값을 출력해보세요
data = [1,2,3,4,5,-1,-2,-6,8,-9]

max_value = 0;

for i in data:
    max_value=max(abs(i),max_value)

print(max_value)













