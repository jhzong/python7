# # 변수 - 1개의 값을 저장하는 공간
# # 복합변수 - 여러개의 값을 저장하는 공간
# # 리스트(순서있음), 튜플(수정불가), 딕셔너리('키'값으로 저장),셋(중복불가)

# a=10
# a_list=[10,20,30,40,50]
# num=1
# nums=[1,2,3]
# print(a)
# print(a_list)
# print(a_list[0])

# a_list=[0,1,2,3,4,5,6,7,8,9]
# # 4,6를 출력
# print(a_list[4])
# print(a_list[6])

# stus=['Hong',100,90,80,270,90.0] # 리스트에 저장되는 값의 타입은 유지 된다.
# print("합계 : ",stus[4])

# # 이름 : 홍길동, 평균 : 90.0 출력. %print 사용.
# print("name : %s, avg : %.1f"%(stus[0],stus[5]))

# a_list=[1,3,5,7,9,11]
# # print 7,11
# print(a_list[3])
# print(a_list[5])
# print(a_list[3],a_list[5])

# stus=['Hong',100,90,80,270,90.0]
# # print Kor : 100
# print("Kor:%d"%stus[1])

stus=["Hong",100,90,80,270,90.0]
# print name:Hong,Kor:100,Eng:90,Math:80
print("name :",stus[0],", Kor :",stus[1])
print("name : %s, Kor: %d, Eng : %d, Math : %d, sum : %d, avg : %.1f"\
    %(stus[0],stus[1],stus[2],stus[3],stus[4],stus[5]))


