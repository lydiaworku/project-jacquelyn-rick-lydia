import pygame
import english_words
import time

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

pygame.display.update()


from english_words import english_words_lower_alpha_set

five_list = []

for item in english_words_lower_alpha_set:
    if len(item) == 5:
        word = item
        five_list.append(item)

# Picks a word from the random list of english words 

r1b3 = pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2), box_width, box_height)
r1b2 = pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2), box_width, box_height), 3)
r1b1 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2), box_width, box_height)
r1b4 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2), box_width, box_height)
r1b5 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2), box_width, box_height)

r2b3 = pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 75, box_width, box_height)
r2b2 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 75, box_width, box_height)
r2b1 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 75, box_width, box_height)
r2b4 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 75, box_width, box_height)
r2b5 = pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 75, box_width, box_height)



# displays rows of boxes to the screen:


class BoxRow():

    def __init__(self):
        pass

    def firstrow():
        pygame.draw.rect(screen, light_gray, r1b3, 3)
        pygame.draw.rect(screen, light_gray, r1b2, 3)
        pygame.draw.rect(screen, light_gray, r1b1, 3)
        pygame.draw.rect(screen, light_gray, r1b4, 3)
        pygame.draw.rect(screen, light_gray, r1b5, 3)
        pygame.display.update()

    def secondrow():
        pygame.draw.rect(screen, light_gray, r2b3, 3)
        pygame.draw.rect(screen, light_gray, r2b2, 3)
        pygame.draw.rect(screen, light_gray, r2b1, 3)
        pygame.draw.rect(screen, light_gray, r2b4, 3)
        pygame.draw.rect(screen, light_gray, r2b5, 3)
        pygame.display.update()

    def thirdrow():
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 150, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 150, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 150, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 150, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 150, box_width, box_height), 3)
        pygame.display.update()

    def fourthrow():
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 225, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 225, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 225, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 225, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 225, box_width, box_height), 3)
        pygame.display.update()

    def fifthrow():
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)), (screen_height * 0.2) + 300, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 1.5, (screen_height * 0.2) + 300, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) - box_width * 3, (screen_height * 0.2) + 300, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 1.5, (screen_height * 0.2) + 300, box_width, box_height), 3)
        pygame.draw.rect(screen, light_gray, pygame.Rect((screen_width * 0.5 - (box_width / 2)) + box_width * 3, (screen_height * 0.2) + 300, box_width, box_height), 3)
        pygame.display.update()

    def turn_green(box):
        pygame.draw.rect(screen, green, box, 0)

    def turn_yellow(box):
        pygame.draw.rect(screen, yellow, box, 0)

    def turn_dark_gray(box):
        pygame.draw.rect(screen, dark_gray, box, 0)

BoxRow.firstrow()
BoxRow.secondrow()
BoxRow.thirdrow()
BoxRow.fourthrow()
BoxRow.fifthrow()
pygame.display.update()



winner = ''
counter = 0

print(word)


playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

# Loop that keeps the game open until the user quits





def play_game():
    user_word = input('what is your guess? ')
    if user_word == word:
        global winner
        winner = 'You won! '
        print(winner)
    elif len(user_word) != 5 or type(user_word) != str:
        print('guess must be a five letter word')
    elif user_word not in five_list:
        print('invalid word')
    else:

        if counter == 1:

# correct letter and placement

            if user_word[0] == word[0]:
                BoxRow.turn_green(r1b1)
                pygame.display.update()
            if user_word[1] == word[1]:
                BoxRow.turn_green(r1b2)
                pygame.display.update()
            if user_word[2] == word[2]:
                BoxRow.turn_green(r1b3)
                pygame.display.update()
            if user_word[3] == word[3]:
                BoxRow.turn_green(r1b4)
                pygame.display.update()
            if user_word[4] == word[4]:
                BoxRow.turn_green(r1b5)
                pygame.display.update()

# correct letter but wrong place

            if user_word[0] != word[0] and (user_word[0] == word[1] or user_word[0] == word[2] or user_word[0] == word[3] or user_word[0] == word[4]):
                BoxRow.turn_yellow(r1b1)
                pygame.display.update()
            if user_word[1] != word[1] and (user_word[1] == word[0] or user_word[1] == word[2] or user_word[1] == word[3] or user_word[1] == word[4]):
                BoxRow.turn_yellow(r1b2)
                pygame.display.update()
            if user_word[2] != word[2] and (user_word[2] == word[0] or user_word[2] == word[1] or user_word[2] == word[3] or user_word[2] == word[4]):
                BoxRow.turn_yellow(r1b3)
                pygame.display.update()
            if user_word[3] != word[3] and (user_word[3] == word[0] or user_word[3] == word[1] or user_word[3] == word[2] or user_word[3] == word[4]):
                BoxRow.turn_yellow(r1b4)
                pygame.display.update()
            if user_word[4] != word[4] and (user_word[4] == word[0] or user_word[4] == word[1] or user_word[4] == word[2] or user_word[4] == word[3]):
                BoxRow.turn_yellow(r1b5)
                pygame.display.update()

# incorrect letter

            if user_word[0] not in word:
                BoxRow.turn_dark_gray(r1b1)
                pygame.display.update()
            if user_word[1] not in word:
                BoxRow.turn_dark_gray(r1b2)
                pygame.display.update()
            if user_word[2] not in word:
                BoxRow.turn_dark_gray(r1b3)
                pygame.display.update()
            if user_word[3] not in word:
                BoxRow.turn_dark_gray(r1b4)
                pygame.display.update()
            if user_word[4] not in word:
                BoxRow.turn_dark_gray(r1b5)
                pygame.display.update()

            pygame.display.update()
        
        elif counter == 2:

            # correct letter and placement

            if user_word[0] == word[0]:
                BoxRow.turn_green(r2b1)
                pygame.display.update()
            if user_word[1] == word[1]:
                BoxRow.turn_green(r2b2)
                pygame.display.update()
            if user_word[2] == word[2]:
                BoxRow.turn_green(r2b3)
                pygame.display.update()
            if user_word[3] == word[3]:
                BoxRow.turn_green(r2b4)
                pygame.display.update()
            if user_word[4] == word[4]:
                BoxRow.turn_green(r2b5)
                pygame.display.update()

# correct letter but wrong place

            if user_word[0] != word[0] and (user_word[0] == word[1] or user_word[0] == word[2] or user_word[0] == word[3] or user_word[0] == word[4]):
                BoxRow.turn_yellow(r2b1)
                pygame.display.update()
            if user_word[1] != word[1] and (user_word[1] == word[0] or user_word[1] == word[2] or user_word[1] == word[3] or user_word[1] == word[4]):
                BoxRow.turn_yellow(r2b2)
                pygame.display.update()
            if user_word[2] != word[2] and (user_word[2] == word[0] or user_word[2] == word[1] or user_word[2] == word[3] or user_word[2] == word[4]):
                BoxRow.turn_yellow(r2b3)
                pygame.display.update()
            if user_word[3] != word[3] and (user_word[3] == word[0] or user_word[3] == word[1] or user_word[3] == word[2] or user_word[3] == word[4]):
                BoxRow.turn_yellow(r2b4)
                pygame.display.update()
            if user_word[4] != word[4] and (user_word[4] == word[0] or user_word[4] == word[1] or user_word[4] == word[2] or user_word[4] == word[3]):
                BoxRow.turn_yellow(r2b5)
                pygame.display.update()

# incorrect letter

            if user_word[0] not in word:
                BoxRow.turn_dark_gray(r2b1)
                pygame.display.update()
            if user_word[1] not in word:
                BoxRow.turn_dark_gray(r2b2)
                pygame.display.update()
            if user_word[2] not in word:
                BoxRow.turn_dark_gray(r2b3)
                pygame.display.update()
            if user_word[3] not in word:
                BoxRow.turn_dark_gray(r2b4)
                pygame.display.update()
            if user_word[4] not in word:
                BoxRow.turn_dark_gray(r2b5)
                pygame.display.update()
    

while counter != 5:
    counter += 1
    print(counter)
    play_game()
    if winner == 'You won! ':
        counter = 5

pygame.display.update()

# quits the game if the user gets the word right and prints you won message