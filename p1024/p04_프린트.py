
#소수점 1자리까지 출력
number=102.123456789
print("%.1f" % number)


#소수점 2자리까지 출력
number2=1.2345
print("%.2f" % number2)

#10자리 공간을 확보해 빈공백은 0으로 채워 출력
number3=100
print("%010d" % number3)

#10자리 공간을 확보해 빈공백은 0으로 채우고, 소수점은 2자리까지 출력
number4=100.23456
print("%010.2f" % number4)
