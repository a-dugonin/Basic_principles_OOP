class Ship:
    """ Класс позволяет создать объект "Корабль" с базовым атрибутом в качестве модели """
    def __init__(self, model: str = None):
        self.model = model

    def walk_on_water(self):
        """ Метод позволяет кораблю плыть """
        print(f'Корабыль поплыл')

    def __str__(self) -> str:
        return f'Модель корабля - {self.model}'


class CargoShip(Ship):
    """ Класс позволяет создавать грузовые корабли на базе родительского класса Ship """
    def __init__(self, model: str = None, fullness: int = 0):
        super().__init__(model)
        self.fullness = fullness

    def load_ship(self):
        """ Метод позволяет загрузить корабль """
        print('Загружаем корабль')
        self.fullness += 1
        print(f'Загруженность корабля = {self.fullness}')

    def unload_ship(self):
        """ Метод позволяет разгрузить корабль """
        print('Разгружаем корабль')
        if self.fullness == 0:
            print('Корабль разгружен')
        else:
            self.fullness -= 1
        print(f'Загруженность корабля = {self.fullness}')


class WarShip(Ship):
    """ Класс позволяет создавать военные корабли на базе родительского класса Ship """
    def __init__(self, model: str = None, gun: str = None):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        """ Метод позволяет произвести атаку """
        print(f'Корабль атакует с помощью {self.gun}')


def main():
    cargo_ship = CargoShip(model='cargo_123')
    war_ship = WarShip(model='war_craft_ship_777', gun='пушка')
    print(cargo_ship)
    cargo_ship.load_ship()
    cargo_ship.unload_ship()
    print(war_ship)
    war_ship.attack()
    cargo_ship.walk_on_water()


if __name__ == '__main__':
    main()
