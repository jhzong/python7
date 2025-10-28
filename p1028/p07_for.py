# for문
# 구조 - for 변수 in 범위(range,list,문자열):

# 1~5 for
# 숫자를 입력받아, 입력 받은 값을 출력하는 것을 5번 반복

# for i in range(5):
#     num=input("type a number>>")
#     print("{} no. you typed {}".format(i+1,num))

# sum=0
# for i in range(5):
#     num=int(input("type a number>>"))
#     sum=sum+num
#     print("{} no. you typed {}. s.total is {}".format(i+1,num,sum))

# print("total : {}".format(sum))

# 1~10 합
sum=0
for i in range(1,11):
    sum=sum+i

print(sum)








# a_list =[]
# sum=0
# for i in range(10):
#     num=int(input("type a number>>"))
#     if num%2==0:
#         break # 반목분을 중단시키는 명령어
#     a_list.append(num)
#     sum=sum+num

# print("list :",a_list,"sum :",sum)


