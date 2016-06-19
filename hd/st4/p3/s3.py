"""
Реализуйте reducer первой mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.

Ключ входных данных составной: он содержит слово и номер документа через "#".

Ключом в выходных данных является слово, а значение состоит из двух элементов, разделенных табуляцией: номер документа и tf (сколько раз данное слово встретилось в данном документе).

Sample Input:
aut#1	1
aut#1	1
aut#1	1
aut#1	1
aut#2	1
aut#2	1
bene#2	1
de#2	1
mortuis#2	1
nihil#1	1
nihil#2	1
Caesar#1	1
Sample Output:
aut	1	4
aut	2	2
bene	2	1
de	2	1
mortuis	2	1
nihil	1	1
nihil	2	1
Caesar	1	1
"""
import sys

pr = None;
count = 0;
for line in sys.stdin:
    (n, v) = line.strip().split('\t', 1)

    if pr is None:
        pr = n

    if n != pr:
        print(pr.replace('#', '\t') + '\t' + str(count))
        count = 0
        pr = n
    count += 1

print(pr.replace('#', '\t') + '\t' + str(count))
