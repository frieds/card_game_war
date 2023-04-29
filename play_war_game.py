from war_game import WarGame


def main():
    player1_name = input("Enter the name of player 1: ")
    player2_name = input("Enter the name of player 2: ")

    game = WarGame(player1_name, player2_name)
    game.play()


if __name__ == "__main__":
    main()
