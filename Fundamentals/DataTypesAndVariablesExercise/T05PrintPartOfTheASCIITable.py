start=int(input())
finish=int(input())
for i in range(finish-start+1):
    print(chr(start),end=' ')
    start+=1