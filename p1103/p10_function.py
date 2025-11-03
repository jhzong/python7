# 기본매개변수 - 호출함수 매개변수 개수와 함수정의 매개변수 개수가 같아야 함.

# 가변배개변수 - 기본변수가 압에 오고, 뒤에 가변 매개변수가 오면 매개변수가 달라도 됨.
#              표기는 *매개변수 라고 하면 됨.

# def func(a,*b):
#     print(a)
#     for i in b:
#         print(i)

# func(1,2,3,4)


# keyword 매개변수 - 변수에 미리 할당하고, 값이 들어오면 입력값을 계산하고,
#                  입력값이 없으면 미리 할당된 값으로 계산.

# def func(a,b=10):
#     print(a+b)
    
# func(20,10)
# func(20)
# func(10)

# def func(*a,b=10):
#     print(b)
#     for i in a:
#         print(i)
# func(10,1,2,3,b=2)


from StuFunc import* # StuFunc.py 안에있는 모든 함수를 가져옴
# score recorder

while True:
    screen_print()  # 함수호출
    m=int(input("select menu>>"))
    
    if m==1: # 성적입력
        stu_input()
        stu_print() # 함수를 호출함으로써 코드 중복 제거
        
    elif m==2: # 성적출력
        stu_print()
        
    elif m==3:
        
        pass