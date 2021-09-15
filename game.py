import random
import time

from card import Card
from nemesisCard import NemesisCard
from nemesis import Nemesis
from player import Player


class Game:

    characterArray = {
        "Mist": {
                "power": 1, "maxCharge": 4, "starterBreach": [0,0,3,4], "deck": [],"hand" : []
        }
    }

    def __init__(self, nbPlayers):
        self.nbPlayers = nbPlayers
        self.nemesisName = "empty"
        self.nemesis = None
        self.mainMenu = True
        self.characterSelect = False
        self.characterList = ["Mist", "Jian","a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
        self.characterSelected = []
        self.playerList = []
        self.deckOrder = []
        self.discardDeckOder = []
        self.gemDeck = []
        self.relicDeck = []
        self.spellDeck = []
        self.reserveDeck = []
        self.reserveDeckCount = [7, 7, 7, 5, 5, 5, 5, 5, 5]
        self.isPlaying = True
        self.win = None
        self.chooseEffect = []
        self.isPossibleChooseEffect = []
        self.waitingForPlayerChoice = False


    def setNbPlayers(self,stringPlayers):
        self.nbPlayers = stringPlayers.split("-")[1]

    def setNemesisName(self,nemesis):
        self.nemesisName = nemesis.split("-")[1]

    def setupNemesis(self):
        self.nemesis = Nemesis(self.nemesisName)
        self.nemesis.setupNemesis(self.nbPlayers)
        self.mainMenu = False

    def setPlayer(self,index,name):
        self.characterSelected[index] = name

    def launchGame(self):
        #self.createDeckOrder()
        self.createTestDeckOrder()
        self.createAllCards()
        self.createReserve()
        self.createPlayerSetup()
        self.nemesis.additionnalSetup()

    def gameIsOver(self, boolean):
        self.win = boolean
        self.isPlaying = False

    def doNemesisTurn(self):
        self.doNemesisBoard()
        self.nemesisDrawCard()

    def nemesisDrawCard(self):
        if not self.nemesis.nemesisDeck:
            if not self.nemesis.nemesisBoard:
                self.gameIsOver(True)
        else:
            card = self.nemesis.drawNemesisCard()
            self.doNemesisCard(False, card)

    def doNemesisBoard(self):
        if not self.nemesis.nemesisBoard:
            for card in self.nemesis.nemesisBoard:
                self.doNemesisCard(True, card)

    def doNemesisCard(self, boolean, nemesisCard):
        if nemesisCard.cardType == "Serviteur":
            self.doServiteurEffect(boolean,nemesisCard)
        elif nemesisCard.cardType == "Pouvoir":
            self.doCardPowerEffect(boolean,nemesisCard)
        elif nemesisCard.cardType == "Attaque":
            self.doAttaqueEffect(nemesisCard)

    def checkEffet(self, effect):
        self.isPossibleChooseEffect = [False, False]
        isPossible = False
        if effect =="065":
            for player in self.playerList:
                if player.charge > 0:
                    isPossible = True
                    self.isPossibleChooseEffect[1] = True
                if player.spellBoard:
                    self.isPossibleChooseEffect[0] = True
                    isPossible = True
        return isPossible

    def doServiteurEffect(self,alreadyOnBoard,nemesisCard):
        if alreadyOnBoard:
            effectNumber = nemesisCard.cardEffect
            #Souffle Du Labyrinthe
            if effectNumber == "065":
                if self.checkEffect("065"):
                    self.chooseNemesisEffect(1, 2)

    def doChoosenEffect(self,codeEffect,player):
        #1 - Discard Prepared Spell
        #2 - Loose 1 charge
        if codeEffect == 1:
            player.discardSpell(1)
        elif codeEffect == 2:
            player.looseCharge(1)

        self.waitingForPlayerChoice = False


    def chooseNemesisEffect(self,codeFirstEffect,codeSecondEffect):
        self.chooseEffect = [codeFirstEffect, codeSecondEffect]
        self.waitingForPlayerChoice = True
        while self.waitingForPlayerChoice:
            time.sleep(1)

    def createPlayerSetup(self):
        i = 1
        for char in self.characterSelected:
            player = Player(char, i, Game.characterArray[char]["power"], Game.characterArray[char]["maxCharge"], Game.characterArray[char]["starterBreach"], Game.characterArray[char]["deck"], Game.characterArray[char]["hand"])
            self.playerList.extend(player)
            i += 1


    def createReserve(self):
        random.shuffle(self.gemDeck)
        random.shuffle(self.relicDeck)
        random.shuffle(self.spellDeck)
        firstGem = self.getReserveCard("Gemme",0,3)
        secondGem = self.getReserveCard("Gemme",3,4)
        thirdGem = self.getReserveCard("Gemme",5,6)
        firstRelic = self.getReserveCard("Relic",1,4)
        secondRelic = self.getReserveCard("Relic",4,8)
        firstSpell = self.getReserveCard("Spell",1,3)
        secondSpell = self.getReserveCard("Spell",3,4)
        thirdSpell = self.getReserveCard("Spell",4,5)
        fourthSpell = self.getReserveCard("Spell",6,9)
        self.reserveDeck.extend([firstGem,secondGem,thirdGem,firstRelic,secondRelic,firstSpell,secondSpell,thirdSpell,fourthSpell])
        for card in self.reserveDeck:
            print(card.cardName)


    def getReserveCard(self,type,min,max):
        keepLooping = True
        print("GetReserveCard " + type + " Min " + str(min) + " Max " +  str(max))
        while keepLooping:
            if type == "Gemme":
                card = self.gemDeck[random.randint(0, len(self.gemDeck) - 1)]
                print("Checking " + card.cardName)
                if card.cardCost >= min and card.cardCost <= max:
                    print("Accepted " + card.cardName)
                    self.gemDeck.remove(card)
                    keepLooping = False
            elif type == "Relic":
                card = self.relicDeck[random.randint(0,len(self.relicDeck) - 1)]
                if card.cardCost >= min and card.cardCost <= max:
                    self.relicDeck.remove(card)
                    keepLooping = False
            elif type == "Spell":
                card = self.spellDeck[random.randint(0,len(self.spellDeck) - 1)]
                if card.cardCost >= min and card.cardCost <= max:
                    self.spellDeck.remove(card)
                    keepLooping = False

        return card

    def createDeckOrder(self):
        if int(self.nbPlayers) == 1:
            self.deckOrder = [1,1,1,0,0]
        elif int(self.nbPlayers) == 2:
            self.deckOrder = [1, 1, 2, 2, 0, 0]
        elif int(self.nbPlayers) == 3:
            self.deckOrder = [1, 2, 3, 5, 0, 0]
        elif int(self.nbPlayers) == 4:
            self.deckOrder = [1, 2, 3, 4, 0, 0]

        random.shuffle(self.deckOrder)

    def createTestDeckOrder(self):
        self.deckOrder = [0, 0, 1, 2]


    def createAllCards(self):
        self.createGemCards()
        self.createRelicCards()
        self.createSpellCards()

    def createGemCards(self):
        elementExtraterrestre = Card("Gemme", "Élément Extraterrestre", "004", 4)
        beryliteHantee = Card("Gemme", "Beylite Hantée", "011",3)
        pierreDeDouleur = Card("Gemme", "Pierre De Douleur", "018", 6)
        opaleBrulante = Card("Gemme", "Opale Brûlante", "56", 5)
        saphirNuageux = Card("Gemme", "Saphir Nuageux", "62", 6)
        agregatDeDiamants = Card("Gemme", "Agrégat De Diamants", "69", 4)
        jade = Card("Gemme","Jade","76",2)
        rubisFulgurant = Card("Gemme", "Rubis Fulgurant", "83", 4)
        perleFiltrante = Card("Gemme", "PerleFiltrante", "90", 3)
        ambreDeBRisbois = Card("Gemme", "Ambre De V'Risbois", "9788",3)
        agateSangsue = Card("Gemme", "Agate Sangsue", "N02",3)
        scarabeeFossilise = Card("Gemme", "Scarabée Fossilisé", "V03",3)
        pierreDeSang = Card("Gemme", "Pierre De Sang", "W56", 6)
        mineraiDeLaBreche = Card("Gemme", "Minerai De La Brèche", "W63", 4)
        diamantInquietant = Card("Gemme", "Diamant Inquiétant", "W70",3)
        magnetiteCongelee = Card("Gemme", "Mangétite Congelée", "W84",3)
        bouquetDeScories = Card("Gemme", "Bouquet De Scories", "W91", 4)
        verrePyroclastique = Card("Gemme", "Verre Pyroclastique", "W98",3)
        self.gemDeck.extend([elementExtraterrestre,beryliteHantee,pierreDeDouleur,opaleBrulante,saphirNuageux,agregatDeDiamants,jade,
                             rubisFulgurant,perleFiltrante,ambreDeBRisbois,agateSangsue,scarabeeFossilise,pierreDeSang,mineraiDeLaBreche,
                             diamantInquietant,magnetiteCongelee,bouquetDeScories,verrePyroclastique])

    def createRelicCards(self):
        sphereDesSecrets = Card("Relic", "Sphère Des Secrets", "030", 3)
        batonDexplosion = Card("Relic", "Bâton D'explosion", "104", 3)
        vortexEnBouteille = Card("Relic", "Vortex En Bouteille", "109", 3)
        dagueFlechissante = Card("Relic", "Dague Fléchissante", "114", 2)
        orbeDeStabilisation = Card("Relic", "Orbe De Stabilisation", "119", 4)
        talismanDeMage = Card("Relic", "Talisman De Mage", "124", 5)
        cubeAstral = Card("Relic", "Cube Astral", "025", 5)
        prismeInstable = Card("Relic", "Prisme Instable", "129", 3)
        marteauEnFusion = Card("Relic", "Marteau En Fusion", "N09", 5)
        spiraleTemporelle = Card("Relic", "Spirale Temporelle", "N14", 7)
        cleDimensionnelle = Card("Relic", "Clé Dimensionnelle", "V10", 8)
        cachetDeLeternite = Card("Relic", "Cachet De L'éternité", "V15", 3)
        lingotErratique = Card("Relic", "Lingot Erratique", "W77", 5)
        boussoleDeCairn = Card("Relic", "Boussole De Cairn", "W105", 4)
        parcheminDuConclave = Card("Relic", "Parchemin Du Conclave", "W110", 3)
        attrapeurDeDemons = Card("Relic", "Attrapeur De Démons", "W115", 3)
        totemDeMage = Card("Relic", "Totem De Mage", "W120", 2)
        fetichePrimordial = Card("Relic", "Fétiche Primordial", "W125", 4)
        ganteletDeVorticite = Card("Relic", "Gantelet De Vorticité", "W130", 6)

        self.relicDeck.extend([sphereDesSecrets, dagueFlechissante, batonDexplosion, vortexEnBouteille, orbeDeStabilisation, talismanDeMage, cubeAstral, prismeInstable, marteauEnFusion, spiraleTemporelle, cleDimensionnelle,
                               cachetDeLeternite, lingotErratique, boussoleDeCairn, parcheminDuConclave, attrapeurDeDemons, totemDeMage, fetichePrimordial, ganteletDeVorticite])

    def createSpellCards(self):

        carboniser = Card("Spell", "Carboniser", "035", 8)
        catalyseur = Card("Spell", "Catalyseur", "040", 6)
        auraDeReaction = Card("Spell", "Aura De Réaction", "045", 5)
        conduitDuNeant = Card("Spell", "Conduit Du Néant", "050", 7)
        pyromancie = Card("Spell", "Pyromancie", "055", 7)
        calciner = Card("Spell", "Calciner", "060", 5)
        visionAplifiée = Card("Spell", "Vision Amplifiée", "134", 4)
        nexusDesArcanes = Card("Spell", "Nexus Des Arcanes", "139", 7)
        arcChaotique = Card("Spell", "Arc Chaotique", "144", 6)
        videDévorant = Card("Spell", "Vide Dévorant", "149", 7)
        feuObscur = Card("Spell", "Feu Obscur", "154", 5)
        volDessence = Card("Spell", "Vol D'Essence", "159", 5)
        eclairEnrage = Card("Spell", "Éclair Enragé", "164", 5)
        miseAFeu = Card("Spell", "Mise à Feu", "169", 4)
        tentaculeDeLave = Card("Spell", "Tentacule De Lave", "174", 4)
        vagueDoubli = Card("Spell", "Vague D'Oubli", "179", 5)
        flammeDuPhenix = Card("Spell", "Flamme Du Phénix", "184", 3)
        apercuPlanaire = Card("Spell", "Aperçu Planaire", "189", 6)
        echoSpectral = Card("Spell", "Écho Spectral", "194", 3)
        fouetArdent = Card("Spell", "Fouet Ardent", "199", 6)
        flamber = Card("Spell", "Flamber", "N19", 4)
        radiance = Card("Spell", "Radiance", "N24", 8)
        laMarqueDuSage = Card("Spell", "La Marque Du Sage", "N29", 7)
        eclairDeProphetie = Card("Spell", "Éclair De Prophétie", "N34", 6)
        resonance = Card("Spell", "Résonance", "V20", 6)
        embrassement = Card("Spell", "Embrassement", "V25", 2)
        fulminer = Card("Spell", "Fulminer", "V30", 5)
        feuInterieur = Card("Spell", "Feu Intérieur", "V36", 2)
        flechetteThermique = Card("Spell", "Fléchette Thermique", "V40", 4)
        aurore = Card("Spell", "Aurore", "W135", 5)
        carbonisation = Card("Spell", "Carbonisation", "W140", 4)
        conjurationDesOublies = Card("Spell", "Conjuration Des Oubliés", "W145", 6)
        flecheCeleste = Card("Spell", "Flèche Céleste", "W150", 5)
        champDeConvection = Card("Spell", "Champ De Convection", "W155", 5)
        cristallisation = Card("Spell", "Cristallisation", "W160", 8)
        equilibre = Card("Spell", "Équilibre", "W165", 7)
        torrentArdent = Card("Spell", "Torrent Ardent", "W170", 5)
        eclairDechirant = Card("Spell", "Éclair Déchirant", "W175", 4)
        meche = Card("Spell", "Mèche", "W180", 4)
        forgeNova = Card("Spell", "Forge Nova", "W185", 6)
        affluxPyrotechnique = Card("Spell", "Afflux Pyrotechnique", "W190", 4)
        retourALaPoussiere = Card("Spell", "Retour À La Poussière", "W195", 7)
        familierImaginaire = Card("Spell", "Familier Imaginaire", "W200", 3)

        self.spellDeck.extend([carboniser, catalyseur, auraDeReaction, conduitDuNeant, pyromancie, calciner, visionAplifiée, nexusDesArcanes, arcChaotique, videDévorant, feuObscur, volDessence,
                               eclairEnrage, miseAFeu, tentaculeDeLave, vagueDoubli, flammeDuPhenix, apercuPlanaire, echoSpectral, fouetArdent, flamber, radiance, laMarqueDuSage, eclairDeProphetie,
                               resonance, embrassement, fulminer, feuInterieur, flechetteThermique, aurore, carbonisation, conjurationDesOublies, flecheCeleste, champDeConvection, cristallisation,
                               equilibre, torrentArdent, eclairDechirant, meche, forgeNova, affluxPyrotechnique, retourALaPoussiere, familierImaginaire])






