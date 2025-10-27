# 국, 영, 수 점수를 입력 받아 함계, 평균을 출력

k=int(input("Kor score : "))
e=int(input("Eng score : "))
m=int(input("Math score : "))
sum=k+e+m
avg=sum/3
print("합계는 %d입니다."%sum)
print("평균은 %.2f입니다."%avg)
