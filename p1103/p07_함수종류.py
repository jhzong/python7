# return : 함수를 호출한 곳으로 값을 전달할때 사용.
#          함수 결과 값을 변수로 저장해야 할떄 사용.
def cal(a,b): # 매개변수는 꼭 타입을 일치할 것
    return a+b
    #return a+b # 함수 끝을 만나면 함수종료
    #return     # return을 만나면 함수종료

num1=cal(10,5)
num2=cal(2,7)
num3=cal(3,5)
num4=cal('a',9)# error