# # 중첩 for문
# for i in range(1,10):
#     for j in range(1,10):
#         #print(i,"*",j,"=",i*j)
#         print(" {} X {} = {} ".format(i,j,i*j))

# for i in range(1,10):
#     print("[ {}단 ]".format(i))
#     for j in range(1,10):
#         #print(i,"*",j,"=",i*j)
#         print(" {} X {} = {} ".format(i,j,i*j))




# for i in range(1,10):
#     print("[ {}단 ]".format(i))
#     for j in range(1,10):
#         #print(i,"*",j,"=",i*j)
#         print(" {} X {} = {} ".format(i,j,i*j),end=" ")
#     print()
    
    
# for i in range(1,10):
#     if i%2!=0:
#         continue # continue 1번만 skip, break:첫시점에서 중지
        
#     print("[ {}단 ]".format(i))
#     for j in range(1,10):
#         #print(i,"*",j,"=",i*j)
#         print(" {} X {} = {} ".format(i,j,i*j))

# # 중첩for문 사용해 00,01,02,03...11,12...99
# for i in range(0,10):
#     for j in range(0,10):
#         print("{}{}".format(i,j))

# for i in range(0,10):
#     for j in range(0,10):
#         print("{}{}".format(i,j),end=" ")
#     print()

# for i in range(0,10):
#     for j in range(0,10):
#         print("{}{}".format(j,i),end=" ")
#     print()
    
    
# for i in range(0,10):
#     print(f"{i}백대")
#     for j in range(0,10):
#         for k in range(0,10):
#             print("{}{}{}".format(i,j,k),end=" ")
#         print()
        
        
# # 501~1000 홀수의 합을 출력
# sum=0
# for i in range(501,1001):
#     if i%2!=0:
#         sum=sum+i
# print(sum)


# # 1~100 3의 배수의 합을 출력
# sum2=0
# for i in range(1,101):
#     if i%3==0:
#         sum2=sum2+i
# print(sum2)

fruits=['사과','배','복숭아','딸기','포도']
for fruit in enumerate(fruits):   # enumerate(리스트) - 리스트번호, 리스트값
    print(fruit)
    
for i,fruit in enumerate(fruits):  # enumerate() 함수 : index번호 리턴
    print("{}.{}".format(i+1,fruit))
    
print("[ fruit list - range]")

for i in range(len(fruits)):
    print("{}.{}".format(i+1,fruits[i]))