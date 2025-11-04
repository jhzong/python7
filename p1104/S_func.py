# 학생 1명 성적을 저장하는 공간
class Student:
    def __init__(self,stuno,name,kor,eng,math): # 생성자 - 객체선언시 함수호출
        self.stuno=stuno # self 자동으로 변수생성
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math
        self.total=kor+eng+math
        self.avg=self.total/3
        self.rank=0
    
    def sum(self):
        return self.kor+self.eng+self.math
    
    def avg(self):
        return self.total/3
    
# 학생성적들을 저장하는 공간
class Stuscore:
    stu_list=[]
    titles=["No.","name","Kor","Eng","Math","T.sum","Avg","Rank"]
    
    # 학생성적을 1명 추가하는 함수
    def add(self,s):
        self.stu_list.append(
            {'stu_no':s.stuno,'name':s.name,'kor':s.kor,\
    'eng':s.eng,'math':s.math,'sum':s.total,'avg':s.avg,'rank':s.rank}
        )
        print("추가됐습니다.")
    
# 학생성적을 출력    
    def print(self):
        print("<< printing record >>")
        print(" "*10,"student record list" )
        print("-"*65)
        print(*self.titles,sep="\t")
        print("-"*65)   
        for stus in self.stu_list:
            print(f"{stus['stu_no']}\t{stus['name']}\t{stus['kor']}\t{stus['eng']}\
\t{stus['math']}\t{stus['sum']}\t{stus['avg']:.2f}\
\t{stus['rank']}")
        print()