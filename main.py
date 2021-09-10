
from pygame.locals import *
import pygame

from window import Window
from game import Game

if __name__ == '__main__':
    pygame.init()
    window = Window()
    game = Game(0)
    window.createStartMenuWindow()
    clock = pygame.time.Clock()
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                for btn in window.listBtnPlayers:
                    if btn.click(mouse):
                        game.setNbPlayers(btn.text)
                        window.displayNumberOfPlayer(game.nbPlayers)
                for btnN in window.listBtnNemesis:
                    if btnN.click(mouse):
                        game.setNemesisName(btnN.text)
                        window.displayNemesis(game.nemesisName)
                if window.btnStartGame.click(mouse):
                    if game.nemesisName != "empty" and game.nbPlayers:
                        game.setupNemesis()
                        window.createCharacterView(game)
            #print(event)
        pygame.display.update()
        clock.tick(60)

