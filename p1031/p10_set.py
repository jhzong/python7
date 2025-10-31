# set - key만 있음. 키 중복불가.
# 중복 제거할때 사용
# 집합 개념
set1={1,1,2,3,4,2,5,4,4,4,1}
print(set(set1))

a_list=[1,2,3,1,1,5,6,7,3]
print(set(a_list))

names=["Hong","Yuu","Lee","Lee","Hong","Yuu"]
nset=set(names)
print(nset) # 변수로 변형해도됨
print(set(names))
