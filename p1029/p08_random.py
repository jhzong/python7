import random
# # randrange() 1~10까지 랜덤 숫자를 3개
# for i in range(3):
#     print(random.randrange(1,11),end=" ")

# print(random.sample([1,2,3,4,5,6,7,8,9,10],5))

# 1~10
n_list=[]
r_num=random.randrange(1,101)
for i in range(10):
    my_num=int(input("enter number>>"))
    n_list.append(my_num)
    if r_num==my_num:
        print("you won")
        break
    elif r_num>my_num:
        print("higher")
    else:
        print("lower")
print("answer is",r_num)
print("you typed",n_list)