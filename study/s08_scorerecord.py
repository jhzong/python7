# 성적입력 프로그램
import random
stu_list=[]
stu_count=10101
title=["No.","name","Kor","Eng","Math","T.sum","Avg"]
#-------------------메뉴창---------------------
while True:
    print("-"*30)
    print("[TEST SCORE RECORDER 1.0]")
    print("-"*30)
    print("\t<MENU>\t")
    print("-"*30)
    print("1. score input")          #입력
    print("2. score list")           #출력
    print("3. score edit")           #수정
    print("4. delete record")        #삭제
    print("0. terminate program")    #종료
    print("-"*30)
    m=int(input("select menu>>"))

#-------------------입력창---------------------
    if m==1:    
        print("-"*30)
        print("\t<score input>\t")
        print("-"*30)
        name=input("input name of stu_No.{}>>".format(stu_count))  # 정보입력
        kor=int(input("input Korean score>>"))
        eng=int(input("input English score>>"))
        math=int(input("input Math score>>"))
        T_sum=kor+eng+math
        avg=T_sum/3
        
        info=[stu_count,name,kor,eng,math,T_sum,avg]
        stu_list.append(info)                              # stu_list라는 list에 info라는 list 추가
        stu_count=stu_count+1
        print("recording complete")
    
        print(stu_list) #test용

#-------------------기록창---------------------    
    elif m==2:
        print("-"*50)
        print("\t<score list>\t")
        print("-"*50)
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        print("-"*50)
        for info in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*info))
        print()

#-------------------수정창---------------------        
    elif m==3:
        pass

#-------------------삭제창---------------------
    elif m==4:
        pass

#-------------------종료창---------------------
    elif m==0:
        print("\t<terminating program>\t")
        print()
        break



