stu_list=[]
while True:
# 반복시작
    print("[score input]")
    name=input("enter name>>")
    kor=int(input("enter Kor score>>"))
    eng=int(input("enter Eng score>>"))
    math=int(input("enter Math score>>"))
    sum=kor+eng+math
    avg=sum/3

    info=[name,kor,eng,math,sum,avg]
    stu_list.append(info)

    print("name\tKor\tEng\tMath\tSum\tAvg")
    print("-"*50)
    #print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name,kor,eng,math,sum,avg))
    print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(*info)) # 전개연산자

    print(stu_list)

