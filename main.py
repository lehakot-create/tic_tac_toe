def print_table(table):
    text = ''
    text += '-' * 13 + '\n'
    for i in range(0, 9, 3):
        text += f'| {table[i]} | {table[i+1]} | {table[i+2]} |' + '\n'
        text += '-' * 13 + '\n'
    return text


def init_table():
    return list(range(1, 10))


def check_win(table):
    lst = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
           (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    flag = False
    for el in lst:
        if table[el[0]] == table[el[1]] == table[el[2]]:
            flag = True
    return flag


def free_cell(table):
    return [el for el in table if type(el) == int]


def comp_step(table):
    dct = {}
    lst = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
           (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    enemy_step = table.count('X')  # посчитать колво ходов соперника
    if enemy_step == 0:
        return 4
    elif enemy_step == 1:  # у соперника 1 ход: выбираем ячейку с большим колвом комбинаций
        # for i in range(10):
        #     for el in lst:
        #         print(i, el)
        #         if all([i in el, table[el[0]] != 'X', table[el[1]] != 'X', table[el[2]] != 'X']):
        #             dct[i] = dct.get(i, 0) + 1
        # return max(dct.items(), key=lambda x: x[1])[0]
        if table[4] == 'X':
            return 0
        else:
            return 4
    elif enemy_step == 2:  # у соперника 2 хода: перекрываем линию соперника
        pass
    else:
        pass



    # у соперника 3 хода:
    #           - проверить свою линию
    #           - перекрыть линию противника


# print(comp_step([1, 'X', 3, 4, 5, 6, 7, 8, 9]))

def check_answer(questions, lst):
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
        print('В разработке')
    else:
        # user1 = X  user2 = 0
        user = 1
        table = init_table()
        while True:
            print(print_table(table))
            answer = check_answer(f'Пользователь {user} ваш ход:', free_cell(table))
            table = edit_table(table, answer, dct[user])
            if check_win(table):
                print(f'Пользователь {user} выиграл.')
                if check_answer(f'Еще поиграем? 1-да/2-нет', [1, 2]) == 1:
                    main()
                else:
                    break
            if user == 1:
                user = 2
            else:
                user = 1


# if __name__ == '__main__':
#     main()
