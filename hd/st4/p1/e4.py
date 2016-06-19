"""
Реализуйте Combiner в задаче подсчета среднего времени, проведенного пользователем на странице.

Mapper пишет данные в виде key / value, где key - адрес страницы, value - пара чисел, разделенных ";". Первое - число секунд, проведенных пользователем на данной странице, второе равно 1.

Sample Input:
www.facebook.com	100;1
www.google.com	10;1
www.google.com	5;1
www.google.com	15;1
stepic.org	60;1
stepic.org	100;1
Sample Output:
www.facebook.com	100;1
www.google.com	30;3
stepic.org	160;2

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
    (v, g) = val.split(';')
    d[key] = (s + int(v), c + 1)
# print(l)
for key in l:
    (s, c) = d[key]
    print(key + '\t' + str(s) + ';' + str(c))
