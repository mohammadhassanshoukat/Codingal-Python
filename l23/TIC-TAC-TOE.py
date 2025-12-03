#implemention of 2 players in python game
board={'7':' ' , '8':' ' , '9':' ' ,
       '4':' ' , '5':' ' , '6':' ' ,
       '1':' ' , '2':' ' , '3':' ' }
boardkeys=[]
for key in board:
    boardkeys.append(key)
def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
#now we will write the main function which has all the gameplay functionality
def game():
    turn='X'
    count=0
    for i in range(10):
        printboard(board)
        print("It's your turn " + turn + ". Move to which place?")
        move=input()
        if board[move]==' ':
            board[move]=turn
            count+=1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
        #now we will check if the player X or 0 has wn for every move after 5 moves
        if count>=5:
            if board['7']==board['8']==board['9']!=' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['4']==board['5']==board['6']!=' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['1']==board['2']==board['3']!=' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['1']==board['4']==board['7']!=' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['2']==board['5']==board['8']!=' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['3']==board['6']==board['9']!=' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['7']==board['5']==board['3']!=' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
            elif board['1']==board['5']==board['9']!=' ':
                printboard(board)
                print("\nGame Over.\n")
                print(" **** " +turn + " won. ****")
                break
        #if neither X nor O wins and the board is full, we'll declare the result as a tie
        if count==9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
        #now we will change the player after every move
        if turn=='X':
            turn='O'
        else:
            turn='X'
        #now we will ask if the players want to restart the game or not
    restart=input("Do you want to play Again?(Yes/No)")
    if restart=='Yes' or restart=='yes' or restart=='Y' or restart=='y' or restart=='YES':
        for key in boardkeys:
            board[key]=' '
        game()
if __name__=="__main__":
    game()