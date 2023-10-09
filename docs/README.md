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
in: 5
out: 25
```
* def perimeter(r):
* return a*4
```angular2html
in: 2
out: 8
```
__triangle__:
* def rectangle(a, h):
* return a*h/2
```angular2html
in: 4, 5
out: 10
```

## История изменений проекта с хешами комитов
№1
#### commit 71dda1bd87f1b188b1147f58baa774bf9cbe9d33
#### Author: Kirill <kirillkuznecov5754@gmail.com>
#### Date:   Mon Oct 9 19:46:20 2023 +0300

№2
#### commit 177735a9da2a957cc3bfa7fe919758e05f267873 (HEAD -> new_1)
#### Author: Kirill <kirillkuznecov5754@gmail.com>
#### Date:   Mon Oct 9 19:47:43 2023 +0300

№3
#### commit c5f269dc90d02b138ff1d29d6c20052f92769b78
#### Author: Kirill <kirillkuznecov5754@gmail.com>
#### Date:   Mon Oct 9 19:44:18 2023 +0300

№4
#### commit 41d3a2c1bc49a7dac762b47f945e05248fe72cbf
#### Author: Kirill <kirillkuznecov5754@gmail.com>
#### Date:   Mon Oct 9 19:43:30 2023 +0300

