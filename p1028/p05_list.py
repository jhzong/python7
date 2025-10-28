a_list=[1,2,3]
# list 추가 - append, insert, extend
# append - 제일뒤에 추가
a_list.append(10)
print(a_list)
# insert(위치,값) - 지정 위치에 값을 추가
a_list.insert(1,200)
print(a_list)
# extend - 두 리스트를 합침
a2_list=[5,6,7]
a_list.extend(a2_list)
print(a_list)
a_list=a_list+[10,20,30]
print(a_list)

# 변수-비파괴적(값이 유지), 리스트-파괴적(값이 변화)

# list 값 변경 - 위치값을 입력하면 변경됨
a_list[2]=1000
# a_list[100]=1000 # 없는 위치 입력시 에러
print(a_list)

# 삭제
# pop()-제일뒤 삭제
aa_list=[1,2,3,4,5,6,7]
aa_list.pop()
print(aa_list)
# **del - 해당 위치의 값 삭제
del aa_list[0]
print(aa_list)
# remove - 해당값 삭제(앞에서 부터)
aa_list.remove(5)
print(aa_list)
# clear - 모두삭제
aa_list.clear()
print(aa_list)

# [] 1D list
# [[]] 2D list
# [[[]]] 3D list
b_list=[["Hong",100],["Hong",70],["Hong",80],["Hong",90]]

print(b_list)
print(b_list[0])
print(b_list[0][1])