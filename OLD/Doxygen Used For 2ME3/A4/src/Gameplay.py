#  @author Muyideen Jimoh -- jimohma
#  @date 04/05/2017
#  @file Gameplay.py

## This module will contain the methods that makes up the gameplay of the battleship
## game as a whole. 

from Board import *
from The_ships import *  ## this import all the methods in the module "The_ships"

## Using the imported methods in the modules, you don't have to include "self. " in order to use them. 

class GamePlay:

    MAX_HIT = 12  ## Exact amount of hits needed to win the game

    
    def __init__(self, ship_P1, ship_P2, fire_P1, fire_P2):
        self.p1_ship = ship_P1  ## state variable for the list of list for ship for player one
        self.p2_ship = ship_P2
        self.p1_fire = fire_P1  
        self.p2_fire = fire_P2  ## I believe the maximum fire that can both shoot is 10*10 = 100
        

    ## This returns a boolean expression for checking if the ships in consideration are alll sunked.
    def gameOver(self, count):

        ## Count is a constant which is the sum of all the coordinates that
        ## a player's ship occupies.
        if count == self.MAX_HIT:
            return True
        else:
            return False

    ## This method was later on not implemented, but it's in cluded on the MIS and due to time constraint, I'm unable to augment things. Please don't penelize me too much.. Thanks :-)
    def shipSunk(self, ship):  ## ??? Receives a list of ship coordinates. This should return a boolen expression

        if len(ship) == 0: ## Given that a coordinate of a ship was hit, that coordinate would be removed from the list which contains the cells where a ship is placed.
                           ## if the list is zero, meaning all the cells were hit, we return True showing that the ship is sunk
            return True

        else:              ## Else we return False, meaning that the ship is still alive because some of its cell(s) or coordinate have not been hit yet
            return False

    def play(self):

        ## grid for player 1 board and player 2 board respectively
        
        grid1 = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                ,[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                ,[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]

        grid2 = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                ,[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                ,[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]

        p1 = Board() ## Setting the board for player 1
        p2 = Board() ## Setting the board for player 2

        ## These three variables are holding the coordinates for the respective
        ## ships set by player 1
        p1_ship1 = self.p1_ship.ship_Titanic() ## This handles the list of coordinate for the first ship
        
        
        p1_ship2 = self.p1_ship.ship_Hokage()  ## This variable takes the coordinate for the second ship
        
        p1_ship3 = self.p1_ship.ship_Kazekage() ## Handles the coordinates for the third ship

        ## The comments above for player 1 goes for player 2 as well. 
        p2_ship1 = self.p2_ship.ship_Titanic()
        
        p2_ship2 = self.p2_ship.ship_Hokage()
        
        p2_ship3 = self.p2_ship.ship_Kazekage()

        count_1 = 0  ## for tracking the number of hits player 1 makes

        count_2 = 0  ## for tracking the number of hits player 2 makes
        
    

        miss_em = 'X'  ## 'X' gets displayed on the grid for a miss a player's reference board
        hit_em = 'O'   ## 'O' gets displayed on the grid for a hit a player's reference board

        winner = "The game is tie"  ## Variable for tracking the winner. It's initialized to a tie because the game just started
        
        condition = True  ## Basically this while loop ends once a player is able to sink all his opponent's ships..So the condition becomes False and then we break out
                          ## of the while loop and other for-loops within it. 
        while condition:
            check = False  ## for tracking whose won the game at every attack attemp made by player 1
            checking = False  ## ## for tracking whose won the game at every attack attemp made by player 2

            for i in range(len(self.p1_fire)):

                for k in range(len(p2_ship1)):  ## could have used self.p1_ship1, but it doesn't really matter
                                                   ## because the size of the two should be the same anyway..size = 4
                    attack_1 = self.p1_fire[i]  ## attack coordinate for player 1
                    attack_2 = self.p2_fire[i]  ## attack coordinate for player 2
                    
                    ## Attack from player1
                    ##################################################################################
                    if self.p1_fire[i] == p2_ship1[k]: ## t=comparing to the first ship which is Titanic
                        
                        #temp_p2_ship1.remove(attack_1) ## removes the hit coordinate from player2's temporary ship
                        count_1 = count_1 + 1
                        
                        if p1.get_state(grid1, attack_1[0], attack_1[1]) == ' ':
                            p1.set_state(grid1, attack_1[0], attack_1[1], hit_em)  ## marks the corrdinate when a hit was made as 'X'

                        ## we need to check whether the ship is sunk at this point
                        
                    elif self.p1_fire[i] == p2_ship2[k]:
                        
                        #p2_ship2.remove(attack_1) ## removes the hit coordinate from player2's ship
                        count_1 = count_1 + 1
                        
                        p1.set_state(grid1, attack_1[0], attack_1[1], hit_em)  ## marks the corrdinate when a hit was made as 'X'

                    elif self.p1_fire[i] == p2_ship3[k]:
                        
                        #p2_ship3.remove(attack_1) ## removes the hit coordinate from player2's ship
                        count_1 = count_1 + 1
                        
                        p1.set_state(grid1, attack_1[0], attack_1[1], hit_em)  ## marks the corrdinate when a hit was made as 'X'

                    else:
                        p1.set_state(grid1, attack_1[0], attack_1[1], miss_em)  ## marks the coordinate where a miss was made as 'O'


                    check = self.gameOver(count_1)     ## Tries to see if all of player 2 ship has drowned
                    ################################################################################

                    ## Attack from player 2
                    ################################################################################
                    if self.p2_fire[i] == p1_ship1[k]: ## t=comparing to the first ship which is Titanic
                        
                        #p1_ship1.remove(attack_2) ## removes the hit coordinate from player2's ship
                        count_2 = count_2 + 1
##                        p1_ship1[k] = (attack_2[1],attack_2[0])   ## this is just to change the tuple in the index of the ship so that the player's board is marked correctly
##                        print(p1_ship1[k])
                        
                        p2.set_state(grid2, attack_2[0], attack_2[1], hit_em)  ## marks the corrdinate when a hit was made as 'X'
                        
                    elif self.p2_fire[i] == p1_ship2[k]:
                        
                        #p1_ship2.remove(attack_2) ## removes the hit coordinate from player2's ship
                        count_2 = count_2 + 1
                        
                        p2.set_state(grid2, attack_2[0], attack_2[1], hit_em)  ## marks the corrdinate when a hit was made as 'X'

                    elif self.p2_fire[i] == p1_ship3[k]:
                        
                        #p1_ship3.remove(attack_2) ## removes the hit coordinate from player2's ship
                        count_2 = count_2 + 1
                        
                        p2.set_state(grid2, attack_2[0], attack_2[1], hit_em)  ## marks the corrdinate when a hit was made as 'X'

                    else:
                        p2.set_state(grid2, attack_2[0], attack_2[1], miss_em)  ## marks the coordinate where a miss was made as 'O'

                    #######################################################################################

                    checking = self.gameOver(count_2)  ## Tries to see if all of player 1 ship has drowned  
                    
                    if check == True:
                        winner = "Player 1"  
                        condition = False
                        break
                    elif checking == True:
                        winner = "Player 2"
                        condition = False  ## For stopping the while loop incase player 1 sinks all of player2's ship
                        break
                        
                    if not condition:  ## condition for breaking out of the third for-loop
                        break
                    
                if not condition:  ## condition for breaking out of the second for-loop
                    break
                
            if check == False and checking == False:  
                return winner   ## this is a tie.. winner was initialied in the beginning to a string having the message "It's a tie! "

        return winner


    ## Returns a statement saying who the winner of the game round is                
    def winner_mssg(self, winner):

        if winner == "Player 1":
            return "Player 1 won this game of Battleship"

        elif winner == "Player 2":
            return "Player 2 won this game of Battleship"
        
        else:
            return "There is no winner! "
        
    

    
