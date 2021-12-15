with open('./others/d5.txt', 'r') as f:
    raw = [line.strip() for line in f.readlines()]
    f.close()

dd = []
for line in raw:
    print([tuple([int(x) for x in n.split(','[0])]) for n in line.split(' -> ')])
    #dd.append([(int(n[0]), int(n[2])) for n in line.split(' -> ')])

#min_val = min([n for pair in dd for point in pair for n in point])
#max_val = max([n for pair in dd for point in pair for n in point])

#print(min_val, max_val)
#plane = [[]]