import random # 선언, random 클라스 가져와 쓰겠다.
# 0.000000000<=x<1.000000000
print(random.random()) 
# 1~10사이의 숫자를 랜덤으로 가져옴.
print(random.randrange(1,11)) 
# 1~10사이의 숫자를 랜덤으로 가져옴.
print(random.randint(1,11)) 
# 해당 리스트에서 2개를 랜덤으로 가져옴(중복X)
print(random.sample([1,2,3,4,5],2)) 
# 해당 리스트에서 4개를 랜덤으로 가져옴(중복O)
print(random.choices([1,2,3,4,5],k=4)) 
# 해당리스트의 순서를 랜덤으로 조정
a_list=[1,2,3,4,5]
random.shuffle(a_list) 
print(a_list)