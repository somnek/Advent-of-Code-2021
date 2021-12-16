with open('./others/d5.txt', 'r') as f:
    raw = [line.strip() for line in f.readlines()]
    f.close()

dd = []
for line in raw:
    dd.append([tuple([int(x) for x in n.split(',')]) for n in line.split(' -> ')])

min_val = min([n for pair in dd for point in pair for n in point])
max_val = max([n for pair in dd for point in pair for n in point])

plane = [[0] * (max_val+1) for _ in range(max_val+1)]

# keep only vertical/horizontal
vh = lambda x: x[0][0] == x[1][0]or x[0][1] == x[1][1]
dd = [d for d in dd if vh(d)]

def process(point_a, point_b):
    if point_a[0] == point_b[0]:
        bigger = max([point_a[1], point_b[1]])
        smaller = min([point_a[1], point_b[1]])
        btw = [(point_a[0], n) for n in range(smaller+1, bigger)]
        return [point_a] + btw + [point_b]
    elif point_a[1] == point_b[1]:
        bigger = max([point_a[0], point_b[0]])
        smaller = min([point_a[0], point_b[0]])
        btw = [(n, point_a[1]) for n in range(smaller+1, bigger)]
        return [point_a] + btw + [point_b]

    return []

# mark
for line in dd:
    point_a, point_b = line[0], line[1]
    mp = process(point_a, point_b)
    for p in mp:
        x, y = p[0], p[1]
        plane[y][x] += 1

print(*plane, sep='\n')
final = sum([c > 1 for row in plane for c in row])
print(f"{final=}")