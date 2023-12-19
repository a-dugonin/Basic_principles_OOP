class CanFly:
    """ Класс позволяет создать некий объект который умеет летать """

    def __init__(self, height: int = 0, speed: int = 0):
        self.__height = height  # м
        self.__speed = speed  # км/ч

    def get_height(self):  # геттер
        return self.__height

    def get_speed(self):  # геттер
        return self.__speed

    def set_height(self, height: int = 0):  # сеттер
        self.__height = height

    def set_speed(self, speed: int = 0):  # сеттер
        self.__speed = speed

    def take_off(self):
        """ Базовый метод позволяющий объекту взлететь """
        pass

    def fly(self):
        """ Базовый метод позволяющий объекту лететь """
        pass

    def to_land(self, height: int = 0, speed: int = 0, landing_status: bool = False):
        """ Базовый метод позволяющий объекту приземлиться """
        self.set_height(height=height)
        self.set_speed(speed=speed)

    def __str__(self):
        return f'{self.__class__.__name__} на высоте {self.__height}, скорость объекта {self.__speed}'


class Butterfly(CanFly):
    """ Класс для реализации объектов бабочка """
    def take_off(self, height: int = 0):
        """ Метод позволяет бабочке взлететь """
        print('Бабочка взлетела')
        self.set_height(height=height)

    def fly(self, speed: int | float = 0):
        """ Метод позволяет бабочке лететь """
        self.set_speed(speed=speed)
        print(f'Бабочка летит со скоростью {self.get_speed()}')


class Rocket(CanFly):
    """ Класс для реализации объектов ракета """
    def take_off(self, height: int = 0, speed: int = 0):
        """ Метод позволяет ракете взлететь """
        print('Ракета взлетела')
        self.set_height(height=height)
        self.set_speed(speed=speed)

    def to_land(self, height: int = 0, speed: int = 0, landing_status: bool = False):
        """ Метод позволяет ракете приземлиться """
        super().to_land()
        if not landing_status:
            print('Ракета приземлилась')
        else:
            self.explode()

    def explode(self):
        """ Метод взрыва ракеты """
        print('Ба-баххххх... ракета взорвалась!')


def main():
    butterfly = Butterfly()
    print(butterfly)
    butterfly.take_off(height=1)
    butterfly.fly(speed=0.5)
    print(butterfly)
    print()
    rocket = Rocket()
    print(rocket)
    rocket.take_off(height=500, speed=1000)
    print(rocket)
    rocket.to_land(landing_status=True)
    print(rocket)


if __name__ == '__main__':
    main()
