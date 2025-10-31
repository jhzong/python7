enlish={
    '사랑':'love',
    '커피':'coffee',
    '컴퓨터':'computer',
    '이름':'name',
    '한국':'korea'
}

# 영어 맞추기 프로그램
c=0
en_dic={}
for k,e in enlish.items():
    # 정답입력
    print("{} :(\t)".format(k)) 
    answer=input(">>")

    # 정답확인
    if answer==e:      # answer==value
        print("O ")
        c=c+1          # c=c+1 <=> c+=1
    else:
        print("X",e)

print(f"총 {c}개 맞춤")




            
# names=['Hong','Hong',' Kim','Lee','Yuu','Lee','Hong','Kim','Kang','Hong']
# n_dic={}

# for n in names:
#     if n not in n_dic:
#         n_dic[n]=1
#     else:
#         n_dic[n]=n_dic[n]+1

# print(n_dic)





# a_list=[1,2,3,1,1,2,1,3,4,5]
# a_dic={}

# # 반복
# for i in a_list:
#     if i not in a_dic:
#         a_dic[i]=1
#     else:
#         a_dic[i]=a_dic[i]+1

# print(a_dic)






















# b_dic={}
# # 1:0 2:0 3:0
# for i in range(1,4): #추가
#     b_dic[i]=0
    
# print(b_dic)
# # 2:5 변경
# b_dic[2]=5
# print(b_dic)

# c_dic={}
# # '홍':100 '이':90 '유':80 #추가
# c_dic['Hong']=100
# c_dic['Lee']=90
# c_dic['Yuu']=80

# print(c_dic)

# # '이':95로 변경
# c_dic['Lee']=95
# print(c_dic)

# # '유'를 삭제
# del c_dic['Yuu']

# print(c_dic)












# # 1:4 2:2 3:2 4:1 5:1
# # for 변수 in 범위: #범위-range,list,문자열,dictionary(keys,items,튜플)
# for i in a_list:
#     a_dic[i]=0

# print(a_dic)
# dict 추가 없는 키 입력
# 


# 해당값이 있는지 확인, dict도 똑같음.
# if 1 in a_list:
#     print('존재')
# else:
#     print('없음')

# a_dic={'1':1,'2':3,'3':4}
# if '7' in a_dic:
#     print('존재')
# else:
#     print('없음')
