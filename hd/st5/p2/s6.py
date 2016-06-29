"""
Реализуйте reducer в задаче поиска кратчайшего пути с помощью Hadoop Streaming.

Входные и выходные данные: в качестве ключа идет номер вершины, значение состоит из двух полей, разделенных табуляцией:

Минимальное расстояние до данной вершины (если его еще нет, то пишется INF)
Список исходящих вершин (через "," в фигурных скобках).
Пример работы reducer на второй итерации обработки следующего графа:

Sample Input:
1	0	{2,3,4}
10	INF	{}
10	INF	{}
2	1	{}
2	1	{5,6}
3	1	{}
3	1	{}
4	1	{}
4	1	{7,8}
5	2	{}
5	INF	{9,10}
6	2	{}
6	INF	{}
7	2	{}
7	INF	{}
8	2	{}
8	INF	{}
9	INF	{}
9	INF	{}
Sample Output:
1	0	{2,3,4}
10	INF	{}
2	1	{5,6}
3	1	{}
4	1	{7,8}
5	2	{9,10}
6	2	{}
7	2	{}
8	2	{}
9	INF	{}
"""
import sys

np = None
wp = None
nnn = '{}'
for line in sys.stdin:
    (n, w, nn) = line.strip().split('\t')
    if np is None:
        (np, wp, nnn) = (n, w, nn)
        continue
    if np != n:
        print(np + '\t' + wp + '\t' + nnn)
        (np, wp, nnn) = (n, w, nn)
    else:
        if len(nn) > 2:
            nnn = nn
print(np + '\t' + wp + '\t' + nnn)

