# stu_dic={}

# # 'no':1,'name':'Hong','kor':100 를 dictionary에 추가
# # 키 : 값

# stu_dic['no']=1
# stu_dic['name']='Hong'
# stu_dic['kor']=100
# print(stu_dic)

# for k,v in stu_dic.items(): # (key, value)
#     print("{}:{}".format(k,v))
    
# for k in stu_dic.keys():    # key, stu_dic[key]=value
#     print("{}:{}".format(k,stu_dic[k]))
    
# for v in stu_dic.values():
#     print("값 : {}".format(v))


# a_list=list(stu_dic.items())
# print(a_list)

# print("{} : {}".format(a_list[0][0],a_list[0][1]))
# print("{} : {}".format(a_list[1][0],a_list[1][1]))
# print("{} : {}".format(a_list[2][0],a_list[2][1]))

stu_list=[
    {'no':1,'name':'Hong','kor':100},
    {'no':2,'name':'Yuu','kor':80},
    {'no':3,'name':'Lee','kor':90}
]

# 3번째에 있는 kor를 50으로 변경
stu_list[2]['kor']=50
print(stu_list)

stus={'no':3,'name':'Lee','kor':90}
# kor -> 50
stus['kor']=50
print(stus)
    
a_list=[3,"Lee",90]
a_list[2]=50
print(a_list)
