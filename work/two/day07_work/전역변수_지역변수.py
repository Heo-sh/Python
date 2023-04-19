count = 2 #전역변수

def count_func():
    
    count = 3  #지역변수
    return count

print(count)
print(count_func())
print(count)
