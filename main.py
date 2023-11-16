# -*- coding: utf-8 -*-
"""python_practice_loops.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18_WxbIGuLrFwTGHVi3Tj5LYoMFMaKIol

# I. range.

1. (4 бали) Створіть обʼєкт типу range, який буде містити послідовність цілих чисел від 0 до 9 включно. Виведіть його довжину (кількість значень).
"""

print(list(range(9)))

"""2. (5 балів) Створіть обʼєкт типу range, який буде містити послідовність цілих чисел (16, 13, 10, 7, 4, 1, -2, -5)"""

print(list(range(-2,17)))

"""3. (4 бали) Створіть змінну зі значенням цілого типу. Перевірте, чи вона належить проміжку від 49 до 100 включно. Як ви гадаєте, для чого використовуються range?"""

a = 51
b = range(49,100)
if a in b:
  print("Присутній")
else:
  print("Не присутній")

"""функція range використовуєтся для того щоб створювати список із послідовних чисел

# II. Comprehensions.

4. (6 балів) Створіть множину (set), використовуючи range та set comprehension.
"""

set_1 = {x for x in range(1, 10)}
print(set_1)

"""5. (8 балів) Створіть словник, використовуючи dict comprehension, що містить if else. Коли слід використовувати comprehensions, а коли їх слід уникати?"""

my_dict = {x: 'Hello' if x % 2 == 0 else 'Goodbye' for x in range(1, 100)}

print(my_dict)

"""**місце для відповіді*

6. (7 балів) Створіть список з рядками та запишіть його у змінну. Створіть ще один список на основі попереднього, де кожен рядок буде містити тільки три перших заглавних символи. Наприклад: ['hello', 'i', 'dont', 'care'] -> ['HEL', 'I', 'DON', 'CAR']
"""

list_1 = ['hello', 'i', 'dont', 'care']

list_2 = [s[:3].upper() for s in list_1]

print(list_2)

"""# III. Цикли.

7. (6 балів) Продемонструйте роботу циклу while. Чи можна використовувати в умові циклу булеві значення? Чому?
"""

while_1 = 10
while (while_1 <= 50) and (while_1 not in range(44, 56, 2)):
   print(while_1)
   while_1 += 1

"""8. (8 балів) Напишіть програму, яка виведе на екран непарні числа в діапазоні від 0 до 20 включно."""

for c in range(20):
    if c % 2 != 0:
        print(c)

"""9. (7 балів) Створіть список з елементами булевого типу або None. Використовуючи цикли, отримайте в результаті список з кортежами, де перший елемент кортежу - індекс(ціле число), а другий елемент - відповідне значення з першого списку.

Наприклад, [True, True, None, False] -> [(0, True), (1, True), (2, None), (3, False)]
"""

list_initial = [True, True, None, False]

list_result = [(index, value) for index, value in enumerate(list_initial)]

print(list_result)

"""10. (10 балів) Створіть словник, де ключі - назви книжок, а значення - їхня кількість у наявності в Вашій міні-бібліотеці. Бібліотека має містити щонайменше 6 книжок (6 пар значень у словнику) і щонайбільше 10 (пар значень). Використовуючи цикли, оновіть словник (не створюйте новий) так, щоби кількість книг у наявності збільшилося на 5 кожної книги. Наприклад,
{'It': 3, 'Fault stars': 10, 'Bible': 17, 'Psychological romance': 4, 'Harry Potter': 13} -> {'It': 8, 'Fault stars': 15, 'Bible': 22, 'Psychological romance': 9, 'Harry Potter': 18}
"""

library = {'It': 3, 'Fault stars': 10, 'Bible': 17, 'Psychological romance': 4, 'Harry Potter': 13}

for book in library:
    library[book] += 5

print(library)

"""11. (15 балів) Визначте цілочислену змінну n, що належить проміжку від 4 до 10 включно. Використовуючи цикли, виведіть в консоль наступний патерн.

#
##
###
####

... #*n

"""

n = 10

for i in range(1, n + 1):
    print("#" * i)

"""12. (20 балів) Гра "Нумо вгадай".
Розробіть просту гру, де користувач має вгадати випадкове число від 1 до 100. Для генерації випадкового числа використовуйте функцію random.randint(a, b) (тут a та b включно). Для отримання числа з консолі використовуйте функцію input(), результат якої обовʼязково явно приведіть до типу int.

Підказка: використовуйте цикл while та умови if-else, щоб повідомити користувачу піказки (напр. "Більше", "Менше") поки користувач не вгадає. По завершенню виведіть кількість спроб, які знадобилися для вгадування.

"""



"""# Вітаю! Ви велика(ий) молодець, що впоралась(вся). Похваліть себе та побалуйте чимось приємним. Я Вами пишаюся."""