for _ in range(int(input())):
    n = int(input())
    c=0
    a = list(map(int,input().split()))
    if a[0]!=5:
        print("NO")
    else:
        d = {5:1,10:0}
        a=a[1:]
        for i in range(len(a)):
            if a[i]==5:
                d[5]+=1
            elif a[i]==10:
                if d[5]>=1:
                    d[5]-=1
                    d[10]+=1
                else:
                    c=1
                    print("NO")
                    break
            elif a[i]==15:
                
                if d[10]>=1:
                    d[10]-=1
                elif d[5]>=2:
                    d[5]-=2
                else:
                    c=1
                    print("NO")
                    break
            
        if c==0:
            print("YES")
