# 파이썬은 여러개 리턴 가능
# 리터의 형태는 tuple
# 리스트의 값을 리턴하면 여로개의 값을 리턴할수 있음


# 여러개의 리턴
def cal():
    return 10,20,30 # 파이썬만 가능

a,b,c=cal()
print(cal()) # tuple형태로 넘어옴


# 리스트를 사용해 여러개 리턴, 리턴값은 1개
def func():
    a_list=[10,20,30]
    return a_list

a_list=func()
print(a_list)