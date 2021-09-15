import pygame
from button import Button

class Window:
    def __init__(self):
        self.listBtnPlayers = []
        self.listBtnNemesis = []
        self.listBtnCharacters = []
        self.listBtnChoice = []
        self.playerBreach = [[],[],[],[]]
        self.xMax = 1500
        self.yMax = 800
        self.btnStartGame = Button("Start",600,675,(255, 0, 0))
        self.cancelBtn = Button("Annuler",1100,30,(255, 0, 0))
        self.launchGameBtn = Button("Start", 1100, 150, (0, 255, 0))
        self.gameDisplay = pygame.display.set_mode((self.xMax, self.yMax))
        self.gameDisplay.fill((255, 255, 255))
        pygame.display.set_caption("Aeon's End")
        self.choiceLabel = {
            1 : "Un joueur défausse un sort préparé",
            2 : "Un joueur perd 1 charge"
        }

    def createStartMenuWindow(self):
        pygame.draw.rect(self.gameDisplay, (0, 125, 255), pygame.Rect(30, 30, 300, 60))
        self.drawText("Nombre de joueurs :", (30, 30), (0, 0, 0))
        #Create Players buttons
        btnPlayer1 = Button("player-1",30,100,(0, 0, 0))
        btnPlayer1.draw(self.gameDisplay)
        self.listBtnPlayers.append(btnPlayer1)
        btnPlayer2 = Button("player-2",30,200,(0, 0, 0))
        btnPlayer2.draw(self.gameDisplay)
        self.listBtnPlayers.append(btnPlayer2)
        btnPlayer3 = Button("player-3",30,300,(0, 0, 0))
        btnPlayer3.draw(self.gameDisplay)
        self.listBtnPlayers.append(btnPlayer3)
        btnPlayer4 = Button("player-4",30,400,(0, 0, 0))
        btnPlayer4.draw(self.gameDisplay)
        self.listBtnPlayers.append(btnPlayer4)
        #Create Nemesis buttons
        pygame.draw.rect(self.gameDisplay, (0, 125, 255), pygame.Rect(300, 30, 300, 60))
        self.drawText("Némesis", (300, 30),(0, 0, 0))
        btnNemesis1 = Button("nemesis-Rage",200,100,(255, 0, 0))
        btnNemesis1.draw(self.gameDisplay)
        self.listBtnNemesis.append(btnNemesis1)
        btnNemesis2 = Button("nemesis-Mask",200,200,(255, 0, 0))
        btnNemesis2.draw(self.gameDisplay)
        self.listBtnNemesis.append(btnNemesis2)
        #Create Start Button
        self.btnStartGame.draw(self.gameDisplay)

    def displayNumberOfPlayer(self, number):
        self.gameDisplay.fill((0, 125, 255), (250, 30, 30, 30))
        self.drawText(number, (230, 30), (0, 0, 0) )

    def displayNemesis(self, nemesis):
        self.gameDisplay.fill((0, 125, 255), (430, 30, 60, 30))
        self.drawText(nemesis, (430, 30), (0, 0, 0))

    def createCharacterView(self,game):
        self.gameDisplay.fill((255, 255, 255))
        imageNemesis = pygame.image.load("ressources/nemesis/RI.png").convert_alpha()
        self.gameDisplay.blit(imageNemesis, (750,0))
        self.createCharacterList(game)
        game.characterSelect = True


    def createCharacterList(self,game):
        x = 0
        y = 325
        for character in game.characterList:
            btnCharacter = Button(character, x, y, (0, 0, 0))
            btnCharacter.draw(self.gameDisplay)
            self.listBtnCharacters.append(btnCharacter)
            y += 120
            if y >= self.yMax - 120:
                x += 200
                y = 325

        z = 30
        for i in range(int(game.nbPlayers)):
            self.drawText("Sélectionner le Joueur " + str(i + 1) + " : ", (30, z), (0, 0, 0))
            z += 50
            game.characterSelected = [None] * int(game.nbPlayers)


        self.cancelBtn.draw(self.gameDisplay)
        self.launchGameBtn.draw(self.gameDisplay)



    def selectCharacters(self,game,btn):
        for char in game.characterSelected:
            if char is None:
                index = game.characterSelected.index(char)
                self.displayCharacterSelected(btn.text, index + 1)
                game.setPlayer(index,btn.text)
                break

    def displayCharacterSelected(self,characterName,playerNumber):
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render(characterName, 1, (0, 0, 0))
        self.gameDisplay.blit(text, (320, 30 + 50 * (playerNumber-1)))

    def resetCharacter(self,game):
        game.characterSelected = [None] * int(game.nbPlayers)
        self.gameDisplay.fill((255, 255, 255), (320,30,60,230))

    def launchGame(self,game):
        game.characterSelect = False
        self.gameDisplay.fill((255, 255, 255))
        imageNemesis = pygame.image.load("ressources/nemesis/RI.png").convert_alpha()
        self.gameDisplay.blit(imageNemesis, (750,0))
        while game.isPlaying:
            if game.waitingForPlayerChoice:
                self.drawChoice(game)
            if game.deckOrder[0] == 0:
                game.deckOrder.remove(0)
                game.doNemesisTurn()
                self.drawNemesisTurn(game)
            elif game.deckOrder[0] > 0 and game.deckOrder[0] < 5:
                self.drawPlayerTurn(game.deckOrder[0])
            elif game.deckOrder[0] == 5:
                self.drawJokerTurn()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    for btnCh in self.listBtnChoice:
                        if btnCh.click(mouse) and game.waitingForPlayerChoice and btnCh.color == (0, 0, 200):
                            btn_key = list(self.choiceLabel.keys())[list(self.choiceLabel.values()).index(btnCh.text)]
                            if btn_key == 1:
                                self.checkSpellClick(game, mouse)
                            elif btn_key == 2:
                                self.drawText("Sélectionner un Joueur", (30, 30), (0, 0, 0))
                                self.choosePlayer(game, mouse, 2)

                            game.waitingForPlayerChoice = False
                        elif btnCh.click(mouse) and game.waitingForPlayerChoice and btnCh.color == (128, 128, 128):
                            print("Not possible btnCh")


    def choosePlayer(self, game, mouse, effect):
        y = 100
        self.listBtnPlayers = []

        for player in game.playerList:
            btnJoueur = Button(player.name,30,y,(0, 0, 0))
            y += 100
            self.listBtnPlayers.append(btnJoueur)

        for btn in self.listBtnPlayers:
            if btn.click(mouse) and game.waitingForPlayerChoice:
                if game.playerList[self.listBtnPlayers.index(btn)].checkEffet(effect):
                    game.playerList[self.listBtnPlayers.index(btn)].doEffect(effect)


    def checkSpellClick(self, game, mouse):
        self.drawText("Sélectionner un sort", (30, 30), (0, 0, 0))
        for playerSpellUI in self.playerBreach:
            for spell in playerSpellUI:
                if spell.click(mouse) and game.waitingForPlayerChoice and spell and game.waitingForPlayerChoice:
                    game.playerList[self.playerBreach.index(playerSpellUI)].playerDiscardSpell(playerSpellUI.index(spell))



    def drawNemesisTurn(self, game):
        #Todo draw Nemesis Turn
        for nemesisCard in game.nemesis.nemesisBoard:
            self.drawNemesisCard(nemesisCard)

    def drawNemesisCard(self, nemesisCard):
        print("Draw" + nemesisCard.name)

    def drawChoice(self, game):
        grey = pygame.color(128,128,128)
        blue = pygame.color(0, 0, 200)
        for choice in game.chooseEffect:
            if game.isPossibleChooseEffect[game.chooseEffect.index(choice)]:
                color = blue
            else:
                color = grey
            y = 30
            text = self.window.choiceLabel[choice]
            btnChoice = Button(text, 30, y, color)
            btnChoice.draw(self.gameDisplay)
            self.listBtnChoice.extend(btnChoice)
            y += 70


    def drawText(self, text, pos, color):
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render(text, 1, color)
        self.gameDisplay.blit(text,pos)