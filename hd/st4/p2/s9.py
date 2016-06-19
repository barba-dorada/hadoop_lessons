"""
Напишите reducer, реализующий объединение двух файлов (Join) по id пользователя.
Первый файл содержит 2 поля через табуляцию: id пользователя и запрос в поисковой системе.
Второй файл содержит id пользователя и URL, на который перешел пользователь в поисковой системе.

Mapper передает данные в reducer в виде key / value, где key - id пользователя, value состоит из 2 частей:
маркер файла-источника (query или url) и запрос или URL.

Каждая строка на выходе reducer должна содержать 3 поля, разделенных табуляцией: id пользователя, запрос, URL.

Sample Input:
user1	query:гугл
user1	url:google.ru
user2	query:стэпик
user2	query:стэпик курсы
user2	url:stepic.org
user2	url:stepic.org/explore/courses
user3	query:вконтакте
Sample Output:
user1	гугл	google.ru
user2	стэпик	stepic.org
user2	стэпик	stepic.org/explore/courses
user2	стэпик курсы	stepic.org
user2	стэпик курсы	stepic.org/explore/courses
"""

import sys

prev_user = None
q = []
u = []
for line in sys.stdin:
    if line.strip() == '': break
    (user, v) = line.strip().split('\t')

    if prev_user is None or prev_user != user:
        for q0 in q:
            for u0 in u:
                print(prev_user + '\t' + q0 + '\t' + u0)
        q.clear()
        u.clear()

    (tag, value) = v.split(':')
    if tag == 'url':
        u.append(value)
    elif tag == 'query':
        q.append(value)

    prev_user = user

for q0 in q:
    for u0 in u:
        print(prev_user + '\t' + q0 + '\t' + u0)
