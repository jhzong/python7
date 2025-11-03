import random
stu_list=[
    [10101,"Hong",80,80,80,240,80.00],
    [10102,"Yuu",90,90,90,270,90.00],
    [10103,"lee",100,100,100,300,100.00]
]
stu_count=10104
title=["No.","name","Kor","Eng","Math","T.sum","Avg"]

def screen_print():
    print("-"*50)
    print(""*10,"Student test score record")
    print("-"*50)
    print("1. record score")
    print("2. print record")
    print("3. edit score")
    print("4. delete score")
    print("0. exit record")
    print("-"*50)
    
def stu_input():
    # 단순변수가 선언되면 함수에서는 변수를 새롭게 생성
    global stu_count #전역변수
    print("<input>")
    print("-"*50)
    name=input("name of stu no.{}>>".format(stu_count))
    kor=int(input("input Kor score>>"))
    eng=int(input("input Eng score>>"))
    math=int(input("input Math score>>"))
    sum=kor+eng+math
    avg=sum/3
    
    stu_list.append([stu_count,name,kor,eng,math,sum,avg])
    stu_count=stu_count+1
    print("-"*50)
    print("input complete")
    print("-"*50)
    print()
    print(stu_list)
    
def stu_print():
    print("<record list>")
    print("-"*50)
    print(*title,sep="\t")
    print("-"*50)
    for i in stu_list:
        print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*i))
        print()    