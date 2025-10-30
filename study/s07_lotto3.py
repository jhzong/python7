# 1. 변수선언
import random
C=[]  # Choice - 내가 선택한 번호 list
S=[]  # Score - 내가 맞춘 번호 list

# 2. 로또번호추출
lotto=random.sample(range(1,46),6) # random.sample(range(x,y),z)를 이용해 x<=n<y범위의
lotto.sort()                       # 무작위값 6개(중복X) 추출 후 lotto(list)에 추가
print(lotto) # test용

# 3. 번호선택
# for i in range(6):  # for문 사용 - 0부터 5까지 6번 시행
#     c=int(input("make ur choice>>"))
#     C.append(c)

i=0
while i<6:          # while문 사용 - i<6인 동안 반복함
    c=int(input(f"make ur {i+1} choice>>"))
    if 1<=c<=45:
        C.append(c)
        i=i+1
    else:
        print("invalid number try again...")

C.sort()

# 4. 맞춰보기
# for i in lotto:        # for문 2번 사용
#     for j in C:
#         if i==j:
#             S.append(j)
#             break

for i in C:             # for문 1번 사용
    if i in lotto:      # 만약(if) i가 lotto 안에(in) 있다면?
        S.append(i)

s=len(S)

# 5. 결과출력
print("lucky numbers :",lotto)
print(f"U scored {s}!",S)

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
    print("JACKPOT!!")
