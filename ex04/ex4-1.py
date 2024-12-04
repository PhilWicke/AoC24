with open("data1.txt", "r") as file:
    lines = [ i[:-1] for i in file.readlines() ]

ziel = "XMAS"
horizontal, vertical, diagonal = 0, 0, 0
rows, cols = len(lines), len(lines[0])
diagonal1 = {} 
diagonal2 = {} 

for line in lines:
    for i in range(0,len(line)-3):
        fenster = line[i:i+4]
        if fenster == ziel or fenster == ziel[::-1]:
            horizontal += 1

for s in range(0, len(lines[0])):
    for r in range(len(lines)-3):
        fenster = lines[r][s]+lines[r+1][s]+lines[r+2][s]+lines[r+3][s]
        if fenster == ziel or fenster == ziel[::-1]:
            vertical += 1

for i in range(rows):
    for j in range(cols):
        if i-j not in diagonal1.keys():
            diagonal1[i-j] = []
            diagonal1[i-j].append(lines[i][j])
        else:
            diagonal1[i-j].append(lines[i][j])
        if i+j not in diagonal2.keys():
            diagonal2[i+j] = []
            diagonal2[i+j].append(lines[i][j])
        else:
            diagonal2[i+j].append(lines[i][j])

for diag in [diagonal1, diagonal2]:
    for entry in diag.values():
        target = "".join(entry)
        for i in range(0,len(target)-3):
            fenster = target[i:i+4]
            if fenster == ziel or fenster == ziel[::-1]:
                diagonal += 1

print(horizontal+vertical+diagonal)