with open('./others/d3.txt', 'r') as f:
    dd = [line.strip() for line in f.readlines()]
    f.close()


gamma, epsilon = 0, 0
l = [0 for _ in range(12)]
for i in range(len(dd)):
    for j in range(12):
        l[j] += 1 and int(dd[i][j]) or -1

gamma = int(''.join([str(int(i > 0)) for i in l]), 2)
epsilon = int(''.join([str(int(i < 0)) for i in l]), 2)
 
final = gamma * epsilon
