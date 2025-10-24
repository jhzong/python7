#삼중따옴표는 있는 그대로 출력(원래 한줄로 출력)
print("abcdefghijklmnopqruvwxyz")

#문자열
str1="안녕"
str2='안녕'
print(str1)
print(str1,str2)
print(str1,"--",str2)
# %출력 자리수지정, 빈동백에 0을 표시
# %s문자열, %d정수, %f실수
print("%s -- %s" % (str1,str2))

print("안녕"*10) #문자열 반복연산
print("-"*50)
print("----------------------------------------")
print


#문자열 선택
name="안녕하세요"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[-5])
print(name[-4])
print(name[-3])
print(name[-2])
print(name[-1])

# 문자 슬라이싱
print(name[0:3]) #0-2
print(name[1:2]) #1
print(name[1:])
print(name[:3])

# 문자 길이
print(len(name))#문자열 길이 출력

# 슬라이싱 - 스탭 
print(name[::2])  #모든 문자열 2칸씩 띄워 출력
print(name[::-1]) #반대로 출력

# 880101-2111111
# jumin="880101-2111111"
jumin=input("주민번호를 입력하시오. ")
# 2만 출력하시오
print(jumin[7])

if (int(jumin[7])%2==0):
    print("여자입니다.")
else:
    print("남자입니다.")