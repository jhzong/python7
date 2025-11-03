# enlish={
#     '사랑':'love',
#     '커피':'coffee',
#     '컴퓨터':'computer',
#     '이름':'name',
#     '한국':'korea'
# }

# # 영어 맞추기 프로그램
# # 1:O 2:X 3:X 4:O 5:O
# c=0
# en_dic={}
# i=0
# for k,e in enlish.items():
#     # 정답입력
#     print("{} :(\t)".format(k)) 
#     answer=input(">>")

#     # 정답확인
#     if answer==e:     # answer==value
#         print("O")
#         c=c+1         # c=c+1 <=> c+=1
#         i=i+1
#         en_dic[i]="O"
#     else:
#         print("X",e)
#         i=i+1
#         en_dic[i]="X"

# print(f"총 {c}개 맞춤")


# print(en_dic)
        
# 20문중 랜덤으로 5개 뽑아서 퀴즈만들기
import random
enlish={
    '사랑':'love',
    '차':'car',
    '커피':'coffee',
    '전화':'phone',
    '컴퓨터':'computer',
    '이름':'name',
    '한국':'korea',
    '물':'water',
    '지구':'earth',
    '하늘':'sky',
    '공기':'air',
    '고양이':'cat',
    '강아지':'dog',
    '아기':'baby',
    '엄마':'mother',
    '아빠':'father',
    '집':'house',
    '소년':'boy',
    '소녀':'girl',
    '열쇠':'key'
}


q=random.sample(range(20),5) # random을 이용해 임의의 번호 5개 뽑기
q.sort()
score={} # 정/오답 저장공간
print(q) #[4, 10, 14, 15, 17, 18]
c=0
n=1
for idx, k in enumerate(enlish.keys()): # idx와 key를 추출
    if idx in q:
        print(f"{k}를 영어로 쓰시오.") # 문제 번호 idx, 한글 k, 영어 english[k]
        answer=input(">>")

        if answer==enlish[k]:
            print("정답")
            c=c+1
            score[n]='O'
        else:
            print("오답")
            score[n]='X'
        n=n+1    
print(f"{c}개 정답.",score)



