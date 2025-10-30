stu_list=[
    ["Hong",80,80,80,240,80.00],
    ["Yuu",90,90,90,270,90.00],
    ["lee",100,100,100,300,100.00]  
]
title=["name","Kor","Eng","Math","T.sum","Avg"]

# print(stu_list[1][0])
# print(stu_list[2][0])
# print(stu_list[3][0])

# for i in range(3):
#     print(stu_list[i][0])

# Hong
# Yuu
# Lee
## stu_list를 이용
while True:
    print("[ Delete rocord ]")
    for idx,stus in enumerate(stu_list):
        # print("{}\t{}".format(stus[0],stus[1]))
        print("{}.{}\t{}\t{}\t{}\t{}\t{}\t".format(idx+1,*stus))
    print("-"*50)
#---------------------------del record    
    num=int(input("enter number for deletion>>"))
    del stu_list[num-1]

    print(stu_list)
