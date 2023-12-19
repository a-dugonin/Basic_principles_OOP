class DivisionError(Exception):
    pass


def main():
    try:
        with open('numbers.txt', encoding='utf8') as file:
            num_1, num_2 = file.readline().split()
            if int(num_1) > int(num_2):
                print(int(num_1) / int(num_2))
            else:
                raise DivisionError('Нельзя делить меньшее на большее')
    except FileNotFoundError:
        print('Такого файла не существует!')
    except ValueError:
        print('Переданы не числовые значения')
    except DivisionError:
        print('Нельзя делить меньшее на большее')


if __name__ == '__main__':
    main()
