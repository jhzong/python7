import os
#------------[파일 읽어오기]-------------------------------------------------------
stu_list=[]
f=open("c:/down/aaa.txt","r")

while True:
    txt=f.readline()
    if txt=='': break
#-----------[str을 dict으로 변경]---------------------------------------------------
    # import ast
    # t_dic=ast.literal_eval
    t_list=txt.strip().split(',')
    t_dic={'stuno':int(t_list[0]),'name':t_list[1],'kor':int(t_list[2]),'eng':int(t_list[3]),\
        'math':int(t_list[4]),'total':int(t_list[5]),'avg':float(t_list[6]),'rank':int(t_list[7]),}    
    
    stu_list.append(t_dic)
print(stu_list)





#--------[dict->파일]-------------------------------------------
stu_str=''
for i in range(len(stu_list)):
    stu_str+=f"{stu_list[i]['stuno']},{stu_list[i]['name']},{stu_list[i]['kor']},\
{stu_list[i]['eng']},{stu_list[i]['math']},{stu_list[i]['total']},\
{stu_list[i]['avg']},{stu_list[i]['rank']}\n"

print(stu_str)



f=open("c:/down/ddd.txt","w",encoding="utf8")
f.write(stu_str)

f.close()