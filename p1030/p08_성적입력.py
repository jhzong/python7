import random
stu_list=[
    [1,"Hong",80,80,80,240,80.00],
    [2,"Yuu",90,90,90,270,90.00],
    [3,"lee",100,100,100,300,100.00]  
]
stu_count=4
title=["No.","name","Kor","Eng","Math","T.sum","Avg"]

# student score record
while True:
    print("-"*50)
    print(""*10,"Student score record")
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
    elif choice==2:  # print
        print("<< print record >>")
    elif choice==3:  # edit
        print("<< edit score >>")
    elif choice==4:  # delete
        print("<< delete score >>")
    elif choice==0:
        print("<<Terminating record>>")
        print()
        break