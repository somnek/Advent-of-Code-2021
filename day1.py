a = []
with open('./d1_input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        a.append(int(line))

count = 0
for i in range(1, len(a)):
        if a[i] > a[i - 1]:
            count += 1

print(count)

#with open('./d1_input.txt', 'rb') as f:
#    for line in f:
#        line = line.strip()
#        a.append(int(line))
#
#print(a)

