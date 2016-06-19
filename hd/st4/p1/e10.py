"""
Реализуйте mapper для задачи Cross-Correlation, который для каждого объекта из кортежа создает stripe.

Mapper принимает на вход кортежи - строки, состоящие из объектов, разделенных пробелом.

Mapper пишет данные в виде key / value, где key - объект, value - соответствующий stripe (пример: a:1,b:2,c:3)

Sample Input:
a b
a b a c
Sample Output:
a	b:1
b	a:1
a	b:1,c:1
b	a:2,c:1
a	b:1,c:1
c	b:1,a:2
"""
import sys

for line in sys.stdin:
    if len(line.strip()) == 0:
        break
    values = line.strip().split(' ')
    for x in values:
        m = {}
        for y in values:
            if x != y:
                v = m.get(y, 0)
                m[y] = v + 1
        s = ''
        for (k, v) in m.items():
            if len(s) > 0: s += ','
            s += k + ':' + str(v)
        s = x + '\t' + s
        print(s)
