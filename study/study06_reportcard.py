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
