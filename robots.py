class Robot:
    """ Класс позволяет создавать объект Robot """
    def __init__(self, model: str = None):
        self.model = model

    def __str__(self):
        return f'Модель робота - {self.model}'


class RobotCleaner(Robot):
    """ Класс позволяет создать робот-пылесос """
    def __init__(self, model: str = None, garbage_bag: int = 0):
        super().__init__(model)
        self.garbage_bag = garbage_bag

    def operate(self):
        """ Метод позволяет запустить робот-пылесос """
        print('Запущен режим уборки пола!')
        self.garbage_bag += 1
        print(f'Заполненность контейнера {self.garbage_bag}')


class WarRobot(Robot):
    """ Класс позволяет создать военного робота """
    def __init__(self, model: str = None, gun: str = None):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print(f'Робот защищает базу с помощью оружия {self.gun}')


class SubmarineRobot(WarRobot):
    """ Класс позволяет создать военного подводного робота """
    def __init__(self, model: str = None, gun: str = None, depth: int = 0):
        super().__init__(model, gun)
        self.depth = depth

    def operate(self):
        super().operate()
        print(f'Охрана ведется под водой на глубине {self.depth}')


def main():
    robot_cleaner = RobotCleaner(model='vacuum_cleaner-1')
    print(robot_cleaner)
    robot_cleaner.operate()
    print()
    war_robot = WarRobot(model='super_war-version_3', gun='пулемет')
    print(war_robot)
    war_robot.operate()
    print()
    submarine_robot = SubmarineRobot(model='submarine_last-5', gun='ракета', depth=20)
    print(submarine_robot)
    submarine_robot.operate()


if __name__ == '__main__':
    main()
