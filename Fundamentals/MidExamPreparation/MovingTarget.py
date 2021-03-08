line=[int(x) for x in input().split()]
items=input()
def index_in_range(line, index):
    if 0<=index<len(line):
        return True
while items!="End":
    command, index, token=items.split()
    index=int(index)
    if command=="Shoot":
        power=int(token)
        if index_in_range(line, index):
            line[index]-=power
            if line[index]<=0:
                line.pop(index)

    elif command=="Add":
        value=int(token)
        if index_in_range(line,index):
            line.insert(index,value)
        else:
            print("Invalid placement!")
    elif command=="Strike":
        radius=int(token)
        left_boundary=index-radius
        right_boundary=index+radius
        if index_in_range(line, left_boundary) and index_in_range(line, right_boundary) and index_in_range(line,index):
            left_part=line[:left_boundary]
            right_part=line[right_boundary+1:]
            line=left_part+right_part
        else:
            print("Strike missed!")
    items = input()
print(f"{'|'.join(map(str,line))}")