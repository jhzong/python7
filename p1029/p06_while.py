n_list=[]
i=0
while True:
    if i<4:
        name=input("{}. type name>>".format(len(n_list)+1))
        kor=int(input("{}. type Kor score>>".format(len(n_list)+1)))
        eng=int(input("{}. type Eng score>>".format(len(n_list)+1)))
        math=int(input("{}. type Math score>>".format(len(n_list)+1)))
        sum=kor+eng+math
        avg=sum/3
        n_list.append([name,kor,eng,math,sum,avg])
        print(n_list)
    else:
        break
    i=i+1
    
# print all
print("name\tKor\tEng\tMath\tSum\tAvg")
print("-"*50)
for i in range(len(n_list)):
    print("{}\t{}\t{}\t{}\t{}\t{}".format(*n_list[i]))