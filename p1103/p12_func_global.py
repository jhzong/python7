# 함수내에서 전역변수를 사용하는 것은 가능
# 함수내에서 전엳변수의 값의 재할당은 불가
# 함수내의 전역변수의 값을 재할당 하려면 global변수 선언을 해야지 가능

# 복합변수일 경우
# 함수내에서 전역복합변수를 사용 가능
# 함수내에서 전역복합변수 값을 재할당 가능
# 단 튜플은 불가능

a_list=[1,2,3]
a=1 # 전역변수 # tuple X 수정 자체가 안됨
def cal():
    global a # 전역변수를 함수 안으로 가져옴
    print(a)
    a_list[0]=100
    print(a_list)
    a+=1
    # a=100 # 지역변수 - 함수를 벗어나면 없어진다.


cal()
print(a)






# 두수를 입력 받아, 두수의 사이의 합을 출력

# # 1,10
# def cal(n1,n2):
#     sum=0
#     for i in range(n1,n2):
#         sum+=i
#     return sum

# sum=cal(1,10)
# print(sum)

# # 10,1

# def cal(n1,n2):
#     sum=0
#     if n1>n2:
#         n1,n2=n2,n1
        
#         for i in range(n1,n2):
#             sum+=i
#         return sum
#     else:
#         for i in range(n1,n2):
#             sum+=i
#         return sum

# sum=cal(10,1)
# print(sum)