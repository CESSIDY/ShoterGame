import os
import pickle
import neat
import pygame
import sys
from Settings import win, clock
from bin.Worlds.Generator import GenerateWorlds
from bin.Players.Player import Player
from bin.Players.AIPlayer import AIPlayer
from multiprocessing import Process


class gameWindow(object):
    def __init__(self, AI=False):
        self.settings = {
            'ScreenWidth': 1100,
            'ScreenHeight': 700,
            'playZoneYCoordinates': 550,
            'bg': pygame.image.load('resources/images/bg.jpg').convert(),
            'font': pygame.font.SysFont("comicsans", 30, True),
            'bulletSound': pygame.mixer.Sound('resources/audio/bullet.wav'),
            'hitSound': pygame.mixer.Sound('resources/audio/hit.wav')
        }
        self.win = win
        self.AI = AI
        self.keys = tuple()
        self.events = tuple()
        if not self.AI:
            player = Player(self.win, self.settings)
            pygame.display.set_caption("When will it all end?")
            pygame.mixer.music.load('resources/audio/music.wav')
            pygame.mixer.music.play(-1)
            self.clock = pygame.time.Clock()
            self.worlds_generator = GenerateWorlds(self.settings, self.win, player)
        else:
            self.AI_keys = list()
        self.pause = False

    def setLikePlayer(self):
        player = Player(self.win, self.settings)
        pygame.display.set_caption("When will it all end?")
        pygame.mixer.music.load('resources/audio/music.wav')
        pygame.mixer.music.play(-1)
        self.clock = pygame.time.Clock()
        self.worlds_generator = GenerateWorlds(self.settings, self.win, player)

    def AIStart(self, genomes=None, config=None):
        nets = []
        worlds = []
        ge = []
        for genome_id, genome in genomes:
            genome.fitness = 0  # start with fitness level of 0
            net = neat.nn.FeedForwardNetwork.create(genome, config)
            nets.append(net)
            worlds.append(GenerateWorlds(self.settings, self.win, AIPlayer(self.win, self.settings)))
            ge.append(genome)

        for key, world in enumerate(worlds):
            temp_score = 0
            temp_health = 4
            world.activeWorld.generate()
            while True:
                self.events = pygame.event.get()
                self.keys = pygame.key.get_pressed()
                if not self.isWindowClose():
                    pygame.quit()
                    sys.exit()
                self.gamePause()
                if not self.pause:
                    val_array = world.getWorldInfo()
                    self.AI_keys = nets[key].activate((val_array))
                    world.action(self.AI_keys, self.events)
                    jumpedCount = world.player.isJumpedSomething(world.enemys_generator.enemys)
                    if jumpedCount:
                        ge[key].fitness += jumpedCount * 0.09
                    # give player a fitness of 0.5 for each enemy that he kill
                    if world.player.score > temp_score:
                        ge[key].fitness += 0.7
                    elif world.player.score < temp_score:
                        ge[key].fitness -= 0.5
                        ge[key].fitness -= 0.5
                    temp_score = world.player.score
                    if world.player.health <= 0:
                        ge[key].fitness -= 1.0
                        print(f"ALIVE: {len(worlds)} | SCORE: {world.player.score} | FITNESS: {ge[key].fitness}")
                        nets.pop(key)
                        ge.pop(key)
                        worlds.pop(key)
                        break
                    else:
                        ge[key].fitness += 0.001

                    if world.player.score >= 50:
                        with open('winner.pkl', 'wb') as output:
                            pickle.dump(nets[key], output, 1)
                            break
                else:
                    self.pauseMenu()

    def start(self):
        run = True
        while run:
            clock.tick(30)
            self.events = pygame.event.get()
            self.keys = pygame.key.get_pressed()
            run = self.isWindowClose()
            self.gamePause()
            if not self.pause:
                self.worlds_generator.action(self.keys, self.events)
            else:
                self.pauseMenu()

        pygame.quit()
        sys.exit()

    def gamePause(self):
        for event in self.events:
            if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if self.keys[pygame.K_ESCAPE] and not self.pause:
                    self.pause = True
                elif self.keys[pygame.K_ESCAPE] and self.pause:
                    self.pause = False

    def pauseMenu(self):
        text = self.settings['font'].render("PAUSE", 1, (0, 0, 0))  # Arguments are: text, anti-aliasing, color
        self.win.blit(text, (self.settings['ScreenWidth'] // 2, self.settings['ScreenHeight'] // 2))
        pygame.display.update()

    def isWindowClose(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                return False
        return True


game_window = gameWindow(AI=True)


def run_AI(config_file):
    """
    runs the NEAT algorithm to train a neural network to play flappy bird.
    :param config_file: location of config file
    :return: None
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    # p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    # winner = p.run(gameWindow(AI=True).AIStart, 500)
    winner = p.run(game_window.AIStart, 500)

    # show final stats
    print('\nBest genome:\n{!s}'.format(winner))


def start_menu():
    def is_AI_Button():
        return (game_window.settings['ScreenWidth'] // 2 - 150) <= mouse[0] <= (game_window.settings[
                                                                                    'ScreenWidth'] // 2 - 10) and (
                       game_window.settings['ScreenHeight'] // 2 - 20) <= mouse[1] <= (game_window.settings[
                                                                                           'ScreenHeight'] / 2 + 20)

    def draw_AI_Button(color):
        pygame.draw.rect(game_window.win, color,
                         [game_window.settings['ScreenWidth'] // 2 - 150,
                          game_window.settings['ScreenHeight'] // 2 - 20, 140,
                          55])
        ai_text = game_window.settings['font'].render("AI", 1, (0, 0, 0))
        game_window.win.blit(ai_text, (
            game_window.settings['ScreenWidth'] // 2 - ((150 // 2) + 15),
            game_window.settings['ScreenHeight'] // 2 - 8))

    def is_Player_Button():
        return (game_window.settings['ScreenWidth'] // 2 + 10) <= mouse[0] <= (game_window.settings[
                                                                                   'ScreenWidth'] // 2 + 150) and (
                       game_window.settings['ScreenHeight'] // 2 - 20) <= mouse[1] <= (game_window.settings[
                                                                                           'ScreenHeight'] / 2 + 20)

    def draw_Player_Button(color):
        pygame.draw.rect(game_window.win, color,
                         [game_window.settings['ScreenWidth'] // 2 + 10,
                          game_window.settings['ScreenHeight'] // 2 - 20, 140,
                          55])
        player_text = game_window.settings['font'].render("Player", 1, (0, 0, 0))
        game_window.win.blit(player_text, (
            game_window.settings['ScreenWidth'] // 2 + ((150 // 2) - 30),
            game_window.settings['ScreenHeight'] // 2 - 8))

    run = True
    AI = False
    while run:
        mouse = pygame.mouse.get_pos()
        # light shade of the button
        color_light = (170, 170, 170)
        # dark shade of the button
        color_dark = (100, 100, 100)

        if is_AI_Button():
            draw_AI_Button(color_light)
        else:
            draw_AI_Button(color_dark)

        if is_Player_Button():
            draw_Player_Button(color_light)
        else:
            draw_Player_Button(color_dark)

        pygame.display.update()

        # checks if a mouse is clicked
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # if the mouse is clicked on the button the game is terminated
                if is_Player_Button():
                    AI = False
                    run = False
                    break
                elif is_AI_Button():
                    AI = True
                    run = False
                    break

    if AI:
        local_dir = os.path.dirname(__file__)
        config_path = os.path.join(local_dir, 'config-feedforward.txt')
        run_AI(config_path)
    else:
        game_window.setLikePlayer()
        game_window.start()


if __name__ == '__main__':
    # game_window = gameWindow()
    # game_window.start()
    start_menu()
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    # local_dir = os.path.dirname(__file__)
    # config_path = os.path.join(local_dir, 'config-feedforward.txt')
    # run(config_path)
