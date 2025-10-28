# 조건분 - if문

# 반복문 - 여러번 실행
# for, while

for i in range(10): # range(x) - 범위(시작,끝,스탭)
    print(i)        #            (시작<=x<끝)
                    # 문자열 슬라이싱 [시작:끝:스탭]


for _ in range(5):
    print("hello")
    
for i in range(5):
    print("no.",i+1,"hello")
    
for i in range(1,6):
    print("no.",i,"hello")
    
sum=0
for i in range(1,11):
    sum=sum+i
    print(i,"번째 소계 : ",sum)
print("합계 : ",sum)

sum=0
for i in range(1,11):
    sum=sum+i
    print("{}번째 소계 : {}".format(i,sum))
print("합계 : ",sum)


a_list=['Hong',100,90,80]
for a in a_list: # a_list[0],a_list[1],a_list[2],a_list[3]
    print(a)


# 2D list - for분 2번, 3D list - for문 3번

name="홍길동유관순이순신"
for i in name:
    print(i)



# range를 사용
for i in range(1,11):
    print(i,"번째 숫자를 입력하세요.")


for i in range(10):
    input("{} type>>".format(i+1))
    
sum=0
for i in range(10):
    num=int(input("type>>"))
    sum=sum+num
    
print("sum :",sum)