# Mетод . lower () гарантирует, что такие варианты ввода, как "Basketball" или "BasketBall ",будут интерпретироваться
# одинаково.
sport = input ( "Enter а sport: ")
p1_score=int(input("Enter player 1 score: "))
p2_score = int(input("Enter player 2 score: "))
# 1
if sport.lower() == "basketball":
# 2
    if p1_score == p2_score:
        print("The game is а draw.")
    elif p1_score > p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
elif sport.lower() == "golf":
# 3
    if p1_score == p2_score:
        print("The game is а draw.")
    elif p1_score > p2_score:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    print("Unknown sport")
