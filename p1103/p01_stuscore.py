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

# 입력
    if m==1:
        print("[input]")
        
        name=input("no.{} : input name>>".format(stu_count))
        kor=int(input("input Korean score>>"))
        eng=int(input("input English score>>"))
        math=int(input("input Math score>>"))
        sum=kor+eng+math
        avg=sum/3
        
        stu_list.append([stu_count,name,kor,eng,math,sum,avg])
        stu_count=stu_count+1
        
        print("input complete")
        print(stu_list)


# 출력
    elif m==2:
        print("[list]")
        
        print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*title))
        for i in stu_list:
            print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*i))

# 수정
    elif m==3:
        print("list")
        print("{}.\t{}\t{}".format(*title))
            # for idx,k in enumerate(stu_list):
            #     print("{}.\t{}\t{}".format(idx+1,))
        pass


# 삭제
    elif m==4:
        pass
# 종료
    elif m==0:
        print("terminating program...")
        break
