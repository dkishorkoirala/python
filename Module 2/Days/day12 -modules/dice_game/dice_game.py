import random

def roll_dice():
    input("Press Enter to roll the dice...")
    return random.randint(1, 6)

def play_round(round_num):
    print(f"\n🎲 Round {round_num}")

    print("Player 1's turn:")
    a = roll_dice()
    print(f"Player 1 rolled: {a}")

    print("Player 2's turn:")
    b = roll_dice()
    print(f"Player 2 rolled: {b}")

    if a > b:
        print("🏆 Player 1 wins this round!\n")
        return (1, 0)
    elif b > a:
        print("🏆 Player 2 wins this round!\n")
        return (0, 1)
    else:
        print("🤝 It's a tie!\n")
        return (0, 0)

def play_game():
    Awins = 0
    Bwins = 0

    for turn in range(1, 6):
        a_win, b_win = play_round(turn)
        Awins += a_win
        Bwins += b_win
        print(f"Score: Player 1 = {Awins}, Player 2 = {Bwins}")

    return Awins, Bwins
