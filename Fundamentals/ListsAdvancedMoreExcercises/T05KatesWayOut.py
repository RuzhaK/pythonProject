n = int(input())
maze = []
count_moves = 0
for i in range(n):
    maze.append(input())
for i in range(len(maze)):
    if "k" in maze[i]:
        row_index = i
        break
position = maze[row_index].index("k")
Kate_is_out=False
while not Kate_is_out:

    if maze[row_index][position] == len(maze[row_index]) or maze[row_index][position] == 0  or row_index==0 or row_index==-1:
        count_moves += 1
        print(f"Kate got out in {count_moves} moves")
        Kate_is_out=True
        break

    elif maze[row_index][position + 1] == " ":
        position+=1
        count_moves += 1
    elif maze[row_index][position -1] == " ":
        position-=1
        count_moves += 1
    elif maze[row_index+1][position] == " ":
        row_index+=1
        count_moves += 1
    elif maze[row_index-1][position] == " ":
        row_index-=1
        count_moves += 1
    else:
        print("Kate cannot get out")
    #todo dovarshi


