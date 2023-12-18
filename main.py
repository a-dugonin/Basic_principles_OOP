from coordinate_point import PointCoordinates
from human import Human
from ships import Ship, WarShip, CargoShip

# coordinate_point (task_1)
point_1 = PointCoordinates(x=1, y=1)
print(point_1)
point_2 = PointCoordinates(x=3, y=2)
print(point_2)
point_3 = PointCoordinates(x=8, y=5)
print(point_3)
print()
print()

# human (task_2)
human_1 = Human(name='Антон')
human_1.set_age(age=35)
human_1._Human__age = 18
human_2 = Human(name='Анна', age=18)
print(human_1)
print(human_2)
print(f'Количество человек - {human_1.get_count()}')
print()
print()

# ships (task_3)
cargo_ship = CargoShip(model='cargo_123')
war_ship = WarShip(model='war_craft_ship_777', gun='пушка')
print(cargo_ship)
cargo_ship.load_ship()
cargo_ship.unload_ship()
print(war_ship)
war_ship.attack()
cargo_ship.walk_on_water()

# robots (task_4)