#  @author Muyideen Jimoh -- jimohma
#  @date 04/05/2017
#  @file testBattleship.py

import unittest
from Board import *
from The_ships import *
from Gameplay import *



class BattleshipTesting(unittest.TestCase):

    def setUp(self):

        self.grid1 = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            ,[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
            ,[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]

        ## These are the valid ship coordinates
        self.ship1 = [(2,3),(2,4),(2,5),(2,6)]
        self.ship2 = [(2,1),(3,1),(4,1),(5,1)] 
        self.ship3 = [(10,3),(10,4),(10,5),(10,6)]
        
        self.player1 = Ships(self.ship1, self.ship2, self.ship3)

        ## These are the invalid ship coordinates
        self.ship11 = [(2,3)]
        self.ship22 = [(2,1),(3,1)] 
        self.ship33 = [(10,3),(10,4),(10,5)]
        
        self.player2 = Ships(self.ship11, self.ship22, self.ship33)

        self.p1_Board = Board()
        self.p2_Board = Board()

        ## Marker for a hit or miss on the board
        self.hit = 'O'
        self.miss = 'X'

        
        
        self.p1Ship1 = [(2,1),(3,1),(4,1),(5,1)]
        self.p1Ship2 = [(1,7),(1,8),(1,9),(1,10)]
        self.p1Ship3 = [(10,7),(10,8),(10,9),(10,10)]
    
        self.p2Ship1 = [(5,3),(6,3),(7,3),(8,3)]
        self.p2Ship2 = [(5,4),(6,4),(7,4),(8,4)]
        self.p2Ship3 = [(5,5),(6,5),(7,5),(8,5)]

        self.PP1 = Ships(self.p1Ship1, self.p1Ship2, self.p1Ship3)

        self.PP2 = Ships(self.p2Ship1, self.p2Ship2, self.p2Ship3)

        self.p1Fire = [(5,3),(6,3),(7,3),(8,3),(5,4),(6,4),(7,4),(8,4),(5,5),(6,5),(7,5),(8,5)]

        self.p11Fire = [(5,3),(6,3),(7,3),(8,3),(5,4),(6,4),(7,4),(4,6),(5,5),(3,1),(4,5),(10,9)]

        self.p2Fire = [(3,9),(2,2),(3,3),(6,1),(8,2),(6,4),(8,9),(4,6),(5,5),(3,1),(4,5),(10,9)]

        self.Go = GamePlay(self.PP1, self.PP2, self.p1Fire, self.p2Fire)

        self.Go_1 = GamePlay(self.PP1, self.PP2, self.p11Fire, self.p2Fire)

    def tearDown(self):
        
        self.grid1 = None
        
        self.ship1 = None
        self.ship2 = None 
        self.ship3 = None
        
        self.player1 = None

        self.ship11 = None
        self.ship22 = None 
        self.ship33 = None
        
        self.player2 = None

        self.p1_Board = None
        self.p2_Board = None


        self.p1Ship1 = None
        self.p1Ship2 = None
        self.p1Ship3 = None
    
        self.p2Ship1 = None
        self.p2Ship2 = None
        self.p2Ship3 = None

        self.PP1 = None

        self.PP2 = None

        self.p1Fire = None
        self.p11Fire = None
        
        self.p2Fire = None
        self.Go = None

        self.Go_1 = None
        
## Testing the Board Module
#####################################################################
    def test_get_state(self):
        
        ## Testing the set and get method for board with valid coordinates
        self.p1_Board.set_state(self.grid1, 1, 1, self.miss)
        self.assertEqual(self.p1_Board.get_state(self.grid1, 1, 1), 'X')

    def test_Set_state(self):
        
        ## Testing the set and get method for board with invalid coordinates
        self.assertRaises(Exception, self.p1_Board.set_state(self.grid1, -15, -5, 'O'))
        
    ## Testing the set and get method for board with invalid coordinates
    def test_set_state2(self):
        
        self.assertRaises(Exception, self.p1_Board.set_state(self.grid1, 100, 100, 'X'))
######################################################################################
## End of testing the Board Module
    

## Testing the Ship Module
#####################################################################
    def test_ships(self):

        ## Test for returning the ships
        self.assertEqual(self.player1.ship_Titanic(), self.ship1)
        self.assertEqual(self.player1.ship_Hokage(), self.ship2)
        self.assertEqual(self.player1.ship_Kazekage(), self.ship3)

    def test_ship1Exception(self):

        ## Test for raising exception for invalid ship sizes
        self.assertRaises(Exception,self.player2.ship_Titanic())
        
    def test_ship2Exception(self):
        self.assertRaises(Exception,self.player2.ship_Hokage())

    def test_ship3Exception(self):
        self.assertRaises(Exception,self.player2.ship_Kazekage())
######################################################################################
## End of testing the Ship Module


## Testing the Gameplay Module
#####################################################################
    ## Testing to see if player 1 wins the game
    def test_gameplay(self):

        self.assertEqual(self.Go.play(), "Player 1")

        ## Testing to see if a message is printed for player 1
        self.message = self.Go.play()
        self.winner = self.Go.winner_mssg(self.message)
        self.assertEqual(self.winner, "Player 1 won this game of Battleship")

    ## Testing to see if there is a tie between the two players
    def test_gameplay_tie(self):
            
        self.assertEqual(self.Go_1.play(), "The game is tie")

        ## Testing to see if a message is printed when the game ends with no winner
        self.message = self.Go_1.play()
        self.winner = self.Go.winner_mssg(self.message)
        self.assertEqual(self.winner, "There is no winner! ")
######################################################################################
## End of testing the Gameplay Module

unittest.main()
        
        
    

    
    

        


