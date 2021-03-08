items=list(map(int, input().split()))
index =0
output=[]
k=int(input())
while len(items)>0:
    index=(index+k-1)%len(items)
    item=items.pop(index)
    output.append(item)
print(f"["+",".join(map(str,output))+"]")