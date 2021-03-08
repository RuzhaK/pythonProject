line=input()
i=0
rage_str=""
result=""
while i<len(line):
    ch=line[i]

    if ch.isdigit():
        count_str=ch
        if i+1<len(line) and line[i+1].isdigit():
            count_str+=line[i+1]
            i+=1
        count=int(count_str)
        current_rage=rage_str.upper()*count
        result+=current_rage
        rage_str=""
    else:
        rage_str+=ch
    i+=1
unique_count=len(set(result))
# todo set example
print(f"Unique symbols used: {unique_count}")
print(result)