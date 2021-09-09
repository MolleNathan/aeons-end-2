from nemesis import Nemesis
class Game:
    def __init__(self, nbPlayers):
        self.nbPlayers = nbPlayers
        self.nemesisName = "empty"
        self.nemesis = None


    def setNbPlayers(self,stringPlayers):
        self.nbPlayers = stringPlayers.split("-")[1]

    def setNemesisName(self,nemesis):
        self.nemesisName = nemesis.split("-")[1]

    def setupNemesis(self):
        self.nemesis = Nemesis(self.nemesisName)
        self.nemesis.setupNemesis(self.nbPlayers)








