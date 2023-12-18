# Инкапсуляция
***
## Задача 1 (task_1)

Реализуйте класс, который будет представлять эту точку, и напишите следующие методы:

* Предоставление информации о точке (используйте магический метод str).
* Геттер и сеттер для x.
* Геттер и сеттер для y.

Для сеттеров реализуйте проверку на корректность входных данных: координаты должны быть числом.

#### Запуск скрипта
Скрипт запускается из основного файла main.py
***
## Задача 2 (task_2)

Реализуйте класс «Человек», который инициализируется именем (имя должно состоять только из букв) и возрастом (должен быть в диапазоне от 0 до 100), а внутри класса считается общее количество инициализированных объектов. Реализуйте сокрытие данных для всех атрибутов (как статических, так и динамических), а для изменения и получения данных объекта напишите специальные геттеры и сеттеры. 

При тестировании класса измените приватный атрибут (например, возраст) двумя способами: сеттером и «крайне не рекомендуемым», который был показан в уроке.

#### Запуск скрипта
Скрипт запускается из основного файла main.py
***
# Наследование
***
## Задача 3 (task_3)
Даны два класса кораблей — грузовой и военный. У каждого из этих кораблей есть своя модель, и каждый может сделать два действия: сообщить свою модель и идти по воде. 

Грузовой корабль имеет такой атрибут, как заполненность, изначально он равен нулю. У него есть ещё два действия: погрузить и выгрузить груз с корабля. 

У военного же корабля нет никаких грузов, есть только оружие, которое передаётся вместе с моделью. Также, вместо погрузки и выгрузки, у него есть другое действие — атаковать.

Реализуйте классы грузового и военного кораблей. Для этого выделите общие атрибуты и методы в отдельный класс «Корабль» и используйте наследование. Не забудьте про функцию super в дочерних классах.
#### Запуск скрипта
Скрипт запускается из основного файла main.py
***