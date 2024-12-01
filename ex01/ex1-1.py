with open("data1-1.txt", "r") as f_in:
    lines = f_in.readlines()
list_a = sorted([int(line.strip().split()[0]) for line in lines])
list_b = sorted([int(line.strip().split()[1]) for line in lines])
print(sum([abs(a-b) for a, b in zip(list_a, list_b)]))