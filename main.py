koloda = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
import random
random.shuffle(koloda)
print('Поиграем в очко?')
count_player = 0
count_computer = 0

while True:
    choice = input('Будете брать карту? (y/n)\n')
    if choice == 'y':
        current = koloda.pop()
        print('Вам попалась карта достоинством %d' % current)
        count_player += current
        if count_player > 21:
            print('Извините, вы проиграли.')
            break
        elif count_player == 21:
            print('Поздравляю, у вас 21!')
            break
        else:
            print('У вас %d очков.' % count_player)
    elif choice == 'n':
        print('Вы закончили игру со счетом %d очков.' % count_player)
        break
    else:
        print('Пожалуйста, введите "y" или "n".')

    # Ход компьютера
    if count_computer < 18:
        current = koloda.pop()
        print('Компьютер взял карту достоинством %d' % current)
        count_computer += current
        if count_computer > 21:
            print('Компьютер проиграл.')
            break
        elif count_computer == 21:
            print('Компьютер набрал 21!')
            break
        else:
            print('У компьютера %d очков.' % count_computer)

# Определение победителя
if count_player > count_computer and count_player <= 21:
    print('Вы победили! У вас %d очков, а у компьютера %d очков.' % (count_player, count_computer))
elif count_computer > count_player and count_computer <= 21:
    print('Компьютер победил! У него %d очков, а у вас %d очков.' % (count_computer, count_player))
elif count_player == count_computer:
    print('Ничья! У вас и у компьютера по %d очков.' % count_player)
else:
    print('Вы проиграли! У вас %d очков, а у компьютера %d очков.' % (count_player, count_computer))