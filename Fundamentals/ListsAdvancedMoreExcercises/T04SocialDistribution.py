population = input().split(", ")
min_wealth = int(input())
population=[int(num)for num in population]

if sum(population) / len(population) < min_wealth:
    print("No equal distribution possible")
else:
    for i in range(len(population)):
        if population[i]<min_wealth:
            difference=min_wealth-population[i]
            population[i]=min_wealth
            position=population.index(max(population))
            population[position]-=difference
    print(population)



