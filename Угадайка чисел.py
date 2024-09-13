import random


def is_valid(number):
    if 100 >= number >= 1:
        return True
    else:
        return False


cnt = 0  # подсчет попыток

print('Добро пожаловать в числовую угадайку')
g = int(input("Укажите правую границу: "))
n = random.randint(1, g)
print("Хорошо, ваш ход!")

while True:
    num = int(input())
    if is_valid(num):
        cnt += 1
        if num < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')

        elif num > n:
            print('Ваше число больше загаданного, попробуйте еще разок')

        else:
            print('Вы угадали, поздравляем!')
            print("Вам потребовалось", cnt, "попыток!")
            cont = input("Желаете продолжить? (Да/Нет): ")
            if cont.lower() == "да":
                print("Ну что-ж, продолжим!)")
                g = int(input("Укажите правую границу: "))
                n = random.randint(1, g)
                print("Хорошо, ваш ход!")
                continue
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break

    else:
        print('А может быть все-таки введем целое число от 1 до 100?')
