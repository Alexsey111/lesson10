import random

class Hero:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона.")
        print(f"У {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name, 120, 25)  # Игрок имеет больше здоровья и урона
        self.computer = Hero("Компьютер", 100, 20)

    def start(self):
        print("Игра начинается!")

        # Рандомный выбор, кто делает первый удар
        first_attacker = random.choice([self.player, self.computer])
        second_attacker = self.computer if first_attacker == self.player else self.player

        while self.player.is_alive() and self.computer.is_alive():
            first_attacker.attack(second_attacker)

            if not second_attacker.is_alive():
                print(f"{first_attacker.name} победил!")
                break

            second_attacker.attack(first_attacker)

            if not first_attacker.is_alive():
                print(f"{second_attacker.name} победил!")
                break

            # Смена очереди удара
            first_attacker, second_attacker = second_attacker, first_attacker


if __name__ == "__main__":
    player_name = input("Введите имя игрока: ")
    game = Game(player_name)
    game.start()