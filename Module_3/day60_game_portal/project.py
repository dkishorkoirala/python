import random
from datetime import datetime

class Character:
    def __init__(self, name: str, max_health: int, attack_power: int, defense: int):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack_power = attack_power
        self.defense = defense
        self.defending = False  # reduces next incoming damage only

    def is_alive(self) -> bool:
        return self.health > 0

    def take_damage(self, incoming_damage: int) -> int:
        # Apply defense and defending bonus
        base = max(1, incoming_damage - self.defense)
        if self.defending:
            base = max(0, base - max(1, self.defense // 2))
            self.defending = False  # defend lasts for one hit

        actual = max(0, min(base, self.health))
        self.health -= actual
        return actual

    def attack(self, target: "Character") -> int:
        # Damage uses (attack_power) adjusted by target defense in take_damage
        variance = random.uniform(0.85, 1.15)
        raw = int(round(self.attack_power * variance))
        dealt = target.take_damage(raw)
        # If you attack, you’re no longer in a defensive stance
        self.defending = False
        return dealt

    def defend(self) -> None:
        self.defending = True

    def heal(self, amount: int = 10) -> int:
        if self.health >= self.max_health:
            self.defending = False
            return 0
        healed = min(amount, self.max_health - self.health)
        self.health += healed
        # Healing drops defensive stance
        self.defending = False
        return healed

    def stats_line(self) -> str:
        return (f"{self.name} | HP {self.health}/{self.max_health} | "
                f"ATK {self.attack_power} | DEF {self.defense}")


class Player(Character):
    def __init__(self, name: str):
        super().__init__(name=name, max_health=100, attack_power=18, defense=6)
        self.level = 1
        self.score = 0

    def level_up(self) -> str:
        self.level += 1
        self.score += 1
        # Small stat boosts each level
        self.max_health += 10
        self.attack_power += 2
        self.defense += 1
        # Heal some on level up (but not full)
        self.health = min(self.max_health, self.health + 20)
        return (f"Level UP! -> L{self.level} | "
                f"+10 Max HP, +2 ATK, +1 DEF, +20 HP restored")


class Enemy(Character):
    pass


# ---------- Game Controller ----------

class Game:
    ENEMY_NAMES = [
        "Goblin", "Skeleton", "Bandit", "Wolf", "Slime",
        "Orc", "Ghoul", "Warlock", "Assassin", "Minotaur"
    ]

    def __init__(self):
        self.player: Player | None = None
        self.enemy: Enemy | None = None
        self.action_log: list[str] = []

    # --- Utilities ---
    def log(self, text: str) -> None:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{ts}] {text}"
        self.action_log.append(line)
        print(line)

    def make_enemy_for_level(self, lvl: int) -> Enemy:
        # Scale enemy stats with level (slightly easier than player)
        name = random.choice(self.ENEMY_NAMES)
        base_hp = 70 + 8 * lvl + random.randint(-5, 10)
        base_atk = 12 + 2 * lvl + random.randint(-2, 2)
        base_def = 4 + (lvl // 2) + random.randint(0, 2)
        return Enemy(name=name, max_health=base_hp, attack_power=base_atk, defense=base_def)

    def show_status(self) -> None:
        print("\n=== STATUS ===")
        print(self.player.stats_line())
        print(self.enemy.stats_line())
        print("==============")

    def show_log(self) -> None:
        print("\n=== ACTION LOG ===")
        if not self.action_log:
            print("(empty)")
        else:
            for entry in self.action_log[-50:]:  # last 50 actions
                print(entry)
        print("==================\n")

    # --- Turns ---
    def player_turn(self) -> bool:
        """
        Returns False if player chose to quit the battle, otherwise True.
        """
        while True:
            print("\nYour move:")
            print("  1) Attack")
            print("  2) Defend (reduce next damage)")
            print("  3) Heal (+10 HP)")
            print("  4) Show Status")
            print("  5) Show Log")
            print("  6) Quit Battle")
            choice = input("Choose (1-6): ").strip()

            if choice == "1":
                dmg = self.player.attack(self.enemy)
                self.log(f"{self.player.name} attacks {self.enemy.name} for {dmg} damage.")
                return True
            elif choice == "2":
                self.player.defend()
                self.log(f"{self.player.name} takes a defensive stance.")
                return True
            elif choice == "3":
                healed = self.player.heal(10)
                if healed == 0:
                    self.log(f"{self.player.name} tried to heal but is already at full HP.")
                else:
                    self.log(f"{self.player.name} heals for {healed} HP.")
                return True
            elif choice == "4":
                self.show_status()
            elif choice == "5":
                self.show_log()
            elif choice == "6":
                self.log(f"{self.player.name} flees the battle.")
                return False
            else:
                print("Invalid choice. Try again.")

    def enemy_turn(self) -> None:
        if not self.enemy.is_alive():
            return
        # Simple AI: prefer attack; sometimes defend; rarely heal if low
        # Weights tweak with enemy HP ratio
        hp_ratio = self.enemy.health / self.enemy.max_health
        actions = ["attack", "defend", "heal"]
        if hp_ratio < 0.35:
            weights = [0.55, 0.20, 0.25]
        else:
            weights = [0.70, 0.25, 0.05]

        move = random.choices(actions, weights=weights, k=1)[0]

        if move == "attack":
            dmg = self.enemy.attack(self.player)
            self.log(f"{self.enemy.name} attacks {self.player.name} for {dmg} damage.")
        elif move == "defend":
            self.enemy.defend()
            self.log(f"{self.enemy.name} takes a defensive stance.")
        else:  # heal
            healed = self.enemy.heal(8)
            if healed == 0:
                # If heal does nothing, attack instead
                dmg = self.enemy.attack(self.player)
                self.log(f"{self.enemy.name} attacks {self.player.name} for {dmg} damage.")
            else:
                self.log(f"{self.enemy.name} heals for {healed} HP.")

    # --- Battle Loop ---
    def battle(self) -> bool:
        """
        Returns True if player won, False if lost or quit.
        """
        self.action_log.clear()
        self.log(f"A wild {self.enemy.name} appears!")

        while self.player.is_alive() and self.enemy.is_alive():
            self.show_status()
            cont = self.player_turn()
            if not cont:
                return False
            if not self.enemy.is_alive():
                break
            self.enemy_turn()

        self.show_status()
        if self.player.is_alive() and not self.enemy.is_alive():
            self.log(f"{self.player.name} defeats the {self.enemy.name}!")
            return True
        else:
            self.log(f"{self.player.name} has fallen... Game Over.")
            return False

    # --- Game Flow ---
    def start(self) -> None:
        print("=== TEXT RPG ===")
        pname = input("Enter your hero's name: ").strip() or "Hero"
        self.player = Player(pname)
        print(f"Welcome, {self.player.name}! Starting at Level {self.player.level}.")
        print(self.player.stats_line())

        while True:
            # Create an enemy scaled to player's current level
            self.enemy = self.make_enemy_for_level(self.player.level)
            print("\n------------------------------------------")
            print(f"Encounter: {self.enemy.stats_line()}")
            print("------------------------------------------")

            player_won = self.battle()
            if not player_won:
                break

            # Level up & ask to continue
            print("\n" + self.player.level_up())
            self.show_log()
            print("\nDo you want to fight the next enemy?")
            cont = input("Enter Y to continue, anything else to quit: ").strip().lower()
            if cont != "y":
                break

        print("\n===== FINAL SUMMARY =====")
        print(f"Player: {self.player.name}")
        print(f"Level reached: {self.player.level}")
        print(f"Score (wins): {self.player.score}")
        print("Thanks for playing!")
        self.show_log()



if __name__ == "__main__":
    random.seed() 
    Game().start()
