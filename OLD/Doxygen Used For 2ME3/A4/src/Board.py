#  @author Muyideen Jimoh -- jimohma
#  @date 04/05/2017
#  @file Board.py

## Note: The grid of the battleship_Board is 10x10
## And, accessing the cells of the board would be done by tupples e.g (4,4) or (1,5) etc

class Board:

    MAX_SIZE = 10  ## Dimension in the x & y-direction of the 10 x 10 sized board

    ## This would also be a transition function on the MIS because it just resets the state of the board back to it's original state
    def init(self, grid):  ## Initialize the board back to its default state which is
                           ## a state of empty rows and columns

        if len(grid) != self.MAX_SIZE:
            raise WRONG_BOARD_SIZE("The size of the board has to be exactly 10 ")

        else:
            
            grid_length = len(grid)
            row_length = len(grid[0])
            
            for rows in range(grid_length):
                for cell in range(row_length):
                    grid[rows][cell] = ' '
    
    ## This method is used for getting the status of cells/position on the board
    def get_state(self, grid, row, col):

        if col > 10 or col < 1 or row > 10 or row < 1:
            raise INVALID_COORDINATE("The coordinate you're trying to get is invalid" )
        else:
            spot = grid[col-1][row-1] # We use col-1 & row-1 because python goes through a list
                                      # from 0. so if col& row was 2, we would get grid[1][1]
                                      # which would be the center position on the board
                                      ## On the MIS, This method can simply be described as: For i=0.....|grid| and For j=0....|grid| : grid[i][j]
            if spot == 'X': 
                return 'X'
            elif spot == 'O':
                return 'O'
            else:
                return ' '

    ## This function is a private method.. Meaning it's not visible on the MIS.. It workes out fine because I don't know how to write it formally on the MIS
            
    def __print_row(self, grid, row): ##this is for making the rows of the matrix
        if len(grid) != 10:
            raise WRONG_BOARD_SIZE("Board size must be exactly 10")

        output = self.get_state(grid, row, 1)
        output += '|' + self.get_state(grid, row, 2)
        output += '|' + self.get_state(grid, row, 3)
        output += '|' + self.get_state(grid, row, 4)
        output += '|' + self.get_state(grid, row, 5)
        output += '|' + self.get_state(grid, row, 6)
        output += '|' + self.get_state(grid, row, 7)
        output += '|' + self.get_state(grid, row, 8)
        output += '|' + self.get_state(grid, row, 9)
        output += '|' + self.get_state(grid, row, 10)
        print(output)

    ## This function is a private method.. Meaning it's not visible on the MIS..
        
    def __print_board(self, grid):  ## This method is responsible for displaying the board

        if len(grid) != 10:
            raise WRONG_BOARD_SIZE("Board size must be exactly 10")

        self.print_row(grid, 1)  ## first row of the board
        print('-------------------')
        self.print_row(grid, 2)  ## second row of the board
        print('-------------------')
        self.print_row(grid, 3)  ## third row of th board
        print('-------------------')
        self.print_row(grid, 4)
        print('-------------------')
        self.print_row(grid, 5)
        print('-------------------')
        self.print_row(grid, 6)
        print('-------------------')
        self.print_row(grid, 7)
        print('-------------------')
        self.print_row(grid, 8)
        print('-------------------')
        self.print_row(grid, 9)
        print('-------------------')
        self.print_row(grid, 10)
        return ' '##makes sure method doesn't return any unneccessary None on the command line
    
    
    ## This would be a transition function on the MIS.     
    def set_state(self, grid, row, col, player):
        if col > 10 or col < 1 or row > 10 or row < 1:
            raise INVALID_COORDINATE("The coordinate you're trying to get is invalid")
        
        else:
            if player == 'X':
                spot = 'X'
            else:
                spot = 'O'
            grid[col-1][row-1] = spot

class WRONG_BOARD_SIZE(Exception):
    def __init__(self, wrong_size):
        self.msg = wrong_size

    def __str__(self):
        return str(self.msg)

class INVALID_COORDINATE(Exception):
    def __init__(self, POSITION):
        self.msg = POSITION

    def __str__(self):
        return str(self.msg)



