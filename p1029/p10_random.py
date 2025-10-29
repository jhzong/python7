# 로또번호 맞추기
# 1. 변수선언, 로또번호 생성
import random
lotto=[]
m_num=[]
c_num=[]
# c=0
lotto=random.sample(range(1,46),6)
lotto.sort()
print(lotto)

# 2. 숫자입력
for i in range(6):
    pick=int(input("enter ur number>>"))
    m_num.append(pick)
m_num.sort()
# print(m_num)

# 3. 당첨번호 확인
for i in lotto:
    for j in m_num:
        if i==j:
            c_num.append(j)
            # c=c+1
            break

c=len(c_num)
# 4. 결과화면 출력
print(f"u got {c} right!",c_num)

# 5. 당첨금 출력
if c==0 or c==1:
    print("better luck next time...")
elif c==2:
    print("cograts! u won 5th prize!")
elif c==3:
    print("cograts! u won 4th prize!")
elif c==4:
    print("cograts! u won 3rd prize!")
elif c==5:
    print("cograts! u won 2nd prize!")
else:
    print("JACKPOT!!!!")
