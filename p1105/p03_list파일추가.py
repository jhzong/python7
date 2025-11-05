import os

# f=open('C:\\workspace\\python7\\p1105\\stusdata.txt','r',encoding='utf8')
# txt=f.readline() 
# # txt="1,홍길동,100,100,100,300,100.00,0"
# print(txt.strip().split(',')) # strip():공백제거, split():~기준으로 분리
# print(txt.strip().split(',')[5])
# f.close

# bbb를 출력
# bbb를 a_list에
a_list=[]

f=open('C:\\down\\bbb.txt','r',encoding='utf8')

while True:
    txt=f.readline()
    if txt=="": break
    a_list.append(txt.strip().split(',')) # strip()으로 공백(\n)값 제거
f.close
print(a_list)