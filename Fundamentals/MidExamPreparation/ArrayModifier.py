line=[int(x) for x in input().split( )]
command=input()
while command!="end":
    tokens=command.split()
    if tokens[0]=="swap":
        index_1=int(tokens[1])
        index_2=int(tokens[2])
        element_one=line[index_1]
        element_two=line[index_2]
        line.pop(index_1)
        line.insert(index_1,element_two)
        line.pop(index_2)
        line.insert(index_2, element_one)



    elif tokens[0]=="multiply":
        index_1 = int(tokens[1])
        index_2 = int(tokens[2])
        new_element=line[index_1]*line[index_2]
        line.pop(index_1)
        line.insert(index_1,new_element)
    elif tokens[0]=="decrease":
        line=[(x-1) for x in line]


    command = input()
print(", ".join(map(str,line)))