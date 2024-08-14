"""
Задание: Разработать консольную игру "Битва героев" на Python с использованием классов
 и разработать план проекта по этапам/или создать kanban доску для работы над данным
 проектом

Общее описание:
Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с
различными характеристиками. Игра состоит из раундов, в каждом раунде игроки по
очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.

Требования:

    Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
    Игра должна быть реализована как консольное приложение.

Классы:

Класс Hero:
    Атрибуты:
    Имя (name)
    Здоровье (health), начальное значение 100
    Сила удара (attack_power), начальное значение 20

    Методы:
    attack(other): атакует другого героя (other), отнимая здоровье в размере своей
    силы удара
    is_alive(): возвращает True, если здоровье героя больше 0, иначе False

Класс Game:

    Атрибуты:
    Игрок (player), экземпляр класса Hero
    Компьютер (computer), экземпляр класса Hero

    Методы:
    start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не
    умрет. Выводит информацию о каждом ходе (кто атаковал и сколько здоровья осталось
    у противника) и объявляет победителя.

В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с
реализацией задания и скриншот/файл с планом проекта по этапам или kanban-доску
(таблицу/скриншот таблицы)
"""

import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        other.health -= self.attack_power

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Computer")

    def start(self):
        print("Let the battle begin!")
        current_player = self.player
        while self.player.is_alive() and self.computer.is_alive():
            if current_player == self.player:
                input("Player's turn. Press Enter to attack.")
                self.player.attack(self.computer)
                print(f"{self.player.name} attacked {self.computer.name}. {self.computer.name}'s health: {self.computer.health}")
                current_player = self.computer
            else:
                input("Computer's turn. Press Enter to attack.")
                self.computer.attack(self.player)
                print(f"{self.computer.name} attacked {self.player.name}. {self.player.name}'s health: {self.player.health}")
                current_player = self.player

        if self.player.is_alive():
            print(f"Congratulations! {self.player.name} won!")
        else:
            print("Computer won. Better luck next time.")


# Игра начинается
player_name = input("Enter your hero's name: ")
game = Game(player_name)
game.start()
