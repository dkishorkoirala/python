import dice_game

def print_winner(player1, player2):
    print("\n🎉 Final Result 🎉")
    if player1 > player2:
        print(f"🏆 Player 1 wins the game! ({player1} - {player2})")
    elif player2 > player1:
        print(f"🏆 Player 2 wins the game! ({player2} - {player1})")
    else:
        print("🤝 It's a tie!")

if __name__ == "__main__":
    p1, p2 = dice_game.play_game()
    print_winner(p1, p2)
