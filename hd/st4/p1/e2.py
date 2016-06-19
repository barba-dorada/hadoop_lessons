"""
Sample Input:
aut Caesar aut nihil
aut aut
de mortuis aut bene aut nihil
Sample Output:
aut	6
mortuis	1
bene	1
Caesar	1
de	1
nihil	2
"""
import sys

d = {}
for line in sys.stdin:
    if len(line.strip()) == 0:
        break

    for token in line.strip().split(" "):
        if token:
            v = d.get(token, 0)
            d[token] = v + 1

for (key, val) in d.items():
    print(key + '\t' + str(val))
