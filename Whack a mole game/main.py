import pygame
import random
from pygame import *


class GameManager:
    def __init__(self):
        # Define constants
        self.SCREEN_WIDTH = 900
        self.SCREEN_HEIGHT = 506
        self.FPS = 60
        self.MOLE_WIDTH = 90
        self.MOLE_HEIGHT = 81
        self.FONT_SIZE = 31
        self.FONT_TOP_MARGIN = 380
        self.LEVEL_SCORE_GAP = 4
        self.LEFT_MOUSE_BUTTON = 1
        self.GAME_TITLE = "Whack A Zombie"
        self.PLAY = False
        # Initialize player's score, number of missed hits and level
        self.score = 0
        self.misses = 0
        #self.level = 1
        # Initialize screen
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption(self.GAME_TITLE)
        self.background = pygame.image.load("./Whack a mole game/images/back.png")
        # Font object for displaying text
        self.font_obj = pygame.font.Font('./Whack a mole game/fonts/GROBOLD.ttf', self.FONT_SIZE)
        # Initialize the mole's sprite sheet
        # 6 different states
        
        self.mole = []
        
        appear = pygame.image.load("./Whack a mole game/images/zom_appear/appear_1.png")
        self.mole.append(appear)
        appear = pygame.image.load("./Whack a mole game/images/zom_appear/appear_2.png")
        self.mole.append(appear)
        appear = pygame.image.load("./Whack a mole game/images/zom_appear/appear_3.png")
        self.mole.append(appear)
        appear = pygame.image.load("./Whack a mole game/images/zom_appear/appear_4.png")
        self.mole.append(appear)
        appear = pygame.image.load("./Whack a mole game/images/zom_appear/appear_5.png")
        self.mole.append(appear)
        appear = pygame.image.load("./Whack a mole game/images/zom_appear/appear_6.png")
        self.mole.append(appear)
        appear = pygame.image.load("./Whack a mole game/images/zom_die/die_4.png")
        self.mole.append(appear)
        appear = pygame.image.load("./Whack a mole game/images/zom_die/die_5.png")
        self.mole.append(appear)
        appear = pygame.image.load("./Whack a mole game/images/zom_die/die_6.png")
        self.mole.append(appear)
        appear = pygame.image.load("./Whack a mole game/images/zom_die/die_7.png")
        self.mole.append(appear)
        appear = pygame.image.load("./Whack a mole game/images/zom_die/die_8.png")
        self.mole.append(appear)
        # Positions of the holes in background
        self.hole_positions = []
        self.hole_positions.append((190, 5))
        self.hole_positions.append((360,5))
        self.hole_positions.append((530,5))
        self.hole_positions.append((575,125))
        self.hole_positions.append((405,125))
        self.hole_positions.append((235,120))
        self.hole_positions.append((530,245))
        self.hole_positions.append((360,245))
        self.hole_positions.append((190,235))
        # Init debugger
        #self.debugger = Debugger("debug")
        # Sound effects
        self.soundEffect = SoundEffect()

    # Calculate the player level according to his current score & the LEVEL_SCORE_GAP constant
    '''
    def get_player_level(self):
        newLevel = 1 + int(self.score / self.LEVEL_SCORE_GAP)
        if newLevel != self.level:
            # if player get a new level play this sound
            self.soundEffect.playLevelUp()
        return 1 + int(self.score / self.LEVEL_SCORE_GAP)
    '''
    # Get the new duration between the time the mole pop up and down the holes
    # It's in inverse ratio to the player's current level
    '''
    def get_interval_by_level(self, initial_interval):
        new_interval = initial_interval - self.level * 0.15
        if new_interval > 0:
            return new_interval
        else:
            return 0.05
    '''
    # Check whether the mouse click hit the mole or not
    def is_mole_hit(self, mouse_position, current_hole_position):
        mouse_x = mouse_position[0]
        mouse_y = mouse_position[1]
        current_hole_x = current_hole_position[0]
        current_hole_y = current_hole_position[1]
        if (mouse_x > current_hole_x) and (mouse_x < current_hole_x + self.MOLE_WIDTH) and (mouse_y > current_hole_y) and (mouse_y < current_hole_y + self.MOLE_HEIGHT):
            return True
        else:
            return False

    # Update the game states, re-calculate the player's score, misses, level
    def update(self):
        # Update the player's score
        current_score_string = "SCORE: " + str(self.score)
        score_text = self.font_obj.render(current_score_string, True, (255, 255, 255))
        score_text_pos = score_text.get_rect()
        score_text_pos.centerx = 230
        score_text_pos.centery = self.FONT_TOP_MARGIN
        self.screen.blit(score_text, score_text_pos)
        # Update the player's misses
        current_misses_string = "MISSES: " + str(self.misses)
        misses_text = self.font_obj.render(current_misses_string, True, (255, 255, 255))
        misses_text_pos = misses_text.get_rect()
        misses_text_pos.centerx = self.SCREEN_WIDTH / 5 * 3.1
        misses_text_pos.centery = self.FONT_TOP_MARGIN
        self.screen.blit(misses_text, misses_text_pos)

    # Start the game's main loop
    # Contains some logic for handling animations, mole hit events, etc..
    def prepare(self):
        loop = True

        how_to_play = "CLICK MOUSE TO PLAY"
        how_to_play_text = self.font_obj.render(how_to_play, True, (255, 255, 255))
        how_to_play_text_pos = how_to_play_text.get_rect()
        how_to_play_text_pos.centerx = 400
        how_to_play_text_pos.centery = self.FONT_TOP_MARGIN
        self.screen.blit(how_to_play_text, how_to_play_text_pos)

        while loop:
            for event in pygame.event.get():
                if event.type == QUIT:
                    loop = False
                    self.PLAY = False
                elif event.type == MOUSEBUTTONDOWN:
                    self.PLAY = True
                    return
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(how_to_play_text, how_to_play_text_pos)
            pygame.display.flip()

    def start(self):
        cycle_time = 0
        num = -1
        loop = True
        is_down = False
        interval = 0.1
        initial_interval = 1
        frame_num = 0
        left = 0
        # Time control variables
        clock = pygame.time.Clock()

        for i in range(len(self.mole)):
            self.mole[i].set_colorkey((0, 0, 0))
            self.mole[i] = self.mole[i].convert_alpha()

        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                if event.type == MOUSEBUTTONDOWN and event.button == self.LEFT_MOUSE_BUTTON:
                    self.soundEffect.playFire()
                    if self.is_mole_hit(mouse.get_pos(), self.hole_positions[frame_num]) and num > 0 and left == 0:
                        num = 6
                        left = 14
                        is_down = False
                        interval = 0
                        self.score += 1  # Increase player's score
                        # Play hurt sound
                        self.soundEffect.playHurt()
                        self.update()
                    else:
                        self.misses += 1
                        self.update()

            if num > 10:
                self.screen.blit(self.background, (0, 0))
                self.update()
                num = -1
                left = 0

            if num == -1:
                self.screen.blit(self.background, (0, 0))
                self.update()
                num = 0
                is_down = False
                interval = 0.5
                frame_num = random.randint(0, 8)

            mil = clock.tick(self.FPS)
            sec = mil / 1000.0
            cycle_time += sec
            if cycle_time > interval:
                pic = self.mole[num]
                self.screen.blit(self.background, (0, 0))
                self.screen.blit(pic, (self.hole_positions[frame_num][0] - left, self.hole_positions[frame_num][1]))
                self.update()
                if is_down is False:
                    num += 1
                else:
                    num -= 1
                if num == 7:
                    interval = 0.3
                elif num == 6:
                    num -= 1
                    is_down = True
                    interval = 0.85  # get the newly decreased interval value
                else:
                    interval = 0.1
                cycle_time = 0
            # Update the display
            pygame.display.flip()


# The Debugger class - use this class for printing out debugging information
class Debugger:
    def __init__(self, mode):
        self.mode = mode

    def log(self, message):
        if self.mode is "debug":
            print("> DEBUG: " + str(message))


class SoundEffect:
    def __init__(self):
        self.mainTrack = pygame.mixer.music.load("./Whack a mole game/sounds/Zombie Garden.mp3")
        self.fireSound = pygame.mixer.Sound("./Whack a mole game/sounds/fire.wav")
        self.fireSound.set_volume(1.0)
        self.hurtSound = pygame.mixer.Sound("./Whack a mole game/sounds/hurt.wav")
        self.levelSound = pygame.mixer.Sound("./Whack a mole game/sounds/point.wav")
        pygame.mixer.music.play(-1)

    def playFire(self):
        self.fireSound.play()

    def stopFire(self):
        self.fireSound.sop()

    def playPop(self):
        self.popSound.play()

    def stopPop(self):
        self.popSound.stop()

    def playHurt(self):
        self.hurtSound.play()

    def stopHurt(self):
        self.hurtSound.stop()

    def playLevelUp(self):
        self.levelSound.play()

    def stopLevelUp(self):
        self.levelSound.stop()

###############################################################
# Initialize the game
ICON = pygame.image.load("./Whack a mole game/images/zom_icon.png")
pygame.display.set_icon(ICON)
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()

# Run the main loop
my_game = GameManager()
my_game.prepare()
if my_game.PLAY == True:
    my_game.start()
# Exit the game if the main loop ends
pygame.quit()
