fruit=["사과","배","수박","딸기","포도"]
# 삭제
# 해당 과일을 삭제
print("과일 리스트 : ", fruit)
input2=input("삭제할 과일>>")
if input2 in fruit: # "in" 리스트 안에 해당 글자가 있는지 확인
    fruit.remove(input2)
else:
    print("해당 과일이 리스트에 없습니다.")

print("과일 리스트 : ",fruit)


# input1=input("좋아하는 과일을 입력>>")
# fruit.append(input1)
# print("입력된 과일 : ",fruit)

#

str1="안녕하세요. 반갑습니다. 저는 홍길동입니다."
# 1개의 글자를 입력받아, str1 변수에 존재하는지 확인
print(str1)
input1=input("1개의 글자를 입력하시오.")
# 입력글자 : 하, 존재합니다.
if input1 in str1:
    print("입력한 문자 : %s, 존재합니다."%input1)
else:
    print("입력한 문자 : %s, 존재하지 않습니다."%input1)

