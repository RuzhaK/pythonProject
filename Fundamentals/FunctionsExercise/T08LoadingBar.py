num = int(input())
positions_to_fill=num//10
bar = []
for i in range(10):
    bar.append(".")

def loading_bar(n,line):
    for i in range(n):
       line[i]="%"
    return line


filled=loading_bar(positions_to_fill,bar)
if num < 100:

    print(f"{num}% [{''.join(filled)}]")
    print("Still loading...")
else:
    print(f"{num}% Complete!")
    print(f"[{''.join(filled)}]")
