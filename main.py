from settings import WIN_COMBO


def print_table(table):
    text = ''
    text += '-' * 13 + '\n'
    for i in range(0, 9, 3):
        text += f'| {table[i]} | {table[i+1]} | {table[i+2]} |' + '\n'
        text += '-' * 13 + '\n'
    return text


def init_table():
    return list(range(1, 10))


def check_win(table, lst=WIN_COMBO):
    flag = False
    for el in lst:
        if table[el[0]] == table[el[1]] == table[el[2]]:
            flag = True
    return flag


def free_cell(table):
    return [el for el in table if type(el) == int]


def win_line(table, find_char='X'):
    # найти ячейки занятые соперником
    tmp = []
    dct = {}
    for el in range(len(table)):  # индексы ячеек
        if table[el] == find_char:
            tmp.append(el)
    # найти попадание значений в эл из списка
    for el in WIN_COMBO:
        for i in tmp:
            if i in el:
                dct[el] = dct.get(el, 0) + 1
    dct_sort = sorted(dct.items(), key=lambda x: x[1], reverse=True)
    for el in dct_sort:
        if table[el[0][0]] not in ['X', '0']:
            return el[0][0]
        elif table[el[0][1]] not in ['X', '0']:
            return el[0][1]
        elif table[el[0][2]] not in ['X', '0']:
            return el[0][2]


def comp_step(table):
    enemy_step = table.count('X')  # посчитать колво ходов соперника
    if enemy_step == 0:
        return 4
    elif enemy_step == 1:  # у соперника 1 ход: выбираем ячейку с большим колвом комбинаций
        if table[4] == 'X':
            return 0
        else:
            return 5
    else:  # у соперника 2 хода: перекрываем линию соперника
        cell_num = win_line(table, 'X')
        if cell_num is None:
            return None
        if table[cell_num] == '0':
            # если занята, то составить свою линию
            pass
        else:
            return cell_num + 1


def check_answer(questions, lst=WIN_COMBO):
    while True:
        answer = input(questions)
        if answer.isdigit():
            if int(answer) in lst:
                return int(answer)
        else:
            print('Укажите верные данные')


def edit_table(table, num, char):
    table[num-1] = char
    return table


def main():
    dct = {1: 'X', 2: '0'}
    print('*'*61)
    print('*', ' '*20, 'Крестики-нолики', ' '*20, '*',)
    print('*' * 61)
    print('*', ' '*10, 'Компьютер <---- 1 ----> Пользователь', ' '*9, '*')
    print('*', ' '*7, 'Пользователь <---- 2 ----> Пользователь', ' '*9,  '*')
    answer = check_answer('Выберите вариант игры: ', [1, 2])

    if answer == 1:
        # user = 1 = 'X'  comp = 2 = '0'
        user = 1
        table = init_table()
        while True:
            print(print_table(table))
            if user == 1:
                answer = check_answer(f'Пользователь {user} ваш ход:', free_cell(table))
            elif user == 2:
                print('Ход компьютера')
                answer = comp_step(table)
            if not (answer is None):
                table = edit_table(table, answer, dct[user])
            if check_win(table) or answer is None:
                if answer is None:
                    print(print_table(table))
                    print('Ничья')
                    break
                elif user == 1:
                    print(print_table(table))
                    print(f'Пользователь {user} выиграл.')
                    break
                elif user == 2:
                    print(print_table(table))
                    print('Компьютер выиграл')
                    break
            if user == 1:
                user = 2
            else:
                user = 1
        if check_answer(f'Еще поиграем? 1-да/2-нет', [1, 2]) == 1:
            main()
    else:
        # user1 = 'X'  user2 = '0'
        user = 1
        table = init_table()
        while True:
            print(print_table(table))
            answer = check_answer(f'Пользователь {user} ваш ход:', free_cell(table))
            table = edit_table(table, answer, dct[user])
            if check_win(table):
                print(print_table(table))
                print(f'Пользователь {user} выиграл.')
                if check_answer(f'Еще поиграем? 1-да/2-нет', [1, 2]) == 1:
                    main()
                else:
                    break
            if user == 1:
                user = 2
            else:
                user = 1


if __name__ == '__main__':
    main()
