# a_list=[1,2,3,4,5,6,7,8,9]
# print(a_list)
# b_list=list(range(1,10))
# print(b_list)
# c_list=[i for i in range(1,10)]
# print(c_list)

# d_list=['0','0','0','0','0','0','0','0','0']
# print(d_list)
# e_list=list('0'*9)
# print(e_list)
# f_list=['0'for i in range(9)]
# print(f_list)

## 3x3 list
# a_list=list(range(1,10))
# b_list=[]
# # 1 2 3
# # 4 5 6
# # 7 8 9


# # print(a_list)
# for i in a_list:
#     print(i,end="\t")
#     if i%3==0:
#         print()

# 4x4 list
# a_list=list(range(1,17))

# for i in a_list:
#     print(i,end="\t")
#     if i%4==0:
#         print()
# # 1       2       3       4
# # 5       6       7       8
# # 9       10      11      12
# # 13      14      15      16  

# # 5x5 list
# b_list=list(range(1,26))
# for i in b_list:
#     print(i,end="\t")
#     if i%5==0:
#         print()
# # 1       2       3       4       5
# # 6       7       8       9       10
# # 11      12      13      14      15
# # 16      17      18      19      20

# 3x3 list
# a_list=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(a_list[0])

# # 3x3
# for aa in a_list: # [1,2,3]     [4,5,6]     [7,8,9]
#     for a in aa:
#         print(a,end="\t")
#     print()

## rdm 3x3
# a_list=[9,1,2,5,6,8,3,4,7]
# for idx,value in enumerate(a_list):
#     print(value,end="\t")
#     if (idx+1)%3==0:
#         print()

# rdm 4x4
import random

a_list=list(range(1,17))
random.shuffle(a_list)
print(a_list)

for i,v in enumerate(a_list):
    print(v,end="\t")
    if (i+1)%4==0:
        print()
