import random

def boss_fight():
    player = input("Enter your player name: ")
    player_hp = 100
    boss_hp = 120
    attempt = 1
    heal_available = True

    print("Welcome to the boss fight!")
    print("You have 100 HP and the boss has 120 HP.")
    print("You can heal every 3 turns.\n")

    while player_hp > 0 and boss_hp > 0:
        print(f"----Turn {attempt}----")
        print(f"{player}'s HP: {player_hp}")
        print(f"Boss HP: {boss_hp}")

        if attempt % 3 == 0 and heal_available:
            print("Heal is available in this turn!")
        
        print("\nChoose Your Action:")
        print("1. Attack")
        if attempt % 3 == 0 and heal_available:
            print("2. Heal")
        
        choose = input("Enter your choice(1 or 2): ")

        if choose == "1":
            damage = random.randint(10, 30)
            boss_hp -= damage
            print(f"You attacked the boss for {damage} damage!")

            if damage > 20:
                print("Critical hit! The boss is badly hurt!")
        elif choose == "2" and attempt % 3 == 0 and heal_available:
            heal = random.randint(15, 30)
            player_hp += heal
            if player_hp > 100:
                player_hp = 100
            print(f"\nYou healed yourself for {heal} HP!")
        else:
            print("\nInvalid action or heal not available.")
            continue

        boss_damage = random.randint(5, 20)

        
        player_hp-= boss_damage
        print(f"Boss attacked you back and dealt {boss_damage} damage!\n")
        attempt += 1

        
    if player_hp <= 0 and boss_hp <= 0:
        print("It's draw!, Both you and the boss are defeated.")
    elif player_hp<= 0:
        print(f"\n{player}, you lost! The boss defeated you.")
    else:
        print(f"Congratulation {player}, you defeated the boss!")
        print(f"You took {attempt -1 } turn to win!")

boss_fight()