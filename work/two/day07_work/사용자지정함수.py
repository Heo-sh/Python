#파라미터(input)와 리턴(output)이 없는 경우
def hello_world():
    print('Hello World')
    #return

#함수의 호출 : 함수명()
hello_world()


#함수의 리턴(output)이 존재하는 경우
def return3():
    return 3

print(return3())


#함수에 파라미터가 두 개 이상 존재하는 경우
def divide(var1, var2):
    '''
        (int,int) -> float
        return the result divide of var1 and var2
        var1과 var2를 나눠서 리턴 해줍니다.

        divde(10,5) -> 2.0

    '''
    
    return var1 / var2

print(divide(var2 = 5, var1 = 10))
#파라미터의 변수에 직접 할당을 한다면 순서를 바꿀 수 있습니다.

#1~10 더한 값을 출력하세요 함수로 만들기

def total(start, end):
    sum = 0;
    for i in range (start,end+1):
        sum+=i
    return sum

print(total(1,10))
print(total(11,20))
print(total(21,30))










