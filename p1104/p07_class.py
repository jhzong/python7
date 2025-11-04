# class
# class내 변수,함수를 사용하려면, 무조건 객체선언을 해야함.
# 객체선언 : 참조변수 = class명()
class Car:
    color=""
    speed=0
    
    
    # 생성자 객체선언시 값을 바로 할당할수 있도록 해줌
    def __init__(self,color,speed):
        self.color=color  # self.변수명 시 없으면 class에 자동으로 변수가 추가 됨
        self.speed=speed
        self.tire=4
    
    # class내의 함수 첫 매개변수로 self
    # self - 함수밖에 변수를 찾아 변경하기 위해 사용
    def upSpeed(self,num):
        # 함수내 변수를 선택
        self.speed+=num
        
    def downSpeed(self,num):
        self.speed-=num


# # 객체선언 후 값지정
# c1=Car()
# c1.color="blue"
# c1.upSpeed(100)
# c1.downSpeed(30)
# print(c1.color)
# print(c1.speed)



# 생성자를 통해 값지정 - 생성자를 사용해 프로그램을 실행
c2=Car("Blue",100) # 생성자의 매개변수의 개수를 맞춰야함
print(c2.color)
print(c2.speed)
c2.door=5
print(c2.door)


# c1=Car() # 객체선언
# # 사용방법 - 참조변수.변수명
# # 함수 - 참조변수.함수명
# print(c1.speed)
# c1.upSpeed(10) # class내 함수 호출 - 참조변수.함수명()
# print("speed :",c1.speed)

# # speed up 50, down 30, current speed 100
# print(c1.speed)
# c1.upSpeed(50)
# c1.downSpeed(30)
# c1.upSpeed(100)
# print(c1.speed)

# # print speed

# # change color to blue
# c1.color='blue'
# print(c1.color)

