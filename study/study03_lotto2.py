#1.변수선언,로또번호추출
import random
C=[]
S=[]
lotto=random.sample(range(1,46),6)
lotto.sort()
# print(lotto) # test print
#2.나의선택
for i in range(6):
    c=int(input("enter ur choice>>"))
    C.append(c)
C.sort()

#3.맞춰보기
for i in lotto:
    for j in C:
        if i==j:
            S.append(j)
            break
s=len(S)

#4.결과값출력
print("lucky number is",lotto)
print(f"U scored {s}!",S)

#5.상품결과출력
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
    
# 9x9단
for i in range(1,10):
    print(f"[ {i}단 ]")
    for j in range(1,10):
        print(f"{i} X {j} = {i*j}",end="  ")
    print(end="\n\n")

# 3x3 수열
for i in range(9):
    print(i,end="\t")
    if (i+1)%3==0:
        print()

# 4x4 수열
for j in range(16):
    print(j,end="\t")
    if (j+1)%4==0:
        print()