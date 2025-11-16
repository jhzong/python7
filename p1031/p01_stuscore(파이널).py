import random
stu_list=[
    [10101,"Hong",80,80,80,240,80.00],
    [10102,"Yuu",90,90,90,270,90.00],
    [10103,"lee",100,100,100,300,100.00]
]
stu_count=10104
title=["No.","name","Kor","Eng","Math","T.sum","Avg"]

while True:
    print("*"*36)
    print("[Student Score Recording Program 1.0]")
    print("*"*36)
    print("<menu>","-"*29)
    print("1. input")
    print("2. list")
    print("3. edit")
    print("4. delete")
    print("0. terminate program")
    print("-"*36)
    m=int(input("select menu>>"))
    print()

    if m==1: #입력
        print("<input>")
        print("-"*36)
        name=input("name of stu no.{}>>".format(stu_count))
        kor=int(input("input Kor score>>"))
        eng=int(input("input Eng score>>"))
        math=int(input("input Math score>>"))
        sum=kor+eng+math
        avg=sum/3
        
        stu_list.append([stu_count,name,kor,eng,math,sum,avg])
        stu_count=stu_count+1
        print("-"*36)
        print("input complete")
        print("-"*36)
        print()
        
    elif m==2: #출력
        print("<record list>")
        print("-"*36)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*36)
        for i in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*i))
            print()
    
    elif m==3: #수정
        print("<edit>")
        print("-"*36)
        print()
        print("student list")
        print("-"*36)
        print("{}.\t{}\t{}".format("idx",title[0],title[1]))
        print("-"*36)
        for idx,s in enumerate(stu_list):          # idx와 번호,이름 리스트 출력
            print("{}.\t{}\t{}".format(idx+1,s[0],s[1]))
        e=int(input("select student(idx no.)>>"))  # 학생(e)을 선택
        
        print("editing {}'s score".format(stu_list[e-1][1]))
        print("1. Kor")
        print("2. Eng")
        print("3. Math")
        sj=int(input("select subject>>"))  # 과목(sj)을 선택
        print("{}'s {} score : {}".format(stu_list[e-1][1],title[1+sj],stu_list[e-1][1+sj]))
        ns=int(input("input new score>>")) # 새로운 성적(ns)을 입력
        stu_list[e-1][1+sj]=ns             # 수정된 성적에 맞춰 합계와 평균 계산 후 수정
        stu_list[e-1][5]=stu_list[e-1][2]+stu_list[e-1][3]+stu_list[e-1][4]
        stu_list[e-1][6]=stu_list[e-1][5]/3
        print("changing {}'s {} score to {}".format(stu_list[e-1][1],title[1+sj],ns))
        
        print(stu_list)
        print()
    
    elif m==4: #삭제
        print("<delete>")
        print("-"*36)
        print("record list")
        print("-"*36)
        print()
        print("{}.\t{}\t{}".format("idx",title[0],title[1]))
        print("-"*36)
        for idx,s in enumerate(stu_list):          # idx와 번호,이름 리스트 출력
            print("{}.\t{}\t{}".format(idx+1,s[0],s[1]))
            
        d=int(input("to delete data press the idx no.>>")) # 번호 d를 눌러 삭제 지시(d=idx+1)
        cfm=int(input("deleting {} {}'s record. are u sure?(1.Y/2.N)"\
            .format(stu_list[d-1][0],stu_list[d-1][1]))) # d로 선택한 학생의 데이터를 지울지 확인
        if cfm==2:      # 취소
            print()
            print("deletion canceled...")
            print()
            continue
        
        del stu_list[d-1]
        print("deletion complete")
        print()
        print(stu_list) #test용
    
    elif m==0: #종료
        print("*"*25)
        print("terminating program...")
        print("*"*25)
        break












# # student score record
# while True:
#     print("-"*50)
#     print(""*10,"Student test score record")
#     print("-"*50)
#     print("1. record score")
#     print("2. print record")
#     print("3. edit score")
#     print("4. delete score")
#     print("0. exit record")
#     print("-"*50)
#     choice=int(input("select menu>>"))
    
#     if choice==1:    # record
#         print("<< record score >>")
#         name=input("No.{} name>>".format(stu_count))
#         kor=int(input("Kor score>>"))
#         eng=int(input("Eng score>>"))
#         math=int(input("Math score>>"))
#         T_sum=kor+eng+math
#         avg=T_sum/3
        
#         stu_list.append([stu_count,name,kor,eng,math,T_sum,avg])
#         stu_count=stu_count+1
#         print("record complete.")
#         print()
        
#     elif choice==2:  # print
#         print("<< printing record >>")
#         print(" "*10,"student record list" )
#         print("-"*50)
#         print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
#         print("-"*50)   
#         for stus in stu_list:
        
#             print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*stus))# format 구성원 갯수 맞추기**
#         print()
        
#     elif choice==3:  # edit
#         print("<< edit score >>")
#         print(" "*10,"student record list" )
#         print("-"*50)
#         for idx, stus in enumerate(stu_list):
#             print("{}.{}\t{}".format(idx+1,stus[0],stus[1]))
#         print("-"*50)
#         choice=int(input("number for editing>>"))
        
#         print("[selecting {} for edit]".format(stu_list[choice-1][1]))
#         print("1. Kor")
#         print("2. Eng")
#         print("3. Math")
#         print("-"*50)
#         subject=int(input("enter subject code>>"))
#         # 0=choice-1 [10101,"Hong",80(1+1),80,80,240,80.00]
#         print("-"*50)
#         print("{} score : {} ".\
#             format(title[subject+1],stu_list[choice-1][subject+1]))
#         print("-"*50)
#         score=int(input("enter new score>>"))
#         stu_list[choice-1][subject+1]=score
#         stu_list[choice-1][5]=stu_list[choice-1][2]+\
#             stu_list[choice-1][3]+stu_list[choice-1][4]
#         stu_list[choice-1][6]=stu_list[choice-1][5]/3
        
#         print("{}'s score is edited to {}.".\
#             format(title[subject+1],score))
        
        
#         print(stu_list) # test
#         print()
        
#     elif choice==4:  # delete
#         print("<< 성적 삭제 >>")
#         print(" "*10,"학생 성적" )
#         print("-"*50)
#         for idx, stus in enumerate(stu_list):
#             print("{}.{}\t{}".format(idx+1,stus[0],stus[1]))
#         print("-"*50)
# #---------------------------del record------------------
#         choice=int(input("삭제 번호>>"))#???
# #---------------------------취소----------------------------
#         confirm=int(input("{} {} 기록을 삭제합니다.(1.Y/2.N)>>".\
#             format(stu_list[choice-1][0],stu_list[choice-1][1])))
#         if confirm==2:
#             print("삭제 취소.")
#             continue
# #---------------------------del ------------------------ 
#         del stu_list[choice-1]
#         print("삭제 완료")
#         print()
#         print(stu_list)
        
#     elif choice==0:
#         print("<<Terminating program>>")
#         print()
#         break