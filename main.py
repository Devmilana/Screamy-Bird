import pygame
import sounddevice as sd
import numpy as np
import random
import time
import os

# Initialise pygame
pygame.init()


# Initialise pygame clock
clock = pygame.time.Clock()


# Always fullscreen game window
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# pygame.display.set_caption('SCREAMY BIRD')
# screen_width = pygame.display.Info().current_w
# screen_height = pygame.display.Info().current_h

# Manually set game window size
screen_width = 900
screen_height = 1060
screen = pygame.display.set_mode((screen_width, screen_height)) 
pygame.display.set_caption('SCREAMY BIRD')

# Colors
white = (255, 255, 255)
green = (34, 139, 34)
orange = (255, 165, 0)
red = (255, 0, 0)


# Background image
background_img = pygame.image.load(os.path.join('img', 'bglong.png'))
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))


# ------- BIRD CLASS ------- #
class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = pygame.image.load(os.path.join('img', 'bird.png')) # bird image path
        self.img_width = self.img.get_size()[0]
        self.img_height = self.img.get_size()[1]
        self.jump = 6 # jump height
        self.gravity = 8 # gravity fall height

    # Bird jump movement
    def fly(self):
        self.y -= self.jump

    # Bird fall movement
    def fall(self):
        self.y += self.gravity

    # Bird out of bounds check
    def out_of_bounds(self):
        return (self.y > screen_height - self.img_height or self.y < 0)
    
    # Draw bird to screen
    def draw(self):
        screen.blit(self.img, (self.x, self.y))


# ------- SCORE DISPLAY CLASS ------- #
class ScoreDisplay:
    def __init__(self):
        self.position = [3, 3] # position of score display
        self.score = 0 # initial score set to zero
        self.font = pygame.font.Font('PressStart2P.ttf', 30) # font style and size

    # Add score to current score
    def add_score(self, value):
        self.score += 5

    # Reset score to zero
    def reset(self):
        self.score = 0

    # Draw current score to screen
    def draw(self):
        text = self.font.render(f'CURRENT SCORE: {self.score}', True, white)
        screen.blit(text, self.position)


# ------- PIPE CLASS ------- #
class Pipe:
    def __init__(self, Pipe_width, Pipe_height, gap):
        self.x_Pipe = screen_width # initial x position of pipe
        self.y_Pipe = 0 # initial y position of pipe
        self.Pipe_width = Pipe_width # width of pipe
        self.Pipe_height = Pipe_height * screen_height // 720 # height of pipe
        self.gap = gap # gap between pipes
        self.passed = False # check if pipe has been passed over

    # Draw pipe to screen
    def draw(self):
        pygame.draw.rect(screen, green, [self.x_Pipe, self.y_Pipe, self.Pipe_width, self.Pipe_height]) # Draw top pipe
        bottom_pipe_height = screen_height - self.Pipe_height - self.gap
        pygame.draw.rect(screen, green, [self.x_Pipe, self.y_Pipe + self.Pipe_height + self.gap, self.Pipe_width, bottom_pipe_height]) # Draw bottom pipe with gap

    # Move pipe to new position
    def move(self, x, y):
        self.passed = False
        self.x_Pipe = x
        self.y_Pipe = y

    # Update pipe gap
    def update(self, gap):
        self.gap = gap

    # Check if bird has passed over pipe    
    def pipe_pass_check(self, bird: Bird):
        self.passed = (bird.x > self.x_Pipe + self.Pipe_width and bird.x < self.x_Pipe + self.Pipe_width + bird.img_width / 5)
        return self.passed

    # Check if bird has collided with pipe
    def collision_check(self, bird: Bird):
        return ((bird.y < self.Pipe_height or bird.y + bird.img_height > self.Pipe_height + self.gap) 
                and bird.x + bird.img_width > self.x_Pipe and bird.x < self.x_Pipe + self.Pipe_width)


# ------- (SCREAMY BIRD) MAIN GAME LOOP CLASS ------- #
class ScreamyBird:

    bird = Bird(150, 200) # initial bird position
    score_display = ScoreDisplay() # score display
    Pipe = Pipe(85, random.randint(0, int(screen_height / 2)), bird.img_height * 5) # initial pipe position with gap size

    def __init__(self):
        self.game_over = False

    # Check scream threshold for jump
    def scream_check(indata, outdata, frames, time, status):
        scream_volume = np.linalg.norm(indata) # Normalize scream volume
        # Check scream volume threshold
        if scream_volume > 2.5: 
            ScreamyBird.bird.fly() # bird jump if threshold passed
        else:
            ScreamyBird.bird.fall() # bird falls if threshold not reached

    # Reset game
    def reset_game():
        ScreamyBird.bird = Bird(150, 200)
        ScreamyBird.score_display.reset()
        ScreamyBird.Pipe = Pipe(85, random.randint(0, int(screen_height / 2)), ScreamyBird.bird.img_height * 5)

    # Restart or exit game  
    def restart_exit(self):
        for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]): # check for key press or exit
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.KEYDOWN:
                continue

            return event.key
        return None

    # Display game over screen
    def end_screen(self):
        # Render game over text in orange
        game_over_text = self.score_display.font.render('G A M E   O V E R', True, (255, 165, 0))  # Orange color
        game_over_rect = game_over_text.get_rect(center=(screen_width / 2, screen_height / 2 - 50))

        # Render game over text in white for outline
        game_over_text_outline = self.score_display.font.render('G A M E   O V E R', True, white)
        game_over_rect_outline = game_over_text_outline.get_rect(center=(screen_width / 2, screen_height / 2 - 50))

        # Offset the outline text by a small amount
        game_over_rect_outline.x -= 2
        game_over_rect_outline.y -= 2

        # Blit the outline text first for outline glitch effect
        screen.blit(game_over_text_outline, game_over_rect_outline)
        screen.blit(game_over_text_outline, (game_over_rect_outline.x + 4, game_over_rect_outline.y))
        screen.blit(game_over_text_outline, (game_over_rect_outline.x - 2, game_over_rect_outline.y))
        screen.blit(game_over_text_outline, (game_over_rect_outline.x, game_over_rect_outline.y + 4))
        screen.blit(game_over_text_outline, (game_over_rect_outline.x, game_over_rect_outline.y - 4))
        screen.blit(game_over_text, game_over_rect)

        # Render continue text in red
        continue_text = self.score_display.font.render('Press any key to restart', True, red) # continue text
        continue_rect = continue_text.get_rect(center=(screen_width / 2, screen_height / 2 + 65))
        screen.blit(continue_text, continue_rect)

        pygame.display.update()
        
        time.sleep(1)

        while self.restart_exit() is None:
            clock.tick()
        self.game_over = False

        self.play() # restart game


    # Call game over screen
    def gameOver(self):
        self.end_screen()

    # Main game loop   
    def play(self):
        
        # Inital pipe position
        x_Pipe = screen_width
        y_Pipe = 0
        Pipe_width = 85 # width of Pipes
        Pipe_move = 4  # speed of incoming pipes
        
        # Call reset game 
        ScreamyBird.reset_game()

        # While game is not over
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True # exit game if quit
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    ScreamyBird.bird.fly() # bird jump if mouse clicked

            # Draw background
            screen.blit(background_img, (0, 0))

            # Draw score
            ScreamyBird.score_display.draw()

            # Draw bird
            ScreamyBird.bird.draw()

            # Draw and move pipes
            ScreamyBird.Pipe.move(x_Pipe, y_Pipe)
            ScreamyBird.Pipe.draw()
            x_Pipe -= Pipe_move

            # If bird passes over pipe, add score
            if ScreamyBird.Pipe.pipe_pass_check(ScreamyBird.bird):
                ScreamyBird.score_display.add_score(1)

            # If bird collides with pipe, call game over
            if ScreamyBird.Pipe.collision_check(ScreamyBird.bird):
                self.gameOver()

            # If bird out of bounds, call game over
            if ScreamyBird.bird.out_of_bounds():
                self.gameOver()

            # If pipe out of bounds, reset pipe position
            if x_Pipe < (-1 * Pipe_width):
                x_Pipe = screen_width
                ScreamyBird.Pipe.Pipe_height = random.randint(0, int(screen_height / 2))

            # Update screen
            pygame.display.update()
            
            # Set game speed
            clock.tick(90)


# Main function
def main():
    sd.Stream(callback=ScreamyBird.scream_check).start()
    game = ScreamyBird()
    game.play()


#--- RUN MAIN FUNCTION ---#
if __name__ == '__main__':
    main()