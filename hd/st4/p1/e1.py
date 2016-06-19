"""
Напишите программу, которая реализует In-mapper combining v.1 для задачи WordCount в Hadoop Streaming.
Sample Input:
aut Caesar aut nihil
aut aut
de mortuis aut bene aut nihil
Sample Output:
nihil	1
aut	2
Caesar	1
aut	2
nihil	1
aut	2
de	1
bene	1
mortuis	1

"""
import sys

for line in sys.stdin:
    d = {}
    for token in line.strip().split(" "):
        if token:
            v = d.get(token, 0)
            d[token] = v + 1
            # print(token)
    for (key, val) in d.items():
        print(key + '\t' + str(val))
