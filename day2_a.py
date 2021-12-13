with open('./others/d2.txt', 'r') as f:
    dd = [line.strip('\n') for line in f.readlines()]
    f.close() 

horizontal, depth = 0, 0
for d in dd:
    mp = {d.split()[0]: int(d.split()[1])}
    horizontal += mp.get('forward', 0)
    depth += mp.get('down', 0)
    depth -= mp.get('up', 0)
final = horizontal * depth
print(final)
