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

r[start] = 0
while len(r) < int(nv):

    l_min = None
    n_min = None

    for (n, l) in r.items():
        for (from_node, to_node, ww) in w:
            ll = l + int(ww)
            if to_node in r:
                # if r[to_node] > ll:
                #    # r[to_node] = ll
                continue
            if from_node == n:
                if l_min is None or l_min > ll:
                    l_min = ll
                    n_min = to_node
    if l_min is not None:
        r[n_min] = l_min
        if n_min == stop:
            print(l_min)
            break
    print("n:{} l:{}".format(n_min, l_min))
    print(r)

else:
    print(-1)
# зацикливается , а должно выдать -1?
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
