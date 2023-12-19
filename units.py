class Unit:
    def __init__(self, type_unit: str = None, health: int = 100):
        self.type_unit = type_unit
        self.__health = health

    def get_health(self):  # геттер
        return self.__health

    def set_health(self, health: int = 100):  # сеттер
        self.__health = health

    def take_damage(self):
        """ Метод для реализации нанесения урона объекту """
        pass
        print('Объекту нанесен урон')
        print(f'{self.type_unit}, здоровья - {self.get_health()}')

    def __str__(self):
        return f'{self.type_unit}, здоровья - {self.get_health()}'


class Soldier(Unit):
    def take_damage(self, damage: int = 0):
        """ Метод для реализации нанесения урона объекту """
        health = self.get_health() - damage
        self.set_health(health)
        return super().take_damage()

    def __str__(self):
        return super().__str__()


class Citizen(Unit):
    def take_damage(self, damage: int = 0):
        """ Метод для реализации нанесения урона объекту """
        health = self.get_health() - damage * 2
        self.set_health(health)
        return super().take_damage()

    def __str__(self):
        return super().__str__()


def main():
    soldier = Soldier('Солдат')
    print(soldier)
    soldier.take_damage(10)
    soldier.take_damage(30)
    print()
    citizen = Citizen('Обычный гражданин')
    print(citizen)
    citizen.take_damage(30)


if __name__ == '__main__':
    main()
