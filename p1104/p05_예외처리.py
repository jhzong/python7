# 예외처리 - 오류(에러)가 나도 프로그램을 종료하지 않고 계속 실행시키는 실행

# 오류(error) 구문/런타임 오류
a=10
print(a)
# prin(a) 구문오류 - 오타
#         실행전 미리 알려줌(맞춤법 느낌)

a_list=[1,2,3]
print(a_list[0])

# 예외처리 - try 이후 에러발생 시 에러 위치에서 except 이후로 이동
#          외부연결 : 파일 입/출력, 파일 읽기/쓰기, 프린터 연결, db연결
try:
    print(a_list[100]) # 실행을 해야 알수 있음 - 런타임오류
except Exception as e:
    print("error :",e)


print("ending program")



print(1)
print(2)
try:
    print(3)
    print(4)
    # 에러
    raise SyntaxError # 강제 에러발생 명령어
    print(5)
except: # 에러 발생시에만 실행됨
    print(6)
finally: # 에러 발생 유무에 상관없이 실행
    print(7)
print(8)