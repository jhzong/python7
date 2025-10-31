# stu_list=[name:"Hong",kor:100,eng:100,math:100]#(key) : (value)
# stu_list={key1:value1,key2:value2,key3:value3...} #얕은 복사X

# # 딕셔너리 생성(dict={key:value})
# list1=[1,2,3,]
# dic1={1:'a',2:'b',3:'c'}
# dic2={"no":1,"name":2,"class":3}

# print(list1)
# print(dic1)

# stu={'학번':1,'이름':'홍길동','학과':'컴공'}
# print(stu)
# # 없는 키값 입력 가능
# stu['연락처']='111-1111-1111'
# print(stu)
# # 딕셔너리 수정
# stu['이름']='홍길자'
# print(stu)
# # print(stu['성명']) # 없는 키를 출력할때 에러
# stu['성명1']='홍'
# print(stu)
# del(stu['성명1']) # key는 바꿀 수 없고, 삭제 후 추가해야함.
# print(stu)


stu_list=[
    {'no':1,'name':'Hong','kor':100}
]

print(stu_list[0]['no'])
print(stu_list[0]['name'])


a_dic={'no':1,'name':'Hong','kor':100}
# 국어점수 출력
print(a_dic['kor'])# 없는 key값 입력시 에러

# dictionary get()
print(a_dic.get('kor1'))# 없는 key값 입력시 none타입으로 출력.

# dictionary keys()
print(a_dic.keys())
a_list=list(a_dic.keys())
print(a_list[1])
# dictionary value()
print(a_dic.values())
b_list=list(a_dic.values())
print(b_list)

# dictionary item() - key,value
print(a_dic.items())
c_list=list(a_dic.items())
print(c_list)


aa_list=[
    ['no',1],
    ['name','Hong'],
    ['kor',100]
]

print(aa_list[1][1])





stu_dic={'no':1,'name':'Hong','kor':100}
if 'kor' in stu_dic:
    print("key exist")
else:
    print("no key")

