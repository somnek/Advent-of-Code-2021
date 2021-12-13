# part 2
b = []

with open('./others/d1b.txt') as f:
    for line in f:
        line = line.strip()
        b.append(int(line))
    f.close()

count = 0
prev = sum(b[:3])
for i in range(len(b) - 2):
    ttl = sum([b[i], b[i+1], b[i+2]])
    print(ttl)
    print(ttl > prev)
    if ttl > prev:
        count += 1
    prev = ttl

print(count)

    

