#print() 다양한 출력
print(100)
print("합계")

print("-"*30)

print("100+100=",200)
print("299/3=",(299/3))

# % print를 사용하면 소수점을 제어할 수 있음.
print("299/3=%.3f" % (299/3))#print("YYY %f" % X):X를 문자열의 %f에 대입

kor=100
eng=100
math=99
# %를 사용할때 정수-d, 실수-f
# 100+100+99=299
print(kor,"+",eng,"+",math,"=",kor+eng+math)
print("%d + %d + %d = %d" % (kor,eng,math,(kor+eng+math)))

print("%d" % kor)    # % 뒤에 있는 것을 출력
print("%5d" % kor)   # 5d : 5자리 공간을 확보해 출력
print("%05d" % kor)  # 05d: 5자리 공간을 확보해 공백은 0으로 채움
print("%010d" % kor)
print("%d" % 1000000000)
print("%.2f" % 10.12345) # .2f : 소수점 2자리까지 출력
print("합계 : %05d, 평균 : %.2f" % (299,99.66667))