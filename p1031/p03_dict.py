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