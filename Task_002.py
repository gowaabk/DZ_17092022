""" Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом"" """

from random import randint


def input_num_of_candies(user_name):
    num_candies = int(
        input(f"{user_name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while num_candies < 1 or num_candies > 28:
        num_candies = int(
            input(f"{user_name}, введите корректное количество конфет: "))
    return num_candies


def p_print(user_name, k, counter, value):
    print(
        f"Ходил {user_name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")


player1 = 'Player 1'
player2 = 'Player 2'
value = int(input("Введите количество конфет на столе: "))
choice_first_step = randint(0, 2)
if choice_first_step:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

count_player1 = 0
count_player2 = 0

while value > 28:
    if choice_first_step:
        num_of_candies = input_num_of_candies(player1)
        count_player1 += num_of_candies
        value -= num_of_candies
        choice_first_step = False
        p_print(player1, num_of_candies, count_player1, value)
    else:
        num_of_candies = input_num_of_candies(player2)
        count_player2 += num_of_candies
        value -= num_of_candies
        choice_first_step = True
        p_print(player2, num_of_candies, count_player2, value)

if choice_first_step:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")
