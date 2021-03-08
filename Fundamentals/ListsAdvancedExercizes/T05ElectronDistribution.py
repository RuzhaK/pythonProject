electrons=int(input())
electrons_list=[]
cell_number=1
while electrons>0:
    possible_electrons=min(2*cell_number**2,electrons)
    electrons_list.append(possible_electrons)
    electrons-=possible_electrons
    cell_number+=1

print(electrons_list)