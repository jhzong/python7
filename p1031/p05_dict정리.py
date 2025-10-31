# {key:value}
stu_dic={'no':1, 'name':'Hong', 'kor':100}

# dict 추가
stu_dic['eng']=90

# dict 수정
stu_dic['kor']=10

# dict 삭제
# del stu_dic['name']

# key값만 출력
print(stu_dic.keys())
print(list(stu_dic.keys()))
for k in stu_dic.keys():
    print("{} : {}".format(k,stu_dic[k]))

# value 출력
print(stu_dic.values())
print(list(stu_dic.values()))
for i,v in enumerate(stu_dic.values()):
    print("{} : {}".format(i,v))

# item()출력
print(stu_dic.items())
print(list(stu_dic.items()))
for k,v in stu_dic.items():
    print("{} : {}".format(k,v))

# dict 출력
print(stu_dic['no'])
print(stu_dic['name'])
print(stu_dic['kor'])
# print(stu_dic.get('math')) # error
print(stu_dic.get('kor'))
print(stu_dic.get('math')) # none

print(stu_dic)

#dict 정렬
import operator
names={"Hong":100,"Yuu":80,"Lee":90,"Kim":99,"Kang":95}
# reverse=True:역순정렬, reverse=False:순차정렬
# itemgetter(0):키, itemgetter(1):값
names2=sorted(names.items(),key=operator.itemgetter(0),reverse=True)

print(names)
print(names2)


# list 정렬
a_list=[1,5,9,4,3]
# sort():해당 list 자체를 정렬
# a_list.sort()
# sorted():다른변수에 저장 가능, 원본은 변경X
# reverse=True:역순
a_list.reverse() # 1,5,9,4,3 -> 3,4,9,5,1
b_list=sorted(a_list,reverse=True)
print(a_list)
print(b_list)

# list 최대값:list에서 최대값 출력
print(max(a_list))
print(max(b_list))


