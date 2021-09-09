from nemesisCard import NemesisCard
class Nemesis:
    def __init__(self, nemesisName):
        self.nemesisName = nemesisName
        self.health = None
        self.nemesisDeck = []
        self.switcher = {"Rage": 70}

    def setupNemesis(self,nbPlayers):
        self.health = self.switcher[self.nemesisName]
        self.createNemesisDeck(nbPlayers)


    def createNemesisDeck(self,nbPlayers):
        cardLevel1 = []

        print("create Nemesis deck")


















