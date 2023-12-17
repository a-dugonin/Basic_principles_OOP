from coordinate_point import PointCoordinates
from human import Human


point_1 = PointCoordinates(x=1, y=1)
print(point_1)
point_2 = PointCoordinates(x=3, y=2)
print(point_2)
point_3 = PointCoordinates(x=8, y=5)
print(point_3)
print()
print()

human_1 = Human(name='Антон')
human_1.set_age(age=35)
human_1._Human__age = 18
human_2 = Human(name='Анна', age=18)
print(human_1)
print(human_2)
print(f'Количество человек - {human_1.get_count()}')



