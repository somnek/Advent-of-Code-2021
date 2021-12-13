from collections import Counter

with open('./others/d3.txt', 'r') as f:
    dd = [line.strip() for line in f.readlines()]
    f.close()

d_oxy = dd
d_co2 = dd
# oxygen most common
for i in range(12):
    if len(d_oxy) == 1:
        break
    i0 = Counter([d[i] for d in d_oxy])['0']
    i1 = Counter([d[i] for d in d_oxy])['1']
    if i0 > i1:
        d_oxy = [d for d in d_oxy if d[i] == '0']
    elif i0 < i1:
        d_oxy = [d for d in d_oxy if d[i] == '1']
    elif i0 == i1:
        d_oxy = [d for d in d_oxy if d[i] == '1']

# co2 least common
for i in range(12):
    if len(d_co2) == 1:
        break
    i0 = Counter([d[i] for d in d_co2])['0']
    i1 = Counter([d[i] for d in d_co2])['1']
    if i0 > i1:
        d_co2 = [d for d in d_co2 if d[i] == '1']
    elif i0 < i1:
        d_co2 = [d for d in d_co2 if d[i] == '0']
    elif i0 == i1:
        d_co2 = [d for d in d_co2 if d[i] == '0']

oxygen_generator = int(d_oxy[0], 2)
co2_scrubber = int(d_co2[0], 2)
final = oxygen_generator * co2_scrubber
print(final)
