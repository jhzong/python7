# 로또
# 로또번호 3개를 자동 추출로 입력받아
# 몇개가 맞는지 출력

import random

a_list=[]
answer=[]
lotto=random.sample(range(1,46),6)
lotto.sort()
print(lotto)
count=[]

for i in range(6):
    auto=random.sample(range(1,46),5)
    auto.sort()
    a_list.append(auto)

for a in a_list:
    print(a)

# auto=random.sample(range(1,46),6)
# print(auto)

for a in a_list:
    for i in a:
        if i in lotto:
            answer.append(i)
            count+=len(answer)
print(answer,f"{count}개 맞춤")

# for a in auto:
#     if a in lotto:
#         answer.append(a)
#         count+=len(answer)

# print(answer,f"{count}개 맞춤")

# 번호비교함수
def cal():
    for auto in a_list:
        count=0
        for a in auto:
            if a in lotto:
                count+=1
count.append(count)