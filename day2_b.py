with open('./others/d2.txt') as f:
    dd = [line.strip() for line in f.readlines()]
    f.close()


horizontal, depth, aim = 0, 0, 0
for i in range(len(dd)):
    ins, val = dd[i].split()[0], int(dd[i].split()[1])
    if ins == 'down':
        aim += val
    elif ins == 'up':
        aim -= val
    elif ins == 'forward':
        horizontal += val
        depth += aim * val

final = horizontal * depth
print(final)