line=input().split(" ")
list_new=[]

for i in range(len(line)):
    new_element=int(line[i])
    new_element=new_element*-1
    list_new.append(new_element)
print(list_new)
