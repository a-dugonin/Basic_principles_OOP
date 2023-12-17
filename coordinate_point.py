class PointCoordinates:
    __count = 0

    def __init__(self, x: int = 0, y: int = 0):
        self.__x = x
        self.__y = y
        PointCoordinates.__count += 1

    def get_count(self) -> int:  # геттер
        return self.__count

    def get_x(self) -> int:  # геттер
        return self.__x

    def get_y(self) -> int:  # геттер
        return self.__y

    def set_x(self, x: int) -> None:  # сеттер
        if isinstance(x, int):
            self.__x = x
        else:
            raise TypeError('Введено не числовое значение')

    def set_y(self, y: int) -> None:  # сеттер
        if isinstance(y, int):
            self.__x = y
        else:
            raise TypeError('Введено не числовое значение')

    def __str__(self):
        return (f'Координата x - {self.__x}, координата y - {self.__y}\n'
                f'Количество точек - {self.__count}')


def main():
    point_1 = PointCoordinates(x=1, y=1)
    print(point_1)
    point_2 = PointCoordinates(x=3, y=2)
    print(point_2)
    point_3 = PointCoordinates(x=8, y=5)
    print(point_3)


if __name__ == '__main__':
    main()
