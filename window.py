import pygame
from button import Button

class Window:
    def __init__(self):
        self.listBtnPlayers = []
        self.listBtnNemesis = []
        self.btnStartGame = Button("start",600,600,(255, 0, 0))
        self.gameDisplay = pygame.display.set_mode((1500, 800))
        self.gameDisplay.fill((255, 255, 255))
        pygame.display.set_caption("Aeon's End")

    def createStartMenuWindow(self):
        pygame.draw.rect(self.gameDisplay, (0, 125, 255), pygame.Rect(30, 30, 300, 60))
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render("Nombre de joueurs : ", 1, (0, 0, 0))
        self.gameDisplay.blit(text, (30, 30))
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
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render("Némésis : ", 1, (0, 0, 0))
        self.gameDisplay.blit(text, (300, 30))
        btnNemesis1 = Button("nemesis-Rage",200,100,(255, 0, 0))
        btnNemesis1.draw(self.gameDisplay)
        self.listBtnNemesis.append(btnNemesis1)
        btnNemesis2 = Button("nemesis-Mask",200,200,(255, 0, 0))
        btnNemesis2.draw(self.gameDisplay)
        self.listBtnNemesis.append(btnNemesis2)
        #Create Start Button
        self.btnStartGame.draw(self.gameDisplay)

    def displayNumberOfPlayer(self,number):
        self.gameDisplay.fill((0, 125, 255), (250, 30, 30, 30))
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render(number, 1, (0, 0, 0))
        self.gameDisplay.blit(text, (250, 30))

    def displayNemesis(self,nemesis):
        self.gameDisplay.fill((0, 125, 255), (430, 30, 60, 30))
        font = pygame.font.SysFont("comicsans", 30)
        text = font.render(nemesis, 1, (0, 0, 0))
        self.gameDisplay.blit(text, (430, 30))

    def createGameView(self,game):
        print("createGameView")
