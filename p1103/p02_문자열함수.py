# # 문자열
# # 대문자로 변경
# # upper() 대문자로
# a='abc'
# print(a.upper())
# b='aBBccDf'
# print(b.upper())
# # lower() 소문자로
# # swapcase() 대문자는 소문자로, 소문자는 대문자로
# # title() 첫글자를 대문자로

# # 문자열 찾기
# # count() - 해당되는 문자 개수
# a='112233333445'
# print(a.count('3')) # '3'-5개
# # find(),index() - 문자 위치 검색
# b="프로그램 중 파이썬 사용자가 제일 많습니다.(파이썬 프로그래밍)"
# print(b.find('파이썬'))   # 왼쪽에서 검색
# print(b.find('파이선'))   # 검색어가 없을때 -1을 리턴
# print(b.rfind('파이썬'))  # 오른쪽에서 검색
# print(b.index('파이썬'))
# print(b.index('파이선'))  # 검색어 없을때 에러
# # startswith() - 해당문자로 시작하는지 확인
# print(b.startswith('파이썬'))
# # endswith() - 해당문자로 끝나는지 확인
# c="abc.exe"
# print(c.endswith('exe'))

# # 공백제거
# # strip() - 공백제거
# # rstrip() - 오른쪽 공백제거
# # lstrip() - 왼쪽 공백제거

# input1=input("enter name>>").strip() # 문자열 앞뒤로 공백이 있으면 다른 문자열로 취급됨
# if 'Hong'==input:
#     print('맞습니다',input1)
# else:
#     print('틀립니다',input1)

# # replace() - 문자열 변경 replace('a','b'):'a'를 'b'로 변경
# a="홍길동은 키가 180, 홍길동은 몸무게가 70, 홍길동이 사는 곳이 서울입니다."
# print(a.replace('홍길동','홍길자'))
# # replace(" ",""): " "을 ""로 변경 - 문자열 사이의 공백제거


# # join() - 문자열 결합
# ss="."
# print(ss.join('python'))


# # split() - 문자열 분리 : 리스트로 분리 해줌
# a='1,Hong,100,100,100,300,100.0'
# title=["No.","name","Kor","Eng","Math","T.sum","Avg"]

# print(*title,sep='\t') # sep 사이 간격출력
# a_list= a.split(",")
# print(*a_list,sep='\t')

# # print(sep:변수 사이에 모두 적용, end:마지막에 한번 적용)

# a_list=a.split(',') # ','를 기준으로 분리
# print(a_list)
# b='Hong Yuu Lee Kim'
# b_list= b.split(' ')
# print(b_list)

# map() - 리스트를 입력받아 처리하는 함수
# map(function함수,list데이터)

# isdigit() : 숫자인지 확인
# isalpha() : 문자(영,한) 확인
# isalnum() : 문자(영,한),숫자인지 확인
# ispper() : 대문자인지 확인
# islower() : 소문자인지 확인

# 국어점수를 입력하시오
while True:
    kor=input("input kor score>>")
    if kor.isdigit():
        
        break

    else:
        print("try again, type number")

print(int(kor))

# def multi(x):
#     return x**2
# a=[1,2,3]
# b=list(map(multi,a))
# print(a)
# print(b)


# a=["100","90","80"]
# b=[]
# for i in a:
#     print(b.append(int(i)))

# print(a)
# print(b)

# a=["100","90","80"]
# b=list(map(int,a)) # map타입 객체로 저장;list타입으로 반드시 변환해야함.
# print(a)
# print(b)



# # 문자열 슬라이싱
# a='hello'
# # "ll"출력
# print(a[2:4])
# print('hello'*3) # 3회 반복 출력
# print('hello'+'안녕')# 연결연산자