command=input()
tasks=[]
while command!="End":
    tokens=command.split("-",maxsplit=1)
    priority=int(tokens[0])
    task=tokens[1]

    tasks.append((priority, task))
    command = input()
tasks_in_priority=[task_name for priority,task_name in sorted(tasks)]


print(tasks_in_priority)