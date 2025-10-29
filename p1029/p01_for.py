# for 변수 in 범위: # 문법, 그냥 외우기
# pass - 공백
# break - break 이후로 반복문 종료
# continue - 1회 반복문 skip


# for i in range(10):
#     pass # 아무것도 일어나지 않음 - 빈공백(에러 방지)
#   # break # break가 있는 시점부터 반복문 종료 
# print("프로그램 종료")

# 홀수 출력
# for i in range(10):
#     if i%2==0:
#         continue
#     print(i)

# 짝수 출력
# for i in range(10):
#     if i%2==0:
#         print(i)
#         continue

# for i in range(2,9): #7
#     print(f"{i}")
#     for j in range(1,10): #9
#         pass
#         print("-"*50)
#         #print(f"number : {j}")

# for i in range(2,10):
#     print(i,end=" ")
# print()

# # 5~21    
# for i in range(5,22):
#     print(i,end=" ")
# print()
    
# # 1~10
# for i in range(1,11):
#     print(i,end=" ")
# print()
    
# # 0~9, odd
# for i in range(10):
#     if i%2!=0:
#         print(i,end=" ")
#         continue
    
# # 9x9단
# for i in range(1,10):
#     print(f" [ {i}단 ] ")
#     for j in range(1,10):
#         print(f"{i} x {j} = {i*j}")
#     print()
        
# for i in range(1,10):
#     if i%2==0:continue
#     print(f" [ {i}단 ] ")
#     for j in range(1,10):
#         print(f"{i} x {j} = {i*j}")

# names=["Hong","Yuu","Lee","Kim","Kang"]
# # for 변수 in 범위(range,list,str,dict,tuple):

# for name in names:
#     print(name)
    
# for idx,name in enumerate(names): # idx와 값을 리턴
#     print(f"{idx+1}.{name}")
    
# n_list=[
#     [1,"Hong"],
#     [2,"Yuu"],
#     [3,"Lee"]
# ]
# for ns in n_list:
#     for n in ns:
#         print(n)
        
# 0이 10개 들어가는 list

# append 추가
a_list=[]
for i in range(10):
    a_list.append('0')
print(a_list)

# list 타입 변환
a_list=list('0'*10)
print(a_list)

# list 내포
a_list=['0' for i in range(10)]
print(a_list)

a_list=[i*i for i in range(1,10)]
print(a_list)