board = { '1':' ','2':' ','3':' ',
       '4':' ','5':' ','6':' ',
       '7':' ','8':' ','9':' '}
def printboard(board):
    print(board['1']+ '|'+board['2']+'|'+board['3'])
    print('------')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('------')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game():
    turn='x'
    count=0
    for i in range(10):
        printboard(board)
        print("its your turn mr. "+turn+" at which palce you want to put")
        move=input()
        if(board[move]==' '):
            board[move]=turn
            count+=1
        else:
            print("selected place is not empty choose another on")
            continue
        if(count>=5):
            if(board['1']==board['2']==board['3']!=' '):
                printboard(board)
                print("mr. "+ turn+" wins the game")

                break
            elif(board['4']==board['5']==board['6']!=' '):
                printboard(board)
                print("mr. "+ turn+" wins the game")
                break
            elif(board['7']==board['8']==board['9']!=' '):
                printboard(board)
                print("mr. "+ turn+" wins the game")
                break
            elif(board['1']==board['5']==board['9']!=' '):
                printboard(board)
                print("mr. "+ turn+" wins the game")
                break
            elif(board['3']==board['5']==board['7']!=' '):
                printboard(board)
                print("mr. "+ turn+" wins the game")
                break

        if(turn=='x'):
            turn='0'
        else:
            turn='x'

    print("do you want to play again:Y/N")
    a=input()
    if(a=='y' or a=='Y'):
        game()


game()