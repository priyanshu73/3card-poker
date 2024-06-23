import pygame
import sys
import os
from card import Card
from hand import Hand
from deck import Deck
from player import Player
from button import Button

# Initialize Pygame
pygame.init()
os.system('cls')
# Set up the screen
screen_width = 800
screen_height = 600
card_size = screen_width / 5.5
dp_size = screen_width / 9
win_index = -1
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame")

# Define the resources directory
res_dir = "res"

# Text
text = "Hello, Pygame!"
text_color = (255, 255, 255)  # White color

def display_text(text, x, y, size, font_name):
    font_path = os.path.join(res_dir, font_name) if font_name else None
    font = pygame.font.Font(font_path, size)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)  # Example background color

# Load background image
background = pygame.image.load(os.path.join(res_dir, "bg.jpg"))
background = pygame.transform.scale(background, (screen_width, screen_height))
back_card = pygame.image.load(os.path.join(res_dir, "back.png"))
back_card = pygame.transform.scale(back_card, (.5 * card_size, .76 * card_size))
# Scale the image to your needed size

# Game variables
player_dps = []
hand_imgs = []

# Load handImg
def loadHandImg():
    for i in range(4):
        handimg = []
        hand_imgs.append(handimg)

loadHandImg()
players = []
deck = Deck()
card_imgs = []

deck.generate()
deck.shuffle()

def LoadCard(card):
    cardImg = pygame.image.load(os.path.join(res_dir, f"{card.getValue()}.png"))
    cardImg = pygame.transform.scale(cardImg, (.5 * card_size, .76 * card_size))
    card_imgs.append(cardImg)

for i in range(4):
    name = "player" + str(i + 1)
    player = Player(name)
    players.append(player)
    player_dp = pygame.image.load(os.path.join(res_dir, f"player{i + 1}.png"))
    player_dp = pygame.transform.scale(player_dp, (dp_size, dp_size))
    player_dp.set_alpha(128)  # Set transparency level (0-255)
    player_dps.append(player_dp)

# Loading deck images
def loadDeck():
    cards = deck.get_deck()
    for card in cards:
        LoadCard(card)

loadDeck()

# Drawing deck
def drawDeck():
    cards = deck.get_deck()
    for i in range(len(cards)):
        displayCard(card_imgs[i], 200 + 6 * i, -30 + screen_height / 2, False)

# Game Booleans
dist = False
first = True
p_index = -1
show = False
win_index = -1
winner = None  # winner
# Defining locations
playersloc = [
    (50, 50),
    (screen_width - 150, 50),
    (50, screen_height - 100),
    (screen_width - 150, screen_height - 100)
]

def load_dp():
    for i in range(4):
        if i == win_index:
            screen.blit(player_dps[i], (360, 100))
        else:
            screen.blit(player_dps[i], (playersloc[i]))

playercord = []

for i in range(4):
    if i < 2:
        if i == 0:
            cord = [playersloc[i][0], playersloc[i][1] + 100]
        else:
            cord = [playersloc[i][0] - 120, playersloc[i][1] + 100]
        playercord.append(cord)
    elif i > 1:
        if i == 2:
            cord = [playersloc[i][0], playersloc[i][1] - 120]
        else:
            cord = [playersloc[i][0] - 120, playersloc[i][1] - 120]

        playercord.append(cord)

def displayCard(img, x, y, show):
    if show is False:
        screen.blit(back_card, (x, y))
    else:
        screen.blit(img, (x, y))

def drawBoard():
    drawDeck()
    drawPlayers()
    pygame.display.flip()

def drawPlayers():
    global first
    global dist
    load_dp()

    if dist is True and first:
        space = 10
        for i in range(3):
            for j in range(4):
                displayCard(hand_imgs[j][i], playercord[j][0] + .5 * space, playercord[j][1], False)
                pygame.time.delay(100)
                pygame.display.update()
                space += 20

        first = False
    elif dist is True and not first:
        space = 10
        for i in range(3):
            for j in range(4):
                if j == (p_index - 1):
                    displayCard(hand_imgs[j][i], playercord[j][0] + .5 * space, playercord[j][1], True)
                elif j != (p_index - 1) and not show:
                    displayCard(hand_imgs[j][i], playercord[j][0] + .5 * space, playercord[j][1], False)
                else:
                    displayCard(hand_imgs[j][i], playercord[j][0] + .5 * space, playercord[j][1], True)
                space += 20

def dis_check():
    for i in range(4):
        players[i].hand.show_hand()

def dis_deck():
    for i in range(3):
        for j in range(4):
            index = len(deck.deck) - 1
            hand_imgs[j].append(card_imgs[index])
            card = deck.draw_Card()
            players[j].give_Card(card)

def winnerr():
    winner = players[0]

    for i in range(3):
        if players[i + 1].winner(winner) == players[i + 1]:
            winner = players[i + 1]

    return winner

def winner_ani():
    global win_index
    winner1 = winnerr()
    for i in range(4):
        if players[i] == winner1:
            player_dps[i].set_alpha(255)
            win_index = i

def reset():
    global dist, first, deck, hand_imgs, card_imgs, p_index, instruction, show, win_index, lock, winner, activate

    instruction = "Select Player 1, 2, 3, 4"
    # Reset game variables
    dist = False
    first = True
    p_index = -1
    show = False
    lock = True
    player_dps[win_index].set_alpha(128)
    win_index = -1
    winner = None
    activate = True
    # Clear hand images
    hand_imgs = []
    card_imgs = []
    loadHandImg()

    # Reset deck
    deck = Deck()
    deck.generate()
    deck.shuffle()
    loadDeck()
    load_dp()
    # Reset each player's hand
    for player in players:
        player.hand.clear()

instruction = "Select Player 1, 2, 3, 4"

lock = True
activate = True
def play():
    global dist, instruction, p_index, first, show, lock, winner, activate
    running = True
    clock = pygame.time.Clock()
    FPS = 60
    handType = ""
    instruction2 = ""
    while running:
        screen.blit(background, (0, 0))
        display_text(instruction, 400, 30, 35, None)
        display_text(instruction2, 400, 60, 30, None)

        if p_index == -1:
            instruction = "Press 1 - 4 to select a player"
        else:
            instruction = "You are \n Player " + str(p_index)
            instruction2 = "Press 'spacebar' to distribute cards"

        if dist == True:
            instruction2 = ""
            display_text("Press 's' to show", 400, 60, 30, None)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not dist:
                    dis_deck()
                    dist = True

                if event.key == pygame.K_1:
                    p_index = 1

                elif event.key == pygame.K_2:
                    p_index = 2

                elif event.key == pygame.K_3:
                    p_index = 3

                elif event.key == pygame.K_4:
                    p_index = 4

                if event.key == pygame.K_KP_ENTER:
                    pygame.quit()
                if event.key == pygame.K_0:
                    dis_check()

                if event.key == pygame.K_r:
                    reset()

                if event.key == pygame.K_s:
                    show = True

        if show and dist and activate:
            winner = winnerr()
            activate = False
            winner_ani()
            handType = winner.hand.identify_hand()

        if show and dist:
            winnerName = winner.name
            textt = winnerName + " with " + handType + " won"
            display_text(textt, 400, 200, 20, None)

        drawBoard()
        clock.tick(FPS)

#play()

# Main Menu
BG = pygame.image.load(os.path.join(res_dir, "Background.png"))

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font(os.path.join(res_dir, "beachfont.otf"), size)

def main_menu():
    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(67).render("FARAS", True, "#b68f40")  # Adjusted font size
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))  # Adjusted position

        PLAY_BUTTON = Button(image=pygame.image.load(os.path.join(res_dir, "Play Rect.png")), pos=(400, 200),  # Adjusted position
                            text_input="PLAY", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load(os.path.join(res_dir, "Options Rect.png")), pos=(400, 300),  # Adjusted position
                            text_input="OPTIONS", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load(os.path.join(res_dir, "Quit Rect.png")), pos=(400, 400),  # Adjusted position
                            text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pass
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
