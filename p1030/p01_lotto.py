# 1.변수선언
import random
lotto=[] # 로또번호list
c_list=[] # 입력번호 list
s_list=[] # 맞춘번호 list

# 2.6개의 번호생성
lotto=random.sample(range(1,46),6)
lotto.sort()
print(lotto) # test

# 3.6개의 번호입력
# for i in range(6):
#     c=int(input("enter ur {} choice>>".format(i+1)))
#     c_list.append(c)
# c_list.sort()
i=0
while i<6:
    c=int(input("enter ur {} choice>>".format(i+1)))
    # if not c.isdigit(): # 해당 변수가 "str"이여야 함
    #     print("U can type numbers only...")
    # else:
        
    if 1<=c<=45:
        c_list.append(c)
        i=i+1
    else:
        print("invalid number try again...")
# print(C) # test

# 4.번호확인
# for i in lotto:
#     for j in c_list:
#         if i==j:
#             s_list.append(j)
#             break
for i in c_list:
    if i in lotto:
        s_list.append(i)
s=len(s_list) # 맞춘 갯수
# print(s) # test

# 5.결과출력
print("Lucky number are",lotto)
print(f"U scored {s}!",s_list)

if s==0 or s==1:
    print("Better luck next time...")
elif s==2:
    print("Congrats! U won 5th prize!")
elif s==3:
    print("Congrats! U won 4th prize!")
elif s==4:
    print("Congrats! U won 3rd prize!")
elif s==5:
    print("Congrats! U won 2nd prize!")
else:
    print("JACKPOT!!!")
