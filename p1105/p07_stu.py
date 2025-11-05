# 1명의 학생성적 데이터 class
class Student:
   
    def __init__(self,stuno,name,kor,eng,math):
        self.stuno=stuno
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=self.total/3
        self.rank=0
    
# 객체/참조변수를 출력하면 __str__()함수를 실행
    def __str__(self):
        return f"{self.stuno}\t{self.name}\t{self.kor}\
\t{self.eng}\t{self.math}\t{self.total}\t{self.avg:.2f}\t{self.rank}"
        
# # 객체/참조변수를 출력하면 __str__()함수를 실행
#     def s_print(self):
#         return f"{self.stuno}\t{self.name}\t{self.kor}\
# \t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}"
            
    def s_total(self):
        self.total=self.kor+self.eng+self.math
        
    def s_avg(self):
        self.avg=self.total/3
        
# 학생성적 전체리스트 class
class Students:
    stu_list=[]
    titles=["No.","name","Kor","Eng","Math","T.sum","Avg","Rank"]
        
    def print(self):
        print("<< printing record >>")
        print(" "*10,"student record list" )
        print("-"*65)
        print(*self.titles,sep="\t")
        print("-"*65)
        for stus in self.stu_list:
            print(stus)
        print()
    
    def add(self,student):
        self.stu_list.append(student)



stus=Students()

# students class에서 list에 추가
stus.add(Student(10101,'홍길동',100,100,99))
stus.add(Student(10102,'유관순',90,100,70))
stus.add(Student(10103,'이순신',80,80,100))

stus.print()