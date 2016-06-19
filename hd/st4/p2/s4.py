"""
Напишите reducer, который объединяет элементы из множества A и B. На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)

Sample Input:
1	A
2	A
2	B
3	B
Sample Output:
1
2
3
"""
import sys

l = []
for line in sys.stdin:
    if line.strip()=='':
        break
    (k, v) = line.strip().split('\t')
    if k in l:
        continue
    l += [k]
for v in l:
    print(v)
