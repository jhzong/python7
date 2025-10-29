# ## 1~10 sum
# #for
# s=0
# for i in range(1,11):# 범위내에서 i는 자동증가
#     s=s+i
    
# print(f"sum of 1 to 10 is {s}")

# #while
# s=0
# i=1                  # 초기값
# while i<11:          # 조건문
#     s=s+i
#     i=i+1            # 증감식(수동증가)
# print(f"sum of 1 to 10 is {s}")

# ## sum of numbers entered 5 times
# # for
# s=0
# for _ in range(5):
#     n=int(input("type>>"))
#     s=s+n

# print(f"sum of 5 numbers >> {s}")

# #while
# s=0
# i=0
# while i<5:
#     n=int(input("type>>"))
#     s=s+n
#     i=i+1

# print(f"sum of 5 numbers >> {s}")

# while

stu_list=[]
while True:
    print("[학생성적프로그램]")
    print("1. 성적입력")
    print("2. 성적출력")
    print("3. 성적수정")
    print("0. 종료")
    print("-"*20)
    choice=int(input("type>>"))
    if choice==0: break
    elif choice==1:
        print("[학생성적입력]")
        name=input("enter name>>")
        kor=int(input("enter Kor score>>"))
        eng=int(input("enter Eng score>>"))
        math=int(input("enter Math score>>"))
        sum=kor+eng+math
        avg=sum/3

        info=[name,kor,eng,math,sum,avg]
        stu_list.append(info)

        print("[leaderboard]")
        print("name\tKor\tEng\tMath\tSum\tAvg")
        print("-"*50)
        for i in range(len(stu_list)):
            print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*info)) # 전개연산자
    elif choice==2:
        print("[학생성적출력]")
    elif choice==3:
        print("[학생성적수정]")
    print()


print(stu_list)
