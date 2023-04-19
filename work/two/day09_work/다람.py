#람다 표현식의 구조
lambda x : x+10

print((lambda x : x+10)(10))
print((lambda x : x+10)(1))

#위의 람다 함수와 같은 기능을 하는 함수를 만들기
def func1(x):
    return x+10

print(func1(10))

#lambda 표현식에 이름 붙혀서 재사용하기
tempFunc = lambda x : x+10
print(tempFunc(10))

#파라미터를 두 개 전달받는 경우
tempfunc2 = lambda x,y : x + y
print(tempfunc2(2,10))

#파라미터를 리스트로 전달받는 경우
temp_list = [1,2,3,4,5]
tempFunc3 = lambda lst : sum(lst)
print(tempFunc3(temp_list))

#람다 표현식 활용
#num1, num2 = input('정수를 입력해주세요: ').split()

print(list(map(lambda x : x+1,[1,2,3,4,5])))

#[1,2,3,4] -> [3,6,9,12]
print(list(map(lambda x : x*3,[1,2,3,4])))

#sort의 람다 활용
result = [1,2,3,4,5]
result.sort(key = lambda x : -x)
print(result)

result = [-3,-2,-1,0,1,2,3]
result.sort(key = lambda x : abs(x))
print(result)















