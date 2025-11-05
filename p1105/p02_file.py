import os
#-----[파일쓰기]-----------------------------------------------
# w: 쓰기 - 덮어쓰기, a: 추가 - 기존파일에 추가 
# f=open('c:\\down\\ccc.txt','w') # w모드에서는 파일이 없으면 자동으로 해당경로에 생성.
f=open('c:\\down\\ccc.txt','a') # a모드
stu_data=''
for i in range(1):
    
    txt = input("글자을 입력하시오>>\n")
    stu_data += txt+'\n'


f.write(stu_data)

f.close()
print("완료!")


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
