for _ in range(int(input())):
    c,d=0,0
    for _ in range(int(input())):
        A,B=input().split()
        a,b=0,0
        for i in str(A):
            a+=int(i)
        for i in str(B):
            b+=int(i)
        if a>b:
            c+=1
        elif b>a:
            d+=1
    if c>d:
        print(0,c)
    elif d>c:
        print(1,d)
    else:
        print(2,1)
