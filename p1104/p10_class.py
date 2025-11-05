# __init__(O)--------------------------------------------------
class Students:
    def __init__(self,stuno,name,kor,eng,math,):
        self.stuno=stuno
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=self.total/3
        self.rank=0
    
    def total_f(self):
        return self.kor+self.eng+self.math
        
    def avg_f(self):
        return self.total/3

stu_list = []
s1=Students(10101,'Hong',80,80,80)

print(stu_list)


# __init__(X)------------------------------------------------------
class Student:
    stuno = 0
    name = ""
    kor = 0
    eng = 0
    math = 0
    total = 0
    avg = 0
    rank = 0
    
    def sum(self):
        # self.total = self.kor+self.eng+self.math
        return self.kor+self.eng+self.math
    def avg(self):
        return self.total/3



# # stu_list에 추가-------------------------------------------------
# stu_list = []
# # [ {'stuno':10101,'name':'홍길동','kor':80,'eng':80,'math':80,\
# #    'total':240,'avg':80.00,'rank':0} ]
# s1 = Student()
# s1.stuno = 1
# s1.name = "홍길동"
# s1.kor = 100
# s1.eng = 90
# s1.math = 80
# s1.total = s1.sum()
# s1.avg = s1.avg()
# stu_list.append({'stuno':s1.stuno,'name':s1.name,'kor':s1.kor,'eng':s1.eng,\
#       'math':s1.math,'total':s1.total,'avg':s1.avg,'rank':s1.rank})
# print(stu_list)