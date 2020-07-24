t=int(input())
for i in range(t):
    a=input()
    count=0
    for i in range(1,len(a)):
        if (a[i]=='y' and a[i-1]=='x'):
            count+=1
            i+=2
        else:
            continue
    print(count)
