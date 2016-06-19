"""
Напишите reducer, который реализует симметричную разность множеств A и B (т.е. оставляет только те элементы, которые есть только в одном из множеств).
На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)
Sample Input:
1	A
2	A
2	B
3	B
Sample Output:
1
3

"""
import sys

prev_k = None
prev_v = None
count = 0
for line in sys.stdin:
    if line.strip() == '': break
    (k, v) = line.strip().split('\t')

    if prev_k is None:
        prev_k = k
        prev_v = v
        count += 1
        continue

    if prev_k != k:
        if count == 1 and (prev_v == 'A' or prev_v == 'B'):
            print(prev_k)
        count = 0
    prev_k = k
    prev_v = v
    count += 1
if count == 1 and (prev_v == 'A' or prev_v == 'B'):
    print(prev_k)
