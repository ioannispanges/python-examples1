import random


class GameObject:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Player(GameObject):
    def __init__(self, name, health=100, attack_power=10):
        super().__init__(name)
        self.health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        damage = random.randint(1, self.attack_power)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} and deals {damage} damage")

    # def combine_attack(self, name, attack_power, critical):
    #     super().__init__(name)
    #     self.attack_power = attack_power
    #
    def take_damage(self, damage):
        self.health -= damage
        if self.attack_power <= 0:
            print(f"{self.name} has been defeated ")

    def __str__(self):
        return f"Player {self.name} - Health {self.health}, Attack Power :{self.attack_power}"


class Enemy(GameObject):
    def __init__(self, name, health=100, attack_power=20):
        super().__init__(name)
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        damage = random.randint(1, self.attack_power)
        player.take_damage(damage)
        print(f"{self.name} attacks {player.name} and deals {damage} damage")

    def take_damage(self, damage):
        self.health -= damage
        if self.attack_power <= 0:
            print(f"{self.name} has been defeated ")

    def __str__(self):
        return f"Player {self.name} - Health {self.health}, Attack Power :{self.attack_power}"


class Item(GameObject):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def use(self, player):
        print(f"{player.name} uses {self.name}. {self.description}")

    def __str__(self):
        return f"Item : {self.name}- {self.description}"



player1 = Player("Hero")
enemy1 = Enemy("Monster")
winner = player1 if player1.health > 0 else enemy1

health_potion = Item("Health Potion", "Restore 20 Health")

print(player1)
print(enemy1)

player1.attack(enemy1)
enemy1.attack(player1)

print("=" * 40)

print(player1)
print(enemy1)

health_potion.use(player1)

print("=" * 40)
print(player1)

print(f"{winner.name} wins the battle !")
