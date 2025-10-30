
# for/while문
# for 변수 in 범위:
# while 조건:

# for i in range(10):
#     print(i)

# i=0             # 초기값
# while i<10:     # 조건식 - 조건이 맞을 동안 계속 실행
#     print(i)
#     i=i+1       # 증감식


i=1
while(i!=0):
    i=int(input("type(type 0 to terminate)>>"))
    print("you entered>>",i)

print("[program terminated]")
pass

num=1
for _ in range(100000):  # for문에서 실질적 무한시행이 없기 때문에 범위는 되도록 큰게 설정
    if num==0:break
    num=int(input("type(type 0 to terminate)>>"))
    print("you entered>>",num)
print("[program terminated]")