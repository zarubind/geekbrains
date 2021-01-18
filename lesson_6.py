# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
# желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.
# Подсказка: Подтверждения переключение можно показать вызовом print(self.color) через заданные промежутки времени для
# каждого цвета.

import time
from threading import Thread

class TrafficLight(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__color = 'red'
        self.__color_list = ['red', 'yellow', 'green']
        self.__my_int = [7, 2, 5]

    def run(self):
        while True:
            for idx, val in enumerate(self.__color_list):
                self.__color = val
                print(self.__color)
                time.sleep(self.__my_int[idx])

    def print_color(self):
        print(f'Текущее состояние {self.__color}')

my_traf_light = TrafficLight()
my_traf_light.start() # запуск отдельного потока с переключением цветов

# 1 вариант - проверка состояния на определенной секунде
#time.sleep(8) # например, на 8 секунде должно быть состояние yellow
#my_traf_light.print_color()

# 2 вариант - вывод состояния каждую секунду для контроля
while True:
    time.sleep(1)
    my_traf_light.print_color()

# x = threading.Thread(target=thread_function, args=(1,)) - себе на память, как запустить поток для отдельной функции


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу
# метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self._massa_1cm = 25

    def mass_asph(self, thickness):
        return self._length * self._width * self._massa_1cm * thickness / 1000

my_road = Road(20, 5000)
print(f'{my_road.mass_asph(5)} т')

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

pos1 = Position('Dmitry', 'Rogozin', 'Director Roskosmos', {"wage": 500000, "bonus": 100000})
pos2 = Position('Dzhim', 'Draydenstayn', 'Director NASA', {"wage": 200000, "bonus": 50000})
print(f'{pos1.get_full_name()} ({pos1.position}) зарабатывает {pos1.get_total_income()} $ (за год)')
print(f'{pos2.get_full_name()} ({pos2.position}) зарабатывает {pos2.get_total_income()} $ (за год)')
if pos1.get_total_income() / pos2.get_total_income() > 2:
    print('Кто-то много ворует!')

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        if direction in ['left', 'right']:
            print(f'turn {direction}')
        else:
            print('not turn')

    def show_speed(self):
        print(f'Current speed: {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Speed limit exceeded!')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Speed limit exceeded!')

class PoliceCar(Car):
    pass

towncar = TownCar(30, 'black', 'Toyota', False)
sportcar = SportCar(90, 'red', 'Ferrari', False)
workcar = WorkCar(60, 'white', 'Iveco', False)
policecar = PoliceCar(230, 'blue', 'VAZ', True)
print(f'TownCar: speed={towncar.speed}, color={towncar.color}, name={towncar.name}, is_police={towncar.is_police}')
print(f'SportCar: speed={sportcar.speed}, color={sportcar.color}, name={sportcar.name}, is_police={sportcar.is_police}')
print(f'WorkCar: speed={workcar.speed}, color={workcar.color}, name={workcar.name}, is_police={workcar.is_police}')
print(f'PoliceCar: speed={policecar.speed}, color={policecar.color}, name={policecar.name}, is_police={policecar.is_police}')
towncar.show_speed()
workcar.show_speed()
policecar.turn('left')
policecar.turn('base')

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')

class Pen(Stationery):
    def draw(self):
        print(f'Рисует {self.title}.')

class Pencil(Stationery):
    def draw(self):
        print(f'Рисует {self.title}.')

class Handle(Stationery):
    def draw(self):
        print(f'Рисует {self.title}.')

pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
pen.draw()
pencil.draw()
handle.draw()
