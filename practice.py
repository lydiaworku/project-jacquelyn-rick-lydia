import pygame

pygame.init()

green = (0, 200, 0)
blue = (0, 0, 200)
red = (200, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
light_gray = (200, 200, 200)
yellow = (255, 235, 0)
dark_gray = (135, 135, 135)


screen_width = 500
screen_height = 500


box_width = screen_width / 10
box_height = screen_height / 10


screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(white)


pygame.display.set_caption('Wordle Game')

font = pygame.font.SysFont('timesnewroman', 56)
text = font.render('Wordle', True, black, None)

text_rect = text.get_rect(center = (screen_width / 2, screen_height / 10))
screen.blit(text, text_rect)

# Centers the text and puts it onto the screen



from english_words import english_words_lower_alpha_set

five_list = []

for item in english_words_lower_alpha_set:
    if len(item) == 5:
        word = item
        five_list.append(item)

# Picks a word from the random list of english words 

r1b3 = pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2), box_width, box_height)
r1b2 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2), box_width, box_height)
r1b1 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2), box_width, box_height)
r1b4 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2), box_width, box_height)
r1b5 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2), box_width, box_height)

r2b3 = pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 75, box_width, box_height)
r2b2 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 75, box_width, box_height)
r2b1 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 75, box_width, box_height)
r2b4 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 75, box_width, box_height)
r2b5 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 75, box_width, box_height)

r3b3 = pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 150, box_width, box_height)
r3b2 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 150, box_width, box_height)
r3b1 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 150, box_width, box_height)
r3b4 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 150, box_width, box_height)
r3b5 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 150, box_width, box_height)

r4b3 = pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 225, box_width, box_height)
r4b2 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 225, box_width, box_height)
r4b1 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 225, box_width, box_height)
r4b4 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 225, box_width, box_height)
r4b5 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 225, box_width, box_height)

r5b3 = pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 300, box_width, box_height)
r5b2 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 300, box_width, box_height)
r5b1 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 300, box_width, box_height)
r5b4 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 300, box_width, box_height)
r5b5 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 300, box_width, box_height)


# displays rows of boxes to the screen:


class BoxRow():

    def __init__(self):
        self.firstrow()
        self.secondrow()
        self.thirdrow()
        self.fourthrow()
        self.fifthrow()

    def firstrow(self):
        pygame.draw.rect(screen, light_gray, r1b3, 3)
        pygame.draw.rect(screen, light_gray, r1b2, 3)
        pygame.draw.rect(screen, light_gray, r1b1, 3)
        pygame.draw.rect(screen, light_gray, r1b4, 3)
        pygame.draw.rect(screen, light_gray, r1b5, 3)
        pygame.display.update()

    def secondrow(self):
        pygame.draw.rect(screen, light_gray, r2b3, 3)
        pygame.draw.rect(screen, light_gray, r2b2, 3)
        pygame.draw.rect(screen, light_gray, r2b1, 3)
        pygame.draw.rect(screen, light_gray, r2b4, 3)
        pygame.draw.rect(screen, light_gray, r2b5, 3)
        pygame.display.update()

    def thirdrow(slef):
        pygame.draw.rect(screen, light_gray, r3b3, 3)
        pygame.draw.rect(screen, light_gray, r3b2, 3)
        pygame.draw.rect(screen, light_gray, r3b1, 3)
        pygame.draw.rect(screen, light_gray, r3b4, 3)
        pygame.draw.rect(screen, light_gray, r3b5, 3)
        pygame.display.update()

    def fourthrow(self):
        pygame.draw.rect(screen, light_gray, r4b3, 3)
        pygame.draw.rect(screen, light_gray, r4b2, 3)
        pygame.draw.rect(screen, light_gray, r4b1, 3)
        pygame.draw.rect(screen, light_gray, r4b4, 3)
        pygame.draw.rect(screen, light_gray, r4b5, 3)
        pygame.display.update()

    def fifthrow(self):
        pygame.draw.rect(screen, light_gray, r5b3, 3)
        pygame.draw.rect(screen, light_gray, r5b2, 3)
        pygame.draw.rect(screen, light_gray, r5b1, 3)
        pygame.draw.rect(screen, light_gray, r5b4, 3)
        pygame.draw.rect(screen, light_gray, r5b5, 3)
        pygame.display.update()

    def turn_green(self, box):
        pygame.draw.rect(screen, green, box, 0)
        print('turn green function is running')
        pygame.display.update()

    def turn_yellow(self, box):
        pygame.draw.rect(screen, yellow, box, 0)
        print('turn yellow function is running')
        pygame.display.update()

    def turn_dark_gray(self, box):
        pygame.draw.rect(screen, dark_gray, box, 0)
        print('turn dark gray function is running')
        pygame.display.update()

# BoxRow.firstrow()
# BoxRow.secondrow()
# BoxRow.thirdrow()
# BoxRow.fourthrow()
# BoxRow.fifthrow()


print(word)

# Loop that keeps the game open until the user quits

user_word = ''

def play_game(game, counter):
    user_word = input('what is your guess? ')
    if user_word == 'q':
        return False
    elif len(user_word) != 5 or type(user_word) != str:
        print('guess must be a five letter word')
    elif user_word not in five_list:
        print('invalid word')
    else:

# incorrect letter

        if user_word[0] not in word:
            game.turn_dark_gray(pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
        if user_word[1] not in word:
            game.turn_dark_gray(pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
        if user_word[2] not in word:
            game.turn_dark_gray(pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
        if user_word[3] not in word:
            game.turn_dark_gray(pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
        if user_word[4] not in word:
            game.turn_dark_gray(pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))

# correct letter incorrect placement

        if user_word[0] != word[0] and user_word[0] in word:
           game.turn_yellow(pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
        if user_word[1] != word[1] and user_word[1] in word:
            game.turn_yellow(pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
        if user_word[2] != word[2] and user_word[2] in word:
            game.turn_yellow(pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
        if user_word[3] != word[3] and user_word[3] in word:
            game.turn_yellow(pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
        if user_word[4] != word[4] and user_word[4] in word:
            game.turn_yellow(pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))

# correct letter and placement

        if user_word[0] == word[0]:
           game.turn_green(pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
        if user_word[1] == word[1]:
            game.turn_green(pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
        if user_word[2] == word[2]:
            game.turn_green(pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
        if user_word[3] == word[3]:
            game.turn_green(pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))
        if user_word[4] == word[4]:
            game.turn_green(pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + ((counter - 1) * 75), box_width, box_height))

    return True


        
playing = True
game = BoxRow()
counter = 0
while playing:
    counter += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()

    print(counter)
    result = play_game(game, counter)

    if not result or counter == 5:
        print('game over')
        playing = False
        pygame.quit()

    if user_word == word:
        counter = 5

pygame.quit()
