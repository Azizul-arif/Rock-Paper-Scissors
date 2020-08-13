#rock paper scissors
# ->Rock beats scissor
    # ->Scissor beats paper
    # ->paper beats rock
print("Input must be use 'Rock' 'Paper' 'Scissors'")
def rock_paper_scissor():
    print("Game Start")
    print("Player 1 turn")
    move_player1=input()
    print("Player 2 turn")
    move_player2 = input()
    if(move_player1=='Rock' and move_player2=='Scissors'):
        print("Player 1 win")
    elif(move_player1=='Scissors' and move_player2=='Paper'):
        print("Player 1 win")
    elif(move_player1=='Paper' and move_player2=='Rock'):
        print("Player 1 win")
    elif(move_player1=='Scissors' and move_player2=='Rock'):
        print("Player 2 win")
    elif(move_player1=='Paper' and move_player2=='Scissors'):
        print("Player 2 win")
    elif(move_player1=='Rock' and move_player2=='Paper'):
        print("Player 2 win")
    else:
        print("Match Drawn")
rock_paper_scissor()        