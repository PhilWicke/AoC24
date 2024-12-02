with open("data_test.txt", "r") as f_in:
    lines = f_in.readlines()

count = 0
for report in lines:
    levels = report.split()
    dec = int(levels[0]) - int(levels[1]) > 0
    valid = True
    for i in range(len(levels)-1):
        diff = int(levels[i]) - int(levels[i+1])
        if not((diff > 0 and diff <= 3 and dec) or (diff < 0 and diff >= -3 and not dec and diff != 0)):
            valid = False
            break
    if valid:
        count+=1

print(count)
            

        


