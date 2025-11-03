def cal():
    print()
    

    while True:
        a=int(input("for a>>"))
        if a==0:
            print("end program")
            break
        b=int(input("for b>>"))
        cal(a,b)
