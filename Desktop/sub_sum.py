def test(arr,size):
    count=0
    rang=[]
    for i in range(size):
        count+=arr[i]
        rang.append(i)
        if count==b:
            break
    print(rang)
#drivers code
a,b=input().split()
arr=list(map(int,input().split()))
size=len(arr)
test(arr,size)
