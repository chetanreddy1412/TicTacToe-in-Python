class Board:
    
    def __init__(self):
        
        #The zeroth entry is a dummy position, used to make the indexing from 1 to 9
        self.entries = [' ' for i in range(10)]
        self.status = 'running'
        self.winner = None
        self.isdraw = False
        
    #__str__ is used to print the board
    def __str__(self):

        print('     |     |     ')
        print('  {}  |  {}  |  {}  '.format(*self.entries[1:4]))
        print('_____|_____|_____')

        print('     |     |     ')
        print('  {}  |  {}  |  {}  '.format(*self.entries[4:7]))
        print('_____|_____|_____')

        print('     |     |     ')
        print('  {}  |  {}  |  {}  '.format(*self.entries[7:10]))
        print('     |     |     ')
        
        return str()
    
    #this method adds the required mark at the desired position when called
    def add_entry(self, position,player_mark):
        self.entries[position] = player_mark
    
    #the board status and winner (if any) and draw (if the board is filled) is updated here     
    def update(self):
        
	#Checking if there is a winner and updating the board status
        cols = [(1,4,7),(2,5,8),(3,6,9)]
        rows = [(1,2,3),(4,5,6),(7,8,9)]
        diagonals = [(1,5,9),(3,5,7)]
        
        win_situations = cols+rows+diagonals
        
        for config in win_situations:
            if self.entries[config[0]]=='X' and self.entries[config[1]]=='X' and self.entries[config[2]]=='X':
                self.status = 'over'
                self.winner = 'X'
        
        for config in win_situations:
            if self.entries[config[0]]=='O' and self.entries[config[1]]=='O' and self.entries[config[2]]=='O':
                self.status = 'over'
                self.winner = 'O'
        
	#Checking if the game is drawn and updated the board status        
        if " " not in self.entries[1:]:
            self.status = 'over'
            self.isdraw = True            
    
    #This method is called when its the player's chance
    def player_move(self,player_name,player_mark):
        player_inp = input("{}'s ({}) Turn:".format(player_name,player_mark))
        
        if player_inp.isnumeric():
            player_entry = int(player_inp)
            if player_entry>0 and player_entry<10:
                if self.entries[player_entry]==' ':
                    self.add_entry(player_entry,player_mark)
                    
                else:
                    print('Filled Position Chosen')
                    print('=> CHANCE LOST')   
            
            else:
                print('Position Outside 1-9 Chosen')
                print('=> CHANCE LOST')  
        else:
            print('Invalid Entry Given')
            print('=> CHANCE LOST') 
   
    #this method is called when its the computer's chance        
    def computer_move(self,comp_mark):
        
        if comp_mark == 'X':
            player_mark = 'O'
        else:
            player_mark = 'X'
            
        cols = [(1,4,7),(2,5,8),(3,6,9)]
        rows = [(1,2,3),(4,5,6),(7,8,9)]
        diagonals = [(1,5,9),(3,5,7)]
        
        win_situations = cols+rows+diagonals #possible win configurations

        #If there is a Winning Move
        for config in win_situations:

            if self.entries[config[0]]==" " and self.entries[config[1]]==comp_mark and self.entries[config[2]]==comp_mark:
                self.add_entry(config[0],comp_mark)
                return

            elif self.entries[config[0]]==comp_mark and self.entries[config[1]]==" " and self.entries[config[2]]==comp_mark:
                self.add_entry(config[1],comp_mark)
                return

            elif self.entries[config[0]]==comp_mark and self.entries[config[1]]==comp_mark and self.entries[config[2]]==" ":
                self.add_entry(config[2],comp_mark)
                return

        #Blocking Move
        for config in win_situations:

            if self.entries[config[0]]==" " and self.entries[config[1]]==player_mark and self.entries[config[2]]==player_mark:
                self.add_entry(config[0],comp_mark)
                
                return

            if self.entries[config[0]]==player_mark and self.entries[config[1]]==" " and self.entries[config[2]]==player_mark:
                self.add_entry(config[1],comp_mark)
                return

            if self.entries[config[0]]==player_mark and self.entries[config[1]]==player_mark and self.entries[config[2]]==" ":
                self.add_entry(config[2],comp_mark)
                return

        #If there is no winning or Blocking move, best move is the central location if it is free
        if self.entries[5]==' ':
            self.add_entry(5,comp_mark)
            return

        #If none of the above 3 are executed, a random cell is filled
        import random
        
        empty_slots = [i+1 for i,element in enumerate(self.entries[1:]) if element==' ']
        self.add_entry(random.choice(empty_slots),comp_mark)
        
        return
    
    #this method is called whenever a new game is started
    def reset(self):
        self.entries = [' ' for i in range(10)]
        self.winner = None
        self.status = 'running'
        self.isdraw = False
    
def show_instructions():
        
        print('     |     |     ')
        print('  1  |  2  |  3  ')
        print('_____|_____|_____')
        print('     |     |     ')
        print('  4  |  5  |  6  ')
        print('_____|_____|_____')
        print('     |     |     ')
        print('  7  |  8  |  9  ')
        print('     |     |     ')

        print()

        print("- Each cell in the grid is represented by a number as shown.") 
        print("- When prompted, the player can fill the required unfilled cell by entering a number between 1 and 9")
        print("- The CHANCE IS LOST in 3 cases:") 
        print("  i.   The Player doesn't enter a numerical value")
        print("  ii.  The Player enters a number which is not between 1 and 9")
        print("  iii. The Player enters the position of a filled cell")          


def unit_move(board,player_name,player_mark):
    
    if player_name == 'Computer':
        board.computer_move(player_mark)
    else:
        board.player_move(player_name,player_mark)
    
    print(board)
    print("******************")
    board.update()

def appearance_page():
    print('**** TIC TAC TOE ****')
    print()
    
    show_instructions()
    print()
    
    print('1. Play against Friend')
    print('2. Play against Computer')
    print('3. Exit')

    
    for i in range(3):
        try:
            c = int(input('Please Enter a Choice (1,2,3):'))
            if c==1 or c==2 or c==3:
                break
            else: 
                print('Invalid Choice')
                if i ==2:
                    print('Maximum number of invalid choices over')
                    c = 3
                
        except:
            print('Invalid Choice')
            if i == 2:
                print('Maximum number of Invalid Choices Exceeded')
                c = 3
    
    
    return c


def main():

    board = Board()
    while True:
        c = appearance_page()

        if c == 3:
            print('Thanks You for Playing')
            break

        elif c == 1:
            player1_name = input('Enter Player 1 Name:')
            player2_name = input('Enter Player 2 Name:')

        elif c==2:
            player1_name = input('Enter Player Name:')
            player2_name = 'Computer'

        while True:
            board.reset()

            print(board)
            while True:

                unit_move(board,player1_name,'X')
                if board.status == 'over':
                    break
                unit_move(board,player2_name,'O')
                if board.status == 'over':
                    break

            if board.winner != None:
                if board.winner == 'X':
                    print('{} (X) WON !!'.format(player1_name))
                else:
                    print('{} (O) WON !!'.format(player2_name))

            else:
                assert(board.isdraw == True)
                print('Draw Game !')

            if_continue = input('Do you want to play another game (Y/N): ')

            if if_continue == 'y' or if_continue == 'Y':
                continue
            else:
                break


if __name__ == '__main__':
    main()
