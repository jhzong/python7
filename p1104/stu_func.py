# 함수를 여기에 생성

# 함수내에서 사용할때 단순/복합변수에 따라 호출방식 달라짐
# 단순변수 : global
# 복합변수 호출해서 변형가능

title=["No.","name","Kor","Eng","Math","T.sum","Avg","Rank"]
stu_list=[
    [10101,"Hong",80,80,80,240,80.00,0],
    [10102,"Yuu",90,90,90,270,90.00,0],
    [10103,"lee",100,100,100,300,100.00,0]
]
stu_count=10104

# stu_list=[
#     {'stu_no':10101,'name':'Hong','kor':80,'eng':80,'math':80,'sum':240,'avg':80.00,'rank':0}
#     {'stu_no':10102,'name':'Yuu','kor':90,'eng':90,'math':90,'sum':270,'avg':90.00,'rank':0}
#     {'stu_no':10103,'name':'Lee','kor':100,'eng':100,'math':100,'sum':300,'avg':100.00,'rank':0}
# ]

# main menu 함수
def screen_print():
    print("-"*50)
    print(""*10,"Student test score record")
    print("-"*50)
    print("1. record score")
    print("2. print record")
    print("3. edit score")
    print("4. delete score")
    print("5. apply rank")
    print("0. exit record")
    print("-"*50)
    
# 1.성적입력합수
def stu_input():
    global stu_count # 전역(global)변수 사용
    print("<< record score >>")
    name=input("No.{} name>>".format(stu_count))
    kor=int(input("Kor score>>"))
    eng=int(input("Eng score>>"))
    math=int(input("Math score>>"))
    T_sum=kor+eng+math
    avg=T_sum/3
    
    stu_list.append([stu_count,name,kor,eng,math,T_sum,avg,0])
    stu_count=stu_count+1
    print("record complete.")
    print()


# 2.성적출력함수   
def stu_print():
    print("<< printing record >>")
    print(" "*10,"student record list" )
    print("-"*50)
    print(*title,sep="\t")
    print("-"*50)   
    for stus in stu_list:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*stus))# format 구성원 갯수 맞추기**
    print()


# 3.성적수정함수
def stu_modify():
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
        
# 5.기록삭제함수
def stu_delete():
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
            return # 함수 중간에서 종료시 return, 반복문 중간에서 종료시 continue
#---------------------------del ------------------------ 
        del stu_list[choice-1]
        print("삭제 완료")
        print()
        print(stu_list)
    
# 5.등수처리함수
def stu_rank():
    for s1 in stu_list:
        count=1
        for s2 in stu_list:
            if s1[5]<s2[5]:
                count+=1
        s1[7]=count
    print("rank applied")
