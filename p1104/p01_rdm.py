# 모듈 : 함수의 집합
# 다른 파일의 모듈을 사용하려면, import를 해야 사용가능
# import를 하면 (파일이름.함수명)으로 호출

# import func # func.py의 모든 함수를 불러옴
# import random
# import 이름.함수명
# func.func2()
# random.sample()

# from 파일명 import 함수를 정의하면 파일명 생략가능
# 모듈명 생략가능
# from 모듈명 import 함수,클래스

# # from func import func1,func2...
# # print(func1())
# from func import * # *를 이용해 파일내의 모든 파일 불러옴
# print(func1())
# func2       # 함수사용
# s1=stu()    # 클래스 사용

# # 예제
# # 수학공식
from math import floor,ceil
# # floor : 소수점 버림, ceil : 소수점 올림, round : 반올림
print(floor(1.95))
print(ceil(1.2))
print(round(1.59)) # 내장함수(import 불필요)

# # 모듈이름이 길때 as를 이용해 약어 사용 가능(import A as B)
import random as r

print(r.randint(1,6))

import math
# # dir:모듈안에 있는 모든 함수를 보여주는 명령어
print(dir(math)) # math 안의 모든 함수
print(dir(r))    # r(aka. random) 안의 모든 함수

# 날짜와 시간을 가져오는 모듈
# python-날짜,html-날짜,javascript-날짜,db-날짜
import datetime
now=datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

import time
print("a")
time.sleep(5)
print("b")

# 패키지:모듈 파일을 모아둔 폴더
# from func import func1
# from 폴더명.모듈명 import 변수,함수,클래스,*
from cal.func import*
print(func1())

from cal import func
print(func.func1())