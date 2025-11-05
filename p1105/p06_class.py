# 클래스의 장점 - 변수,함수를 함께 저장, 변수에 접근 제한, 한번의 선언으로 여러개의 변수와 함수를 사용 가능.
#               동일한 변수들을 묶음

# def 함수명():
#     프로그램

# class 이름: # class는 대문자로 시작
#     프로그램

class Car:
    
    
    # Car() 객체선언 할때 __init__함수 먼저 호출
    def __init__(self,color,speed):
        self.color=color
        self.speed=speed
    
    def upSpeed(self,speed): # 지역변수
        self.speed+=speed
    

# class를 사용하려면(변수/함수를 호출,변수에 값을 입력) 무조건 객체선언을 해야함.
# 객체선언
# 참조변수명 = 클래스명()

c =Car("white",0)
# 값읽기
print(c.color)
# 값수정
c.color="red"
print(c.color)

c2=Car("red",100)
c2.upSpeed(100)
print(c2.speed)


# class cal:
#     __hour=12 # 접근제한
#     min=30
#     sec=20
    
#     def setHour(self,hour):
#         if hour>23:
#             print("23보다 큰수는 입력 할수 없습니다.")
#             return
#         self.__hour = hour
#     def getHour(self):
#         return self.__hour

# time=cal()
# print(time.min)
# print(time.__hour) # class의 변수에 직접접근제한
# print(time.getHour)