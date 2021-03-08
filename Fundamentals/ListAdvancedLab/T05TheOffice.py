happiness=[int(n) for n in input().split()]
factor=int(input())
factored_happiness=[v*factor for v in happiness]
average_happiness=sum(factored_happiness)/len(factored_happiness)
happy_values=list(filter(lambda n: n >= average_happiness, factored_happiness))
happy_count=len(happy_values)
total_count=len(happiness)

if happy_count>=total_count/2:
    print(f"Score: {happy_count}/{total_count}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{total_count}. Employees are not happy!")
