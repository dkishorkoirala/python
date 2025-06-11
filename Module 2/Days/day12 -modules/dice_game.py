import random

Awins = 0
Bwins = 0
turn = 1
while turn <= 5:
    print(f"\nRound {turn}")

    print("\nplayer 1")
    print("Enter any key...")
    input()
    a = random.randint(1, 6)
    print(f"You got {a}")
    
    input()
    print("\nPlayer 2")
    print("Enter any key...")
    input()
    b = random.randint(1, 6)
    print(f"You got {b}")

    if a > b :
        Awins += 1
        print ("\nPlayer 1 wins this round")
    else:
        Bwins += 1
        print(f"\nPlayer 2 wins this round")

    turn += 1

    if Awins > Bwins :
        print(f"\nPlayer 1 wins the game {Awins} - {Bwins}")
    else:
        print(f"\nPlayer 2 wins the game {Bwins} - {Awins}")
