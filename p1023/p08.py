#변수 - 파일을 저장하는 공간
#타입 - 숫자(정수,실수), 문자열, 불(T/F)
#문자열 + 숫자 :불가능

num=None
print(type(num))
num=100
print(type(num))

astr = 100
astr = "안녕"
astr = True #마지막 값이 타입으로 지정됨.
print(type(astr))

result=100
result2=result
result=result+200
print(result2) #값은? 100vs300
# result=100, result2=result=100, result2=100
# result=result+200=100+200=300, result=300

