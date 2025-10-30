# a_list=[1,2,3,4,5,6,7,8,9] # len(a_list)=9
# b_list=[                   # len(b_list)=3
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# a_list[3]=100
# print(a_list)
# b_list[1][0]=100
# print(b_list)
# b_list[2][1]=50
# print(b_list)

# # 1차 리스트 출력
# for a in a_list:
#     print(a,end="\t")
# print()

# # 2차 리스트 출력 (???)
# for b in b_list:
#     print(b,end="\t")
# print()
# for bb in b:
#     print(bb,end=" ")


stu_list=[
    ["Hong",80,80,80,240,80.00],
    ["Yuu",90,90,90,270,90.00],
    ["lee",100,100,100,300,100.00]    
]

# print(stu_list[1][3])
# print(stu_list[2][0])
# stu_list[2][2]=80
# print(stu_list)

# stu_list[2][2]=80
# stu_list[2][4]=stu_list[2][1]+stu_list[2][2]+stu_list[2][3]
# stu_list[2][5]=stu_list[2][4]/3


# 0.Hong
# 1.Yuu
# 2.Lee
#--------
#수정하고 싶은 학생번호
#국어점수 변경
print(
    '''
    [수정할 학생번호]
    0.Hong
    1.Yuu
    2.Lee
    '''
)

num=int(input("enter student number>>"))
#1번 선택
#국어를 70 변경, 합계와 평균 출력
stu_list[1][1]=70
stu_list[1][4]=stu_list[1][2]+stu_list[1][2]+stu_list[1][3]
stu_list[1][5]=stu_list[1][4]/3

print(stu_list)




# if num==1:
#     n1=int(input("enter subject number"))
#     n2=int(input("enter subject number"))
#     while True:
#         stu_list[n1][n2]=

