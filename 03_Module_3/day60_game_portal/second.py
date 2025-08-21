class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        """Reduce target's health by attack power"""
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.health -= self.attack_power

    def is_alive(self):
        """Check if character is alive"""
        return self.health > 0


# ---- Simple Game Flow ----
player = Character("Hero", 30, 5)
enemy = Character("Goblin", 20, 3)

print(" Battle Start! ")

while player.is_alive() and enemy.is_alive():
    # Player attacks first
    player.attack(enemy)
    print(f"{enemy.name}'s health: {enemy.health}")
    if not enemy.is_alive():
        print(f"{player.name} wins!")
        break

    # Enemy attacks back
    enemy.attack(player)
    print(f"{player.name}'s health: {player.health}")
    if not player.is_alive():
        print(f"{enemy.name} wins!")
        break
