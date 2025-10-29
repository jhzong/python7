# 1. 변수선언/로또번호 추출
import random
lotto=[]
m_num=[]
score=[]
lotto=random.sample(range(1,46),6)
lotto.sort()
print(lotto)

# 2. 무작위숫자 입력
for i in range(6):
    n=int(input("enter ur choice>>"))
    m_num.append(n)
m_num.sort()
# print(m_num)

# 3. 당첨 확인
for i in lotto:
    for j in m_num:
        if i==j:
            score.append(j)
            break
s=len(score)
# print(score)

# 4. 결과 출력
print(lotto)
print(f"U scored {s}!",score)

# 5. 당첨상품 출력
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
    print("!!!JACKPOT!!!")