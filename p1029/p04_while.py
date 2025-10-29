print("[score input]")
name=input("enter name>>")
kor=int(input("enter Kor score>>"))
eng=int(input("enter Eng score>>"))
math=int(input("enter Math score>>"))
sum=kor+eng+math
avg=sum/3
# print("name:{}".format(name))
# print("Kor:{}".format(kor))
# print("Eng:{}".format(eng))
# print("Math:{}".format(math))
# print("Sum:{}".format(sum))
# print("Avg:{:.2f}".format(avg))

# print("name:{:s}\nKor:{:d}\nEng:{:d}\nMath:{:d}\nSum:{:d}\nAvg:{:.2f}"\
#     .format(name,kor,eng,math,sum,avg))

print("name\tKor\tEng\tMath\tSum\tAvg")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name,kor,eng,math,sum,avg))