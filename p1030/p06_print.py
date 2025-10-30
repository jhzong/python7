stu_list=[
    ["Hong",80,80,80,240,80.00],
    ["Yuu",90,90,90,270,90.00],
    ["lee",100,100,100,300,100.00]  
]
title=["name","Kor","Eng","Math","T.sum","Avg"]
print("-"*50)
print(" "*15,"[grade editor]")
print("-"*50)
print("1. grade recorder")
print("2. grade printer")
print("-"*50)
choice=int(input("select menu>>"))
print()
#-------------------printing grade----------------
print(" "*15,"[list]")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
print("-"*50)
for stus in stu_list:
    print("{}\t{}\t{}\t{}\t{}\t{}\t".format(*stus))