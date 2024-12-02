with open("data1.txt", "r") as f_in:
    lines = f_in.readlines()

def check_report(levels):
    dec = int(levels[0]) - int(levels[1]) > 0
    for i in range(len(levels)-1):
        diff = int(levels[i]) - int(levels[i+1])
        if not((diff > 0 and diff <= 3 and dec) or (diff < 0 and diff >= -3 and not dec and diff != 0)):
               return False, i+1
    return True, 0
        
count = 0
res = ""
for idx, report in enumerate(lines):
    levels = report.split()
    valid_report = check_report(levels)
    if not valid_report[0]:
        removed_next = levels[:valid_report[1]] + levels[valid_report[1]+1:]
        removed_prev = levels[:valid_report[1]-1] + levels[valid_report[1]:]
        if check_report(removed_next)[0] or check_report(levels[1:])[0] or check_report(removed_prev)[0]: 
            count += 1
            res += str(idx)+"\n"
    else:
        count += 1
        res += str(idx)+"\n"

print(count)