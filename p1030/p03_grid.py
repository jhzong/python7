import random

# 5x5=25
# create list (1~26)
a_list=list(range(1,26))

# shuffle list in rdm
random.shuffle(a_list)
print(a_list)

# print 5x5 grid with rdm list
print("\t<<grid guesser>>")
print("-"*40)
for idx, a in enumerate(a_list):
    print(a,end="\t")
    if(idx+1)%5==0:
        print()
print("-"*40)    

