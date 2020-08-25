import pygame
import math
import random

# Setting display
pygame.init()
WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game by Franck!")

# Setting buttons
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (GAP + RADIUS * 2) * 13)/2) # It's the distance from the edge to the first Letter
starty = 400
A = 65

for i in range(26):
    x = startx + GAP * 2 + ((GAP + RADIUS * 2) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# setting fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40, bold=1)
WORD_FONT = pygame.font.SysFont("comicsans", 60)
TITLE_FONT = pygame.font.SysFont("comicsans", 70, italic=1)

# Load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# Game variable
hangman_status = 0
words = ["PYTHON", "AI", "DEVELOPPER", "HANGMAN","GAME"]
word = random.choice(words)
guessed = []

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (169,169,169)

# defining the draw function
def draw():
    window.fill(WHITE)

    # Draw title
    text = TITLE_FONT.render("HANGMAN GAME!", 1, BLACK)
    window.blit(text, (WIDTH / 2 - text.get_width()/2, 20))

    # Draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    window.blit(text, (400, 200))

    # Draw buttons
    for letter in letters:
        x, y, ltr, visible = letter

        if visible:
            pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            window.blit(text, (x - text.get_width() /
                               2, y - text.get_height()/2))

    window.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    window.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    window.blit(text, (WIDTH/2 - text.get_width() /
                       2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def initGame():
	letters.clear()
	guessed.clear()
	global hangman_status
	hangman_status = 0
	for i in range(26):
		x = startx + GAP * 2 + ((GAP + RADIUS * 2) * (i % 13))
		y = starty + ((i // 13) * (GAP + RADIUS * 2))
		letters.append([x, y, chr(A + i), True])


def main():

    global hangman_status
    # Setting loop
    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # getting the mouse position
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - mouse_x)**2 + (y - mouse_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            display_message("You Won!")
            break

        if hangman_status == 6:
            display_message("You Lost!")
            break


start_game = True
while start_game:
    display_message("Would like to play the Hangman Game ?")
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            initGame()
            words = ["PYTHON", "AI", "DEVELOPPER", "HANGMAN","GAME"]
            word = random.choice(words)
            main()
        elif event.type == pygame.QUIT:
            start_game = False

            break
pygame.quit()