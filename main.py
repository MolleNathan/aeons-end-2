
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
                #Select the number of Players
                for btn in window.listBtnPlayers:
                    if btn.click(mouse) and game.mainMenu:
                        game.setNbPlayers(btn.text)
                        window.displayNumberOfPlayer(game.nbPlayers)
                #Select the nemesis
                for btnN in window.listBtnNemesis:
                    if btnN.click(mouse) and game.mainMenu:
                        game.setNemesisName(btnN.text)
                        window.displayNemesis(game.nemesisName)
                if window.btnStartGame.click(mouse) and game.mainMenu:
                    if game.nemesisName != "empty" and game.nbPlayers:
                        game.setupNemesis()
                        window.createCharacterView(game)
                for btnC in window.listBtnCharacters:
                    if btnC.click(mouse) and game.characterSelect and btnC.text not in game.characterSelected:
                        #ajouter le perso à la list des persos joués
                        window.selectCharacters(game,btnC)
                if window.cancelBtn.click(mouse) and game.characterSelect:
                    window.resetCharacter(game)
                if window.launchGameBtn.click(mouse) and game.characterSelect and int(game.nbPlayers) > 0:
                    game.launchGame()
                    window.launchGame(game)




            #print(event)
        pygame.display.update()
        clock.tick(60)

