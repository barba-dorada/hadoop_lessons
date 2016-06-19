"""
Реализуйте reducer из задачи Distinct Values v2.
Reducer принимает на вход строки, каждая из которых состоит из разделенных табуляцией значения и названия группы.
Sample Input:
1	a
1	b
1	b
2	a
2	d
2	e
3	a
3	b
Sample Output:
a	3
d	1
b	2
e	1
"""
import sys

kk = []
m = {}
for line in sys.stdin:
    if len(line.strip()) == 0:
        break
    (k, v) = line.strip().split('\t')

    if not ((k, v) in kk):
        kk += [(k, v)]

for (k, v) in kk:
    vv = m.get(v, 0)
    m[v] = vv + 1
for (k, v) in m.items():
    print(k + '\t' + str(v))
