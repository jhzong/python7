# 변수 - 숫자, 문자열, 불
# 변수는 한번에 1개의 값만 저장
a=10
a=5
print(a)

# 리스트, 튜플, 셋
# 리스트 - 배열 : 데이터를 여러개 저장하는 공간

fruit=["사과","배","복숭아","딸기","포도"]
print(fruit)
print(fruit[0])

numbers=[1,2,3,4,5]
print(numbers)
print(numbers[0])

total=["apple",1,2,True,1.25]
print(total)

stuscore=["홍길동",100,100,100,300,100.0]
print(stuscore)

## 리스트에 데이터 추가
stuscore.append("A") # .append로 리스트에 값 추가
print(stuscore)

stuscore.insert(1,5) # .insert로 1번 위치에 "5"를 추가
print(stuscore)

## 리스트에서 데이터 삭제
stuscore.pop() # 리스트 마지막 리스트값 삭제
print(stuscore)

stuscore.remove("홍길동") # remove로 해당 리스트값 삭제
print(stuscore)

del total[0] # del로 해당 위치의 리스트값 삭제
print(total)