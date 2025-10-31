stu_list=[
    #이름,합계,등수
    ["Hong",288,0],
    ["Yuu",299,0],
    ["Lee",300,0],
    ["Kim",295,0],
    ["Kang",298,0]
    
]

for i in stu_list:
    r_count=1 #등수 계산을 위한 초기변수
    for j in stu_list:
        if i[1] < j[1]:
            r_count=r_count+1
       # 비교가 완료되는 시점     
    i[2]=r_count
print(stu_list)
            


# # 복합변수
# a=10
# aa=a
# b=[1,2,3,4]#        b와 bb가 [1,2,3,4]가 저장된 주소를 공유
# bbb=b#              얕은 복사 - b와 bbb가 list가 저장된 주소를 공유
# bb=b[:]#            깊은 복사 - b의 list를 [:]를 이용해 새로운 bb의
# ccc=[*b]#                      list 주소를 만들어 똑같은 값을 저장
# bb[0]=100   
# print(a)
# print(b)

# a=10 # 변수에는 한번에 1개의 값만 저장
# b=a
# b=20

# print(a)
# print(b)