# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# (проверку на корректность) числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
# на реальных данных.

from datetime import datetime

class Date:
    def __init__(self, datestr):
        self.datestr = datestr
        self.day, self.month, self.year = 0, 0, 0

    @classmethod
    def parse_date(cls, dateobj):
        try:
            date = datetime.strptime(dateobj.datestr, "%d-%m-%Y")
            dateobj.day, dateobj.month, dateobj.year = date.day, date.month, date.year
        except ValueError:
            return False
        return True

    @staticmethod
    def check_date(dateobj): # Преобразование без datetime, не реализована проверка разного количества дней в месяцах
        day, month, year = dateobj.datestr.split('-')
        day, month, year = int(day), int(month), int(year)
        if day in range(1, 32) and month in range(1, 13) and year in range(1, 2022):
            return True
        return False

my_date = Date('20-12-2021')
if Date.parse_date(my_date):
    print(f'{my_date.day} {my_date.month} {my_date.year}')
if Date.check_date(my_date):
    print('Correct date!')
else:
    print('Incorrect date!')

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class ZeroError(ZeroDivisionError):
    def __init__(self, text):
        self.txt = text

try:
    a = int(input('Введите делимое число:'))
    b = int(input('Введите делитель:'))
    if b == 0:
        raise ZeroError("Делитель равен 0!")
    print(f'{a}/{b}={a/b}')
except ZeroDivisionError as err:
    print(err)

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При
# этом работа скрипта не должна завершаться.

class CheckList(Exception):
    def __init__(self, text):
        self.txt = text

my_list = []
print('Введите элементы списка:')
while True:
    tmp = input()
    try:
        if tmp.isdigit():
            my_list.append(int(tmp))
        elif tmp == 'stop':
            break
        else:
            raise CheckList('!!! Это не число !!!')
    except CheckList as err:
        print(err)
print(my_list)

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В
# базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над прошлым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, нельзя
# отправить принтеры в виде строки или меньше 0.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на
# уроках по ООП.

class Storage:
    def __init__(self, name):
        self.name = name
        self.printer = {}
        self.scaner = {}
        self.copy = {}

    def get_eq(self, eq):
        if eq.eqtype == 'printer':
            self.printer.update({eq:0})
        elif eq.eqtype == 'scaner':
            self.scaner.update({eq:0})
        elif eq.eqtype == 'copy':
            self.copy.update({eq:0})
        else:
            return False

    def set_room(self, eq, room):
        if eq.eqtype == 'printer':
            self.printer.update({eq:room})
        elif eq.eqtype == 'scaner':
            self.scaner.update({eq:room})
        elif eq.eqtype == 'copy':
            self.copy.update({eq:room})
        else:
            return False

class Equipment:
    def __init__(self, name, price, year, form, int):
        self.name = name
        self.price = price
        self.year = year
        self.form = form
        self.int = int

    def __str__(self):
        ret = ''
        for val in self.__dict__:
            ret += f'{val}:{self.__dict__[val]} '
        return ret

class Printer(Equipment):
    def __init__(self, name, price, year, form='A4', p_type='laser', int='USB'):
        self.eqtype = 'printer'
        self.p_type = p_type
        super().__init__(name, price, year, form, int)

class Scaner(Equipment):
    def __init__(self, name, price, year, form='A4', s_type='led', int='USB'):
        self.eqtype = 'scaner'
        self.s_type = s_type
        super().__init__(name, price, year, form, int)

class Copy(Equipment):
    def __init__(self, name, price, year, form='A4', c_type='multifunctional', int=None):
        self.eqtype = 'copy'
        self.c_type = c_type
        super().__init__(name, price, year, form, int)

printer1 = Printer('samsung ml-1750', 100, 2010)
printer2 = Printer('hp laserjet', 110, 2014)
scaner1 = Scaner('hp 1000x', 80, 2015)
scaner2 = Scaner('acer 4455', 90, 2017)
copy1 = Copy('xerox 1212', 120, 2018)
copy2 = Copy('xerox 7878', 220, 2021)

my_storage = Storage('Storage1')
my_storage.get_eq(printer1)
my_storage.get_eq(printer2)
my_storage.get_eq(scaner1)

print(printer1)
print(len(my_storage.printer))
my_storage.set_room(printer1, 222)
print(len(my_storage.printer))
print(my_storage.printer)

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        oper = '+' if self.b >= 0 else ''
        return f'{self.a}{oper}{self.b}i'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __truediv__(self, other):
        tmp_a = (self.a*other.a + self.b*other.b)/(other.a**2 + other.b**2)
        tmp_b = (self.b*other.a - self.a*other.b)/(other.a**2 + other.b**2)
        return Complex(tmp_a, tmp_b)

aaa = Complex(3, 4)
bbb = Complex(1, 2)
ccc = aaa / bbb
print(ccc)
