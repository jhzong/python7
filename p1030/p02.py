import random
# 3x3 list 출력
a_list=list(range(1,10))
print(a_list)


for a in a_list:
    print(a,end="\t")
    if a%3==0:
        print()
#rdm 섞기
print(a_list)
random.shuffle(a_list)


#무한실행
while True:
    print("[좌표 맞추기 게임]")
    print("-"*30)
    for idx,a in enumerate(a_list):
        print(a,end="\t")
        if (idx+1)%3==0:
            print()
    print("-"*30)
    num=int(input("원하는 번호를 입력하시오>>"))
    # 9번 입력 받으면 9번 자리가 X가 됨
    for idx,a in enumerate(a_list):
        if a==num:
            a_list[idx]="X"
            
            
