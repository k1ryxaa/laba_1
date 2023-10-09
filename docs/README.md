# Общее описание решения
1. **Создал папку в которую клонировал исходный репозиторий с помощью команды *git clone***
2. **Создал новую ветку в которой вносил изменения с помощью команды *git branch new_features_(мой код из ИСУ)***
3. **Добавил новые файлы в эту ветку**
4. **создал комит с сообщением что был добавлен новй файл**
5. **добавил еще 1 файл в эту ветку**
6. **исправил ошибку и закомитил пофикшенный вариант**
7. **построил граф всего репозитория и текущей ветки с однострочным выводом комитов с помощью команды *git log --graph --oneline --all***
8. **смерджил добавленную ветку в ветку мастер**
9. **сделал Pull Request**
10. **удалил добавленную ветку**



# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a


___
# Описание каждой функции с примерами вызовов

__circle__:
* def area(r):
* return math.pi * r * r
```angular2html
in: 1
out: 3.14
```
__rectangle__:
* def rectangle(a, b):
* return a*b
```angular2html
in: 4, 5
out: 20
```
__square__:
* def area(r):
* return a*a
```angular2html
in: 1
out: 3.14sgi
```
* def perimeter(r):
* return a*4
```angular2html
in: 2
out: 8
```
__rectangle__:
* def rectangle(a, h):
* return a*h/2
```angular2html
in: 4, 5
out: 10
```

## История изменений проекта с хешами комитов
№1
commit b67f85d816964d302fc65c82843904680036facc 
Author: Kirill <kirillkuznecov5754@gmail.com>
Date:   Mon Oct 9 19:16:09 2023 +0300

    style: добавил circle.py

№2
#### commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
#### Author: smartiqa <info@smartiqa.ru>
#### Date:   Thu Mar 4 14:55:29 2021 +0300
№3
#### commit f4a0be7eea144b5c9944178cc41427f176c9a5e7
#### Author: Kirill <kirillkuznecov5754@gmail.com>
#### Date:   Sat Sep 23 17:54:23 2023 +0300

