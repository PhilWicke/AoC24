with open("data_test.txt", "r") as f_in:
    lines = f_in.readlines()





prod = 0
for line in lines:
    allIndices = [i for i, x in enumerate(line[:-4]) if line[i:i+4]=="mul("]
    
    for idx in allIndices:
        start = line[idx:]
        first = start.split(",", 1)[0]
        second= start.split(")", 1)[0].replace(first+",","")
        first = first.replace("mul(", "")
        if first.isdigit() and second.isdigit():
            prod += int(first)*int(second)
            
print(prod)
      


