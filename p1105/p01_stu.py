# stu
# # list형식
# stu_list=[
#     [10101,"Hong",80,80,80,240,80.00,0],
#     [10102,"Yuu",90,90,90,270,90.00,0],
#     [10103,"lee",100,100,100,300,100.00,0]
# ]

# print(stu_list[1][1])

# dictionary형식
stu_list = [
    {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
        'total':240,'avg':80.00,'rank':0},
    {'stuno':10102,'name':'유관순','kor':90,'eng':90,'math':90,\
        'total':270,'avg':90.00,'rank':0},
    {'stuno':10102,'name':'이순신','kor':100,'eng':100,'math':100,\
        'total':300,'avg':100.00,'rank':0},
]

# print(stu_list[1]['name']) # dict데이터 찾기 : dict명[list주소][항목명]

for stu in stu_list:
    print(f"{stu['stuno']}\t{stu['name']}\t{stu['kor']}\
\t{stu['eng']}\t{stu['math']}\t{stu['total']}\t{stu['avg']}\t{stu['rank']}")
