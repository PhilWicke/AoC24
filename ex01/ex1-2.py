with open("data1-1.txt", "r") as f_in:
    lines = f_in.readlines()
list_a = [int(line.strip().split()[0]) for line in lines]
list_b = [int(line.strip().split()[1]) for line in lines]

print(sum([a * len([b for b in list_b if b == a]) for a in list_a]))