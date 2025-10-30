# student score record
import random
stu_list=[]
stu_count=0
title=["No.","name","Kor","Eng","Math","T.sum","Avg"]

while True:
    print("-"*50)
    print(""*10,"Student score record")
    print("-"*50)
    print("1. record score")
    print("2. print record")
    print("3. edit score")
    print("4. delete score")
    print("0. exit record")
    print("-"*50)
    choice=int(input("select menu>>"))
    
    if choice==1:    # record
        print("<< record score >>")
        name=input("enter name>>")
        kor=int(input("enter Kor score>>"))
        eng=int(input("enter Eng score>>"))
        math=int(input("enter Math score>>"))
        sum=kor+eng+math
        avg=sum/3
    
        info=[name,kor,eng,math,sum,avg]
        stu_list.append(info)

        print("[Student score record]")
        print("name\tKor\tEng\tMath\tSum\tAvg")
        print("-"*50)
        for i in range(len(stu_list)):
            print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*info)) # 전개연산자
            
    elif choice==2:  # print
        print("<< print record >>")
    
    
    elif choice==3:  # edit
        print("<< edit score >>")
    
    
    elif choice==4:  # delete
        print("<< delete score >>")
    
    
    elif choice==0:
        print("<<Terminating program>>")
        print()
        break