"""
Реализуйте алгоритм Дейкстры поиска кратчайшего пути в графе.

Входные данные: В первой строке указаны два числа: число вершин и число ребер графа. Далее идут строки с описанием ребер.
Их количество равно числу ребер. В каждой строке указаны 3 числа: исходящая вершина, входящая вершина, вес ребра.
В последней строке указаны 2 номера вершины: начальная и конечная вершина, кратчайший путь между которыми нужно найти.

Выходные данные: минимальное расстояние между заданными вершинами. Если пути нет, то нужно вернуть -1.

Пример:

Image: https://ucarecdn.com/56a66a36-361d-4b6b-836f-9a18e751eddd/

Sample Input:
4 8
1 2 6
1 3 2
1 4 10
2 4 4
3 1 5
3 2 3
3 4 8
4 2 1
1 4
Sample Output:
9
"""
import sys

r = {}
w = []
line = sys.stdin.readline().strip()
nv, nr = line.split(' ')
for i in range(int(nr)):
    line = sys.stdin.readline().strip()
    w.append(line.strip().split(' '))
    # s[n] = None
line = sys.stdin.readline().strip()
start, stop = line.split(' ')


def www(n):
    lll = []
    for (from_node, to_node, ww) in w:
        if from_node == n:
            lll.append((to_node, int(ww)))
    return lll


r[start] = 0
changes = True
# while len(r) < int(nv):
while changes:
    l_min = None
    n_min = None
    changes = False
    fl = False
    for (n, l) in r.items():
        for (to_node, ww) in www(n):
            if to_node in r:
                continue

            ll = l + ww
            if l_min is None or l_min > ll:
                l_min = ll
                n_min = to_node

    if l_min is not None:
        if r.get(n_min, 1000000) > l_min:
            r[n_min] = l_min
            changes = True
    #print(r)

print(r.get(stop, str(-1)))
# print("n:{} l:{}".format(n_min, l_min))
#print(r)

# else:
# print(-1)  # зацикливается , а должно выдать -1?
"""
4 2
3 1 5
4 2 1
4 1
"""

"""
@Евгений_Макаров У вас зацикливается, например, на таких данных:
4 3
1 3 10
2 3 4
3 2 1
1 4"""

"""
@Степан_Семиохин Проверьте на данных:
5 10
1 2 10
1 3 5
2 3 2
2 4 1
3 2 3
3 4 9
3 5 2
4 5 4
5 1 7
5 4 6
1 4"""

"""
@Veraksa_Eugen Падает на данных:
3 2
1 2 1
2 3 1
1 3"""

""" 5й тест
@Veraksa_Eugen Проверьте на данных:
5 4
1 2 1
2 3 1
3 4 1
4 5 1
1 5"""

"""
3 1
1 2 1
1 3"""

"""
решение  №9282907, то окажется, что оно не проходит 5 тест, потому, что оно не находит путь в самом простом графе:
2 1
1 2 1
1 2
Это очень простой тест. Граф проще состоит только из одной вершины (и на таком тесте также нужно самостоятельно проверять свою программу)
"""
