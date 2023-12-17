class Human:
    """ Класс позволяет создавать объект человека """
    __count = 0

    def __init__(self, name: str = None, age: int = None):
        self.__name = name
        self.__age = age
        Human.__count += 1

    def get_count(self) -> int:  # геттер
        return self.__count

    def get_name(self) -> str:  # геттер
        return self.__name

    def get_age(self) -> int:  # геттер
        return self.__age

    def set_count(self, count: int) -> None:  # сеттер
        self.__count = count

    def set_name(self, name: str) -> None:  # сеттер
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError('Имя должно состоять из букв')

    def set_age(self, age: int) -> None:  # сеттер
        if isinstance(age, int) and 0 < age < 100:
            self.__age = age
        else:
            raise TypeError('Введено некорректное значение возраста')

    def __str__(self):
        return f'Имя - {self.__name}, возраст - {self.__age}'


def main():
    human_1 = Human(name='Anton')
    human_1.set_age(35)
    human_1._Human__age = 18
    print(human_1)


if __name__ == '__main__':
    main()
