#국어, 영어, 수학 점수를 입력받아 합계와 평균을 출력하시오.
Kor=int(input("Korean score :"))
Eng=int(input("English score :"))
Math=int(input("Math score :"))

Sum=Kor+Eng+Math #변수 지정해 반복 사용
print("합계 :", Sum)
Avg=Sum/3
print("평균 :", Avg)
#print("평균 : %.2f" % Avg)
