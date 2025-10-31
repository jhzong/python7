import random
stu_list=[
    [10101,"Hong",80,80,80,240,80.00],
    [10102,"Yuu",90,90,90,270,90.00],
    [10103,"lee",100,100,100,300,100.00]
]
stu_count=10104
title=["No.","name","Kor","Eng","Math","T.sum","Avg"]

# student score record
while True:
    print("-"*50)
    print(""*10,"Student test score record")
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
        name=input("No.{} name>>".format(stu_count))
        kor=int(input("Kor score>>"))
        eng=int(input("Eng score>>"))
        math=int(input("Math score>>"))
        T_sum=kor+eng+math
        avg=T_sum/3
        
        stu_list.append([stu_count,name,kor,eng,math,T_sum,avg])
        stu_count=stu_count+1
        print("record complete.")
        print()
        
    elif choice==2:  # print
        print("<< printing record >>")
        print(" "*10,"student record list" )
        print("-"*50)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*50)   
        for stus in stu_list:
        
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stus))# format 구성원 갯수 맞추기**
        print()
        
    elif choice==3:  # edit
        print("<< edit score >>")
        print(" "*10,"student record list" )
        print("-"*50)
        for idx, stus in enumerate(stu_list):
            print("{}.{}\t{}".format(idx+1,stus[0],stus[1]))
        print("-"*50)
        choice=int(input("number for editing>>"))
        
        print("[selecting {} for edit]".format(stu_list[choice-1][1]))
        print("1. Kor")
        print("2. Eng")
        print("3. Math")
        print("-"*50)
        subject=int(input("enter subject code>>"))
        # 0=choice-1 [10101,"Hong",80(1+1),80,80,240,80.00]
        print("-"*50)
        print("{} score : {} ".\
            format(title[subject+1],stu_list[choice-1][subject+1]))
        print("-"*50)
        score=int(input("enter new score>>"))
        stu_list[choice-1][subject+1]=score
        stu_list[choice-1][5]=stu_list[choice-1][2]+\
            stu_list[choice-1][3]+stu_list[choice-1][4]
        stu_list[choice-1][6]=stu_list[choice-1][5]/3
        
        print("{}'s score is edited to {}.".\
            format(title[subject+1],score))
        
        
        print(stu_list) # test
        print()
        
    elif choice==4:  # delete
        print("<< 성적 삭제 >>")
        print(" "*10,"학생 성적" )      
        print("-"*50)
        for idx, stus in enumerate(stu_list):
            print("{}.{}\t{}".format(idx+1,stus[0],stus[1]))
        print("-"*50)
#---------------------------del record------------------
        choice=int(input("삭제 번호>>"))#???
#---------------------------취소----------------------------
        confirm=int(input("{} {} 기록을 삭제합니다.(1.Y/2.N)>>".\
            format(stu_list[choice-1][0],stu_list[choice-1][1])))
        if confirm==2:
            print("삭제 취소.")
            continue
#---------------------------del ------------------------ 
        del stu_list[choice-1]
        print("삭제 완료")
        print()
        print(stu_list)
        
    elif choice==0:
        print("<<Terminating program>>")
        print()
        break