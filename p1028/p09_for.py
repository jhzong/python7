# for 변수 in 범위:
# for i in range(10): #[0,1,2,3,4,5,6,7,8,9]
#     print(i,end=" ") # end=""가 없으면 자동으로 \n되어 출력
    
# sum=0
# for i in range(1,101):
#     sum=sum+i

# print("total is",sum)

# 천을 넘는 위치는 얼마를 더할때 일까요?
# sum=0
# for i in range(1,101):
#     sum=sum+i
#     print(i,sum)
#     if sum > 100:
#         break

# print(f"{i}번째 : {sum}")


# 1*2*3*4*...*10
result=1
for i in range(1,11):
    result=result*i
    print(i,result)
    if result>100:
        break
print(f"{i} round, result is {result}")


