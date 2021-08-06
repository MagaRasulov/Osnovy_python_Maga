import time
from itertools import cycle
'''1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение
светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет
7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между
режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу
примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт.'''
# class TrafficLight:
#
#     __color = ['Красный', 'Желтый', 'Зеленый']
#
#     def running(self):
#         for i in cycle(self.__color):
#             print(i)
#             if i == 'Красный':
#                 time.sleep(7)
#             elif i == 'Желтый':
#                 time.sleep(2)
#             else:
#                 time.sleep(5)
#
# a = TrafficLight()
# a.running()
'''2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать 
формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной 
в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т'''
# class Road:
#
#     def __init__(self, lenght, width):
#         self._lenght = lenght
#         self._width = width
#
#     def result(self):
#         a = int(input('Введите массу асфальта: '))
#         b = int(input('Введите толщину полотна: '))
#         return self._lenght * self._width * a * b
#
# a = Road(20, 5000)
# print(a.result())


'''3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position 
(должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий 
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) 
на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name) 
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры 
класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).'''
# class Worker:
#     name = 'Petr'
#     surname = 'Ivanov'
#     position = 'constructor'
#     _income = {'wage': 50000, 'bonus': 12000}
#
#
# class Position(Worker):
#
#     def get_full_name(self):
#         print(f'{self.name} {self.surname}')
#
#     def get_total_income(self):
#         print(self._income['wage'] + self._income['bonus'])
#
# a = Position()
# a.surname, a.name = 'Nikiforov', 'Ivan'
# a.get_full_name()
# a.get_total_income()


'''4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, 
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, 
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов 
TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите 
результат. Выполните вызов методов и также покажите результат.'''
# class Car:
#     speed = 80
#     color = 'blue'
#     name = 'Porshe'
#     is_police = False
#
#     def go(self):
#         print('Машина поехала')
#
#     def stop(self):
#         print('Машина остановилась')
#
#     def turn(self, direction):
#         self.direction = direction
#         print(f'Машина повернула на {self.direction}')
#
#     def show_speed(self):
#         print(self.speed)
#
#
# class TownCar(Car):
#
#     def show_speed(self):
#         if self.speed > 60:
#             print('Вы превышаете скорость')
#
#
# class WorkCar(Car):
#
#     def show_speed(self):
#         if self.speed > 40:
#             print('Вы превышаете скорость')
#

# class PoliceCar(Car):
#     is_police = True
#
#
# class SportCar(Car):
#     speed = 120
#

# a = WorkCar()
# a.show_speed()
#
# b = PoliceCar()
# print(b.is_police)


'''5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) 
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), 
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого 
из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет 
описанный метод для каждого экземпляра.'''
# class Stationery:
#     title = 'Тетрадь'
#
#     def draw(self):
#         print('Запуск отрисовки')
#
#
# class Pen(Stationery):
#     title = 'Ручка'
#
#     def draw(self):
#         print('Ручкой надо писать')
#
#
# class Pencil(Stationery):
#     title = 'Карандаш'
#
#     def draw(self):
#         print('Карандашом лучше чертить')
#
#
# class Hundle(Stationery):
#     title = 'Маркер'
#
#     def draw(self):
#         print('Маркером лучше раскрашивать')
#
# a = Pen()
# print(a.title)
# a.draw()
#
# b = Pencil()
# print(b.title)
# b.draw()
#
# c = Hundle()
# print(c.title)
# c.draw()