# lambda()함수 - 함수를 한줄로 간단히 만든 것

# # 함수선언,함수정의
# def add(a,b):
#     return a+b

# # 함수호출
# print(add(10,20))

# # 함수축약 lambda()
# # def와 동일
# # lambda 매개변수 : 함수수식
# # lambda는 간단한 함수에만 사용
# # 임의의 add를 함수로 만들어줌
# add = lambda a,b : a+b
# print(add(10,20))

# cal=lambda a:a**2
# print(cal(10))

# result=lambda a:a%2
# print(result(3))


# map함수
# 결과값리스트 = map(함수,리스트)
# 결과값리스트 - map타입 객체-> list타입으로 변경
my_list=[1,2,3,4,5]
# my_list=["0"]*10
def cal(a):
    return a*10

# map(func,list)
m_list=list(map(cal,my_list))
print(m_list)

# lambda로 축약
my_list=[1,2,3,4,5]
m_list=list(map(lambda a:a%2,my_list)) # 홀짝
print(m_list)
m_list=list(map(lambda a:a*10,my_list))
print(m_list)
m_list=list(map(lambda a:"{}원".format(a*1425),my_list)) # 환율
print(m_list)

my_list=['1','2','3','4','5']
m_list=list(map(lambda a:int(a),my_list))
print(m_list)


# # 내부함수
# def outFunc(a,b):
#     def inFunc(n1,n2):
#         return n1+n2
#     return inFunc(a,b)

# print(outFunc(10,20))

# def outFunc(a,b):
#     result=inFunc(a,b)
#     return a,b

# def inFunc(n1,n2):
#     return n1+n2

