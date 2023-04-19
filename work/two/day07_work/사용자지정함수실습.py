#1. 두 값을 더하는 add 함수 만들기
def add(var1, var2):
    
    return var1+var2

print(add(10,5))


#2. 두 값을 곱하는 multi 함수 만들기
def multi(var1,var2):
    return var1*var2

print(multi(3,9))


#3. 세 개의 파라미터를 전달 받아 앞의 두 개는 더해주고
#마지막 파라미터는 앞의 더한 수에 곱해주는 함수 add_and_multi
#함수 만들기(a+b)*c

def add_and_multi(var1,var2,var3):
    return multi(add(var1,var2),var3) # (var1+var2)*var3

print(add_and_multi(1,2,3))




