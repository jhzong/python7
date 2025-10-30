# a_list=[1,2,3,4,5,6,7,8,9]
# b_list=[list(range(1,10))]
# c_list=[i for i in range(1,10)]
# print(a_list)
# print(b_list)
# print(c_list)

# appenad, insert, extend
# pop, del, remove, clear
# 수정 : a_list[idx]=값
# index : 해당위치값 리턴
aa_list=[10,5,15,7,9]
print(aa_list.index(10))

# # 1.비교(enumerate)
# print(aa_list)
# num=int(input("enter>>"))
# for idx, aa in enumerate(aa_list):
#     if aa==num:
#         aa_list[idx]="X"
# print(aa_list)

# # 2.비교(in)
# print(aa_list)
# num=int(input("enter>>"))
# if num in aa_list:
#     aa_list[aa_list.index(num)]="X"

# print(aa_list)

import random
# 1~25 rdm list 5x5 2d(???)
a_list=list(range(1,26))

# shuffle list in rdm
random.shuffle(a_list)
print(a_list)

while True:
# print 5x5 grid with rdm list
    print("<<bingo>>")
    print("-"*40)
    for idx, a in enumerate(a_list):
        print(a,end="\t")
        if(idx+1)%5==0:
            print() 
    print("-"*40)
    num=int(input("enter a number>>"))
    print()

# compare numbers
    if num in a_list:
        a_list[a_list.index(num)]="X"
    # for idx,a in enumerate(a_list):
    #     if num==a:
    #         a_list[idx]="X"
    #         break