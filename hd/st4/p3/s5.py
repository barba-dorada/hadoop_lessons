"""
Реализуйте reducer второй mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.

Входные данные: ключ - слово, значение - тройка: номер документа, tf слова в документе и 1 (разделены ';').

Выходные данные: ключ - пара: слово, номер документа (разделены '#'), значение - пара: tf слова в документе, n - количество документов с данным словом (разделены табуляцией).

Sample Input:
aut	1;4;1
aut	2;2;1
bene	2;1;1
de	2;1;1
mortuis	2;1;1
nihil	1;1;1
nihil	2;1;1
Caesar	1;1;1
Sample Output:
aut#1	4	2
aut#2	2	2
bene#2	1	1
de#2	1	1
mortuis#2	1	1
nihil#1	1	2
nihil#2	1	2
Caesar#1	1	1
"""
import sys

wPrev = None
l = []
for line in sys.stdin:
    (w, v) = line.strip().split('\t')

    if not(wPrev is None):
        if wPrev != w:
            for vv in l:
                (n, c, n0) = vv.split(';')
                print(wPrev + '#' + str(n) + '\t' + c + '\t' + str(len(l)))
            l.clear()

    wPrev = w
    l += [v]

for vv in l:
    (n, c, n0) = vv.split(';')
    print(wPrev + '#' + str(n) + '\t' + c + '\t' + str(len(l)))
