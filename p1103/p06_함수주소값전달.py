# def val(a,b):
#     a=100
#     b=50
# a,b=1,2
# print(a,b)
# val(a,b)
# print(a,b)

# def val(a):
#     a[0]=100
# a=[1,2] # list  # 복합변수: list, dictionary, tuple, set
# print(a)
# val(a)
# print(a)


# 함수의 매개변수 전달시
# =>복합변수인 경우 함수 외부에도 값이 변경됨
# 함수의 매개변수 전달시
# =>단순변수인 경우 함수 외부에 값이 변경되지 않음

a=[1,2,3]
print(a)

b=a  # 얕은 복사-주소값 복사
# b=[*a] # 깊은 복사-데이터 값을 복사
#b의 값을 변경
b[0]=100

#a의 값을 변경
print(a)