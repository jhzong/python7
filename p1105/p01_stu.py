import os
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

# stu_str=f'{stu_list[0]['stuno']},{stu_list[0]['name']},{stu_list[0]['kor']},\
# {stu_list[0]['eng']},{stu_list[0]['math']},{stu_list[0]['total']},\
# {stu_list[0]['avg']},{stu_list[0]['rank']}\n'

#----------[이미 있는 데이터 .txt파일로 옮기기]-----------------------------------
f=open('c:\\down\\aaa.txt','w')
stu_data=''
for i in range(3):
    stu_str=f'{stu_list[i]['stuno']},{stu_list[i]['name']},{stu_list[i]['kor']},\
{stu_list[i]['eng']},{stu_list[i]['math']},{stu_list[i]['total']},\
{stu_list[i]['avg']},{stu_list[i]['rank']}\n'
    stu_data += stu_str+'\n'


f.write(stu_data)

f.close()
print("완료!")

#----------[추가 데이터 기입하기]-------------------------------------------------
with open('c:/down/bbb.txt','r',encoding='utf8') as f:
    while True:
        
    







# for stu in stu_list:
#     print(f"{stu['stuno']}\t{stu['name']}\t{stu['kor']}\
# \t{stu['eng']}\t{stu['math']}\t{stu['total']}\t{stu['avg']}\t{stu['rank']}")
