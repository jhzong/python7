import os

#-----[덤]-------------------------------------------------
# with open() 파일입출력
with open('c:/down/bbb.txt','r',encoding='utf8') as f:
    while True:
        txt=f.readline()
        if txt=='': break
        print(txt.strip())
# f.close() 생략가능

# f=open('c:/down/bbb.txt','r',encoding='utf8')
# while True:
#     txt=f.readline()
#     if txt=='': break
#     print(txt.strip())
# f.close

#-----[파일읽기]-----------------------------------------------
# # 1. 통로(stream):파일열기
# # r:읽기,w:쓰기,a:추가
# f=open("C:\\workspace\\python7\\p1105\\stusdata.txt","r",encoding="utf8")
# # read(),readline()-1줄,readlines()-전체
# # # read() - byte단위
# # while True:
# #     txt=f.read()
# #     if txt =='': break
# #     print(txt,end='')

# # # readline() - 1줄씩
# # while True:
# #     txt=f.readline() 
# #     if txt=="": break
# #     print(txt,end='') # print완료후 줄바꿈을 해줌.

# # readlines() - 전체읽기
# txt_list=f.readlines() # 1줄을 list에 담아서 가져옴.
# # print(txt_list)
# for txt in txt_list:
#     print(txt,end='')

# f.close()

#-----[파일쓰기]-----------------------------------------------
# # w: 쓰기 - 덮어쓰기, a: 추가 - 기존파일에 추가 
# f=open('c:\\down\\ccc.txt','w') # w모드에서는 파일이 없으면 자동으로 해당경로에 생성.
# stu_data=''
# for i in range(1):
    
#     txt = input("글자을 입력하시오>>\n")
#     stu_data += txt+'\n'


# f.write(stu_data)

# f.close()
# print("완료!")

#-----[파일에 추가]-------------------------------------------------
# f=open('c:\\down\\ccc.txt','a') # a모드
# for i in range(5):
#     f.write(f"안녕하세요. {i} \n")

# f.close

# print("완료!")

#-----[파일복사]-------------------------------------------------------
# r:문자읽기,w:문자쓰기,rb:파일읽기,wb:파일쓰기
f= open('c:/down/nct_wish_01.jpg','rb')
f2= open('c:/aaa/nct_wish_01.jpg','wb')

while True:
    nctfile=f.read(1) # read():파일과 문자 읽기 모두가능, readline()/readlines():문자읽기만 가능
    if not nctfile: break
    f2.write(nctfile)

f.close()
f2.close()
print("복사완료!")