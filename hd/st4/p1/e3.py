"""
Реализуйте reducer в задаче подсчета среднего времени, проведенного пользователем на странице.

Mapper передает в reducer данные в виде key / value, где key - адрес страницы, value - число секунд, проведенных пользователем на данной странице.

Среднее время на выходе приведите к целому числу.

Sample Input:
www.facebook.com	100
www.google.com	10
www.google.com	5
www.google.com	15
stepic.org	60
stepic.org	100
Sample Output:
www.facebook.com	100
www.google.com	10
stepic.org	80
"""

import sys

d = {}
l = []
for line in sys.stdin:
    if len(line.strip()) == 0:
        break
        # a = line.strip().split('\t')
        # print(a)
    (key, val) = line.strip().split('\t')  # print(key + "--" + val)
    (s, c) = d.get(key, (0, 0))
    if c == 0:
        l += [key]
    d[key] = (s + int(val), c + 1)
#print(l)
for key in l:
    (s, c) = d[key]
    print(key + '\t' + str(s // c))
