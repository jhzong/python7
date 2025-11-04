title=["No.","name","Kor","Eng","Math","T.sum","Avg","Rank"]
stu_list=[
    [10101,"Hong",80,80,80,240,80.00,0,0],
    [10102,"Yuu",90,90,90,270,90.00,0,0],
    [10103,"lee",100,100,100,300,100.00,0]
]

# 등수처리
for s1 in stu_list:
    count=1
    for s2 in stu_list:
        if s1[5]<s2[5]:
            count+=1
    s1[7]=count

# 출력
print(*title,sep="\t")
for i in stu_list:
    print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}".format(*i))
print()

