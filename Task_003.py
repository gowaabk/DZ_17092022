""" Создайте программу для игры в ""Крестики-нолики"". """
# Крестики-Нолики

from ast import Lambda
import random


def draw_Board(board: list):
    # Эта функция рисует игровую доску с выполненными ходами

    # "Доска" является списком из 10 строк которые рисуют доску в символьной графике
    #print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    #print('   |   |')
    print('---+---+---')
    #print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    #print('   |   |')
    print('---+---+---')
    #print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    #print('   |   |')


def input_Player_Letter():
    # Игрок выбирает знак, которым он хочет играть
    # Возвращает список знака игрока в качестве первого элемента и знака компьютера в качестве второго элемента
    letter = ''
    while not (letter == '1' or letter == '2'):
        letter = input('Каким знаком вы будете играть? 1=(Х) или 2=(О)')

    # Первый элемент возвращаемого списка знак игрока.
    if letter == '1':
        return ['Х', 'О']
    else:
        return ['О', 'Х']


def first_Go():
    # Случайно определяется, кто будет ходить первым
    if random.randint(0, 1) == 0:
        return 'Компьютер'
    else:
        return 'Игрок'


def make_Move(board: list, letter: str, move: int):
    board[move] = letter


def is_Winner(bo: list, le: str):
    # Функция учитывает позицию на доске и текщий ход игрока. Возвращает True, если игрок выиграл
    # Мы используем bo вместо доски и le вместо полных имен переменных
    return ((bo[1] == le and bo[2] == le and bo[3] == le) or  # Верхняя линия
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # Средняя линия
            (bo[7] == le and bo[8] == le and bo[9] == le) or  # Нижняя линия
            # Левая вертикальная линия
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            # Центральная вертикаль
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or  # Верхняя линия
            (bo[1] == le and bo[5] == le and bo[9] == le) or  # Диагональ
            (bo[7] == le and bo[5] == le and bo[3] == le))  # Диагональ


def board_Copy(board: list):
    # Сделаем копию игровой доски и вернем её
    copy_Board = []

    for i in board:
        copy_Board.append(i)

    return copy_Board


def is_Space_Free(board: list, move: int):
    # Возвращает True если ход возможен
    return board[move] == ' '


def player_Move(board: list):
    # Позволяет игроку выполнить ход
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_Space_Free(board, int(move)):
        move = input('Ваш ход (1-9) --> ')
    return int(move)


def choose_Random_Move_From_List(board: list, movesList: list):
    # Возвращает случайный ход из полученного списка возможных ходов
    # Возвращает None если ходов нет
    possible_Moves = []
    for i in movesList:
        if is_Space_Free(board, i):
            possible_Moves.append(i)

    if len(possible_Moves) != 0:
        return random.choice(possible_Moves)
    else:
        return None


def computer_Move(board: list, computerLetter: str):
    # Получает копию содержимого доски и букву, которой ходит компьютер. Исходя из этого определяет куда двигаться и возвращает ход
    if computerLetter == 'Х':
        playerLetter = 'О'
    else:
        playerLetter = 'Х'

    # Здесь начинается алгоритм ИИ "Крестики-Нолики"
    # Первым шагом будет определение возможности победы на следующем ходу
    for i in range(1, 10):
        copy = board_Copy(board)
        if is_Space_Free(copy, i):
            make_Move(copy, computerLetter, i)
            if is_Winner(copy, computerLetter):
                return i

    # Проверяем, может ли игрок выиграть на следющем ходу, чтобы заблокировать его
    for i in range(1, 10):
        copy = board_Copy(board)
        if is_Space_Free(copy, i):
            make_Move(copy, playerLetter, i)
            if is_Winner(copy, playerLetter):
                return i

    # Попытаемся занять один из углов, если они свободны
    move = choose_Random_Move_From_List(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Занимаем центр, если он свободен
    if is_Space_Free(board, 5):
        return 5

    # Занимаем одну из боковых клеток
    return choose_Random_Move_From_List(board, [2, 4, 6, 8])


def is_Board_Full(board):
    # Возвращаем True, если все клетки на доске были заняты. Иначе возвращаем False
    for i in range(1, 10):
        if is_Space_Free(board, i):
            return False
    return True


def game_Is_Playing():
    x = input('Начнем сначала 1 - Да, 2 - Нет')
    if x == 1:
        return True
    else:
        return False


print('Играем в "Крестики-Нолики"!')

while True:
    # Сбрасываем состояние игровой доски
    theBoard = [' ']*10
    playerLetter, computerLetter = input_Player_Letter()
    turn = first_Go()
    print('Первым будет ходить '+turn + '\n')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'Игрок':
            # Ход игрока
            draw_Board(theBoard)
            move = player_Move(theBoard)
            make_Move(theBoard, playerLetter, move)

            if is_Winner(theBoard, playerLetter):
                draw_Board(theBoard)
                print('Поздравляю!!! Вы победили в игре!')
                gameIsPlaying = False
            else:
                if is_Board_Full(theBoard):
                    draw_Board(theBoard)
                    print('Ничья. В следующий раз играй лучше')
                    break
                else:
                    turn = 'Компьютер'

        else:
            # Ход компьютера
            move = computer_Move(theBoard, computerLetter)
            make_Move(theBoard, computerLetter, move)
            if is_Winner(theBoard, computerLetter):
                draw_Board(theBoard)
                print('Компьютер победил! Вы поиграли...')
                gameIsPlaying = False
            else:
                if is_Board_Full(theBoard):
                    draw_Board(theBoard)
                    print('Ничья. В следующий раз играй лучше')
                    break
                else:
                    turn = 'Игрок'
    if game_Is_Playing() == False:
        break
