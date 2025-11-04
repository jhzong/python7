import stu_func

while True:
    stu_func.screen_print()
    choice=int(input("select menu>>"))
    
    if choice==1:
        stu_func.stu_input()
    
    elif choice==2:
        stu_func.stu_print()
        
    elif choice==3:
        stu_func.stu_modify()
    
    elif choice==4:
        stu_func.stu_delete()
    
    elif choice==5:
        stu_func.stu_rank()
    
    elif choice==0:
        print("exit program...")
        break