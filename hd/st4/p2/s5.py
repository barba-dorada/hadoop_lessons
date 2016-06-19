"""
Напишите reducer, который делает пересечение элементов из множества A и B.
На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)
Sample Input:
1	A
2	A
2	B
3	B
Sample Output:
2
"""
import sys

m = {}
for line in sys.stdin:
    if line.strip() == '':
        break
    (k, v) = line.strip().split('\t')
    s = m.get(k, 0)
    m[k] = s + 1

for (k, v) in m.items():
    if v > 1:
        print(k)
