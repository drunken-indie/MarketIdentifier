#  @author Muyideen Jimoh -- jimohma
#  @date 04/05/2017
#  @file The_ships.py

class Ships:


    SHIP_SIZE  = 4
    MAX_GRID = 10
    MIN_GRID = 1

    def __init__(self, ship1, ship2, ship3): ## When you pass an argument
                                              ## to this constructor, it should be the size of your ships
                                              ## e.g Ships(3, 4, 5) ....UPDATE... It could intead be a list of ships position that the player wants to put their ships7
                                              ## e.g ship1 = [(2,3),(2,4),(2,5)]  ## ship2 = [(2,1),(3,1),(4,1),(5,1)] ## ship3 = [(10,3),(10,4),(10,5),(10,6),(10,7)]
                                              ## Ships(ship1, ship2, ship3)
        
        self.Titanic = ship1  ## ship size must be 4 for it to be valid
        self.Hokage = ship2    ## ship size must be 4 for it to be valid
        self.Kazekage = ship3   ##ship size must be 4 for it to be valid

    def ship_Titanic(self): ## Placement should be a list of the position the player wantes to put their ship

        if len(self.Titanic) != self.SHIP_SIZE:
            raise WRONG_SHIP_SIZE("The Size of this ship must be 4 in length ")

        for index in self.Titanic:
            if index[0] > self.MAX_GRID or index[1] > self.MAX_GRID or index[0] < self.MIN_GRID or index[1] < self.MIN_GRID:
                raise INVALID_SHIP_PLACEMENT("The placement of this ship is invalid ")
        
        return self.Titanic

    def ship_Hokage(self):
        
        if len(self.Hokage) != self.SHIP_SIZE:
            raise WRONG_SHIP_SIZE("The Size of this ship must be 4 in length ")

        for index in self.Hokage:
            if index[0] > self.MAX_GRID or index[1] > self.MAX_GRID or index[0] < self.MIN_GRID or index[1] < self.MIN_GRID:
                raise INVALID_SHIP_PLACEMENT("The placement of this ship is invalid ")

        return self.Hokage

    def ship_Kazekage(self):
        
        if len(self.Kazekage) != self.SHIP_SIZE:
            raise WRONG_SHIP_SIZE("The Size of this ship must be 4 in length ")

        for index in self.Kazekage:
            if index[0] > self.MAX_GRID or index[1] > self.MAX_GRID or index[0] < self.MIN_GRID or index[1] < self.MIN_GRID:
                raise INVALID_SHIP_PLACEMENT("The placement of this ship is invalid ")

        return self.Kazekage

class WRONG_SHIP_SIZE(Exception):
    def __init__(self, wrong_size):
        self.msg = wrong_size

    def __str__(self):
        return str(self.msg)

class INVALID_SHIP_PLACEMENT(Exception):
    def __init__(self, invalid):
        self.msg = invalid

    def __str__(self):
        return str(self.msg)

