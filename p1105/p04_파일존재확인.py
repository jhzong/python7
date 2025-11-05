import os

#
# fname=input("검색하려는 파일 이름을 쓰시오>>")

# 파일이 존재하는지 확인(있으면 a, 없으면 w)
if os.path.exists('c:\\down\\'+'ddd.txt'):
    print('존재')
else:
    print('없음')

# 현재위치에 존재하는 모든 파일을 출력 - list
# print(os.listdir('c:\\down\\'))
