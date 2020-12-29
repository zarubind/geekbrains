# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("w_hours", help="work hours", type=int)
parser.add_argument("h_amount", help="hour amount", type=int)
parser.add_argument("add", help="additional payment", type=int)
args = parser.parse_args()
print('Salary:', args.w_hours * args.h_amount + args.add)

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for idx, el in enumerate(my_list) if el > my_list[idx-1] and idx != 0]
print(new_list)

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

my_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(my_list)

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
# четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов
# списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

def my_func(prev_el, el):
    return prev_el * el
print(reduce(my_func, range(100, 1001, 2)))

# 6. Реализовать два небольших скрипта: а) итератор, генерирующий целые числа, начиная с указанного, б) итератор,
# повторяющий элементы некоторого списка, определенного заранее. Подсказка: использовать функцию count() и cycle()
# модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть
# условие его завершения. Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
# завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет
# прекращено.

from itertools import count
from itertools import cycle


def my_int(el):
    for var in count(el):
        yield var


def my_copy(el):
    for var in cycle(el):
        yield var


gen1 = my_int(3)
gen2 = my_copy([1, 2, 3])
for el in gen1:
    print(el)
    if el > 9:
        break
c = 0
for el in gen2:
    print(el)
    if c > 9:
        break
    c += 1

# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове
# функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и
# до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def fact(n):
    for var in range(1, n + 1):
        answer = 1
        for j in range(1, var + 1):
            answer *= j
        yield answer

for el in fact(5):
    print(el)
