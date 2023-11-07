import random
import matplotlib.pyplot as plt

# Calculate distance between two cities
def distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

# Calculate the total distance of a path
def total_distance(path, places):
    d = 0
    for i in range(len(path) - 1):
        d += distance(places[path[i]], places[path[i + 1]])
    d += distance(places[path[-1]], places[path[0]])
    return d

# Make an initial group of paths
def make_initial(num, group_size):
    group = [list(range(num)) for _ in range(group_size)]
    return group

# Calculate the fitness of each path
def calculate_fitness(group, places):
    fitness = [1 / total_distance(p, places) for p in group]
    return fitness

# Choose parents for the next step
def choose_parents(group, fitness):
    total = sum(fitness)
    probs = [f / total for f in fitness]
    chosen = random.choices(range(len(group)), weights=probs, k=2)
    return [group[chosen[0]], group[chosen[1]]]

# Make a new path from two parents
def combine(p1, p2):
    s, e = sorted(random.sample(range(len(p1)), 2))
    child = [-1] * len(p1)
    child[s:e] = p1[s:e]
    rest = [item for item in p2 if item not in child]
    j = 0
    for i in range(len(p1)):
        if child[i] == -1:
            child[i] = rest[j]
            j += 1
    return child

# Change a path a little bit
def change(p, rate):
    if random.random() < rate:
        a, b = random.sample(range(len(p)), 2)
        p[a], p[b] = p[b], p[a]

# Keep the best paths
def keep_best(group, fitness, percent):
    count = int(percent * len(group))
    best = sorted(range(len(fitness)), key=lambda k: fitness[k])[-count:]
    return [group[i] for i in best]

# Main part
def main(num, group_size, generations, combine_rate, change_rate, best_percent):
    places = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num)]
    group = make_initial(num, group_size)
    
    for g in range(generations):
        fitness = calculate_fitness(group, places)
        new_group = []
        
        best = keep_best(group, fitness, best_percent)
        new_group.extend(best)
        
        while len(new_group) < group_size:
            p1, p2 = choose_parents(group, fitness)
            if random.random() < combine_rate:
                child = combine(p1, p2)
            else:
                child = p1
            change(child, change_rate)
            new_group.append(child)
        
        group = new_group
    
    best_path = min(group, key=lambda p: total_distance(p, places))
    best_d = total_distance(best_path, places)
    
    return best_path, best_d, places

# Draw the best path
def draw(path, places):
    x = [places[i][0] for i in path]
    y = [places[i][1] for i in path]
    x.append(places[path[0]][0])
    y.append(places[path[0]][1])
    
    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title("Best Path")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

# Ask for input and run the program
num = int(input("Number of places: "))
group_size = int(input("Size of group: "))
generations = int(input("Number of generations: "))
combine_rate = float(input("Combine rate: "))
change_rate = float(input("Change rate: "))
best_percent = float(input("Best percent: "))

best_path, best_d, places = main(num, group_size, generations, combine_rate, change_rate, best_percent)
    
print("Best path:",best_path)
print("Distance:", best_d)

plt.figure(figsize=(10,6))
plt.plot(places)
plt.xlabel("Generation")
plt.ylabel("Best Distance")
plt.title("TSP Genetic Algorithm - Distance Evolution")
plt.grid(True)
plt.show()

draw(best_path, places)
