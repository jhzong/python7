import random
# 1. 변수 선언
count=0
my_pick=[]
cor_pick=[]
# 2. 1~45 6개의 랜덤숫자를 출력
lotto=random.sample(range(1,46),6)
lotto.sort()
print(lotto)

# 3. 6개의 숫자를 입력받아 출력
for i in range(6):
    my_num=int(input("ur pick>>"))
    my_pick.append(my_num)
my_pick.sort()

# 4. 맞춰보기
print("result")
print(my_pick)
for i in lotto:
    for j in my_pick:
        if i==j:
            count=count+1
            cor_pick.append(j)
            break

print("you got",count,cor_pick)
# 2개 -5천 3 -5만 4개 -백만 5개 -5천만 6개 -20억

# 5.당첨금 출력
if count==0 or count==1:
    print("꽝")
elif count==2:
    print("5,000원 당첨")
elif count==3:
    print("50,000원 당첨")
elif count==4:
    print("1,000,000원 당첨")
elif count==5:
    print("50,000,000원 당첨")
else:
    print("2,000,000,000원 당첨")