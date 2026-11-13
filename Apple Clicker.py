import pygame
import math
import tkinter as tk
import random
import time

#Create a root window (it won't be shown)                                 # Note to self     Click = harvest / Max = Basket / Auto = Auto harvest / Upgrader = Investor or Seller
root = tk.Tk()

#Get screen width and height
screen_now_width = root.winfo_screenwidth()
screen_now_height = root.winfo_screenheight()

#Destroy the root window to clean up
root.destroy()

screen_old_width = 1800
screen_old_height = 1200

sfx = screen_now_width / screen_old_width                         #SCALE FACTOR X
sfy = screen_now_height / screen_old_height                       #SCALE FACTOR Y

#User num (rand atm)
user_num = random.randint(0, 1000)
print(f"Welcome Apple Harvester {user_num}")

#Prints the screen size
print(f"Screen size: {screen_now_width} x {screen_now_height}")

#Prints the SFX
print(f"SFX: {sfx}")

#Prints the SFY
print(f"SFY: {sfy}")

#Starts Pygame
try:
    pygame.init()
except Exception as e:
    print(f"Pygame initiation failed: {e}")
    exit()

#Window settings
WINDOW_WIDTH = int(screen_now_width)
WINDOW_HEIGHT = int(screen_now_height)

try:
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # X=1800, Y=1200
    pygame.display.set_caption("Apple Clicker")
except Exception as e:
    print(f"Display setup failed: {e}")
    exit()

def hex_to_rgb(hex_colour):
    hex_colour = hex_colour.lstrip("#")
    return tuple(int(hex_colour[i:i+2], 16) for i in (0, 2, 4))

#############-------------------------#############
############# Colours in RedGreenBlue #############
#############-------------------------#############

RED = hex_to_rgb("#FF0000")
ORANGE = hex_to_rgb("#FFBB00")
YELLOW = hex_to_rgb("#FFFF00")
GREEN = hex_to_rgb("#00FF00")
BLUE = hex_to_rgb("#0000FF")
WHITE = hex_to_rgb("#FFFFFF")
GREY = hex_to_rgb("#8C8C8C")
BLACK = hex_to_rgb("#000000")

#(Buttons)
red = hex_to_rgb("#990000")
orange = hex_to_rgb("#AA6600")
yellow = hex_to_rgb("#AAAA00")
green = hex_to_rgb("#009900")
blue = hex_to_rgb("#1111CC")

#(Background)
red_ = hex_to_rgb("#CC0000")
orange_ = hex_to_rgb("#CC8800")
yellow_ = hex_to_rgb("#CCCC00")
green_ = hex_to_rgb("#00CC00")
blue_ = hex_to_rgb("#2222FF")

BACKGROUND = hex_to_rgb("#88e2fb")
SHOP_COLOUR = red_
TRUNK_COLOUR = hex_to_rgb("#5a300c")
HOLE_COLOUR = hex_to_rgb("#48270a")
LEAF_COLOUR = hex_to_rgb("#358e29")

#############----------------------#############
############# HOME & AWAY (X-AXIS) #############
#############----------------------#############

HOME = 1545 * sfx
AWAY = 5000 * sfx
CLOSE_HOME = 1430 * sfx
OPEN_HOME = 1730 * sfx

CLICK_HOME = 1546 * sfx
MAX_HOME = 1593 * sfx
AUTO_HOME = 1640 * sfx
UP_HOME = 1687 * sfx
MIS_HOME = 1734 * sfx

Barrier_HOME = 1500 * sfx
Back_HOME = 1520 * sfx

##################################------------##################################
################################## Shape info ##################################
##################################------------##################################

#Tree info
trunk_width = 135 * sfx
trunk_height = 350 * sfy
trunk_x = ((WINDOW_WIDTH / 2) - trunk_width)
trunk_y = 650 * sfy

leaf1_radius = 150 * sfx
leaf1_x = (trunk_x + (trunk_width / 2))
leaf1_y = (trunk_y - (leaf1_radius / 1.7))

leaf2_radius = 83 * sfx
leaf2_x = AWAY * sfx
leaf2_y = 0 * sfy

leaf3_radius = 71 * sfx
leaf3_x = AWAY * sfx
leaf3_y = 0 * sfy

leaf4_radius = 90 * sfx
leaf4_x = AWAY * sfx
leaf4_y = 0 * sfy

#Hole info
hole_x = AWAY * sfx
hole_y = 0 * sfy
hole_radius = 30 * sfx

#Button stuff (180n - 40) (ALL ONLY FOR Y-AXIS)
b1_y = 140 * sfy
b2_y = 320 * sfy
b3_y = 500 * sfy
b4_y = 680 * sfy

#Click/Max/Auto/Upgrader button info (50x50px with 30px gaps)
click_x = int(AWAY)
click_y = 80 * sfy
click_width = 40 * sfx
click_height = 40 * sfy

max_x = int(AWAY)
max_y = 80 * sfy
max_width = 40 * sfx
max_height = 40 * sfy

harvester_x = int(AWAY)
harvester_y = 80 * sfy
harvester_width = 40 * sfx
harvester_height = 40 * sfy

seller_x = int(AWAY)
seller_y = 80 * sfy
seller_width = 40 * sfx
seller_height = 40 * sfy

mis_x = int(AWAY)
mis_y = 80 * sfy
mis_width = 40 * sfx
mis_height = 40 * sfy

#Shop info
barrier_x = int(AWAY)
barrier_y = 0
barrier_width = 20 * sfx
barrier_height = 1200 * sfy

back_x = int(AWAY)
back_y = 0
back_width = 300 * sfx
back_height = 1200 * sfy

SHOP_TEXT = ""
ofset_x = 90 * sfx
ofset_y = 8 * sfy


########--------------########
######## XP bar stuff ########
########--------------########

#XP bar back
xp_back_x = 0
xp_back_y = 0
xp_back_width = int(WINDOW_WIDTH)
xp_back_height = 50 * sfy

#XP bar 
xp_x = 0
xp_y = 0
xp_width = 0
xp_height = 50 * sfy

#Clicks to fill the bar
click_per_xp = 1/2000

########--------------########
######## Button stuff ########
########--------------########

#Button 1C info
b1C_x = int(AWAY)
b1C_y = int(b1_y)
b1C_width = 230 * sfx
b1C_height = 150 * sfy

#Button 2C info
b2C_x = int(AWAY)
b2C_y = int(b2_y)
b2C_width = 230 * sfx
b2C_height = 150 * sfy

#Button 3C info
b3C_x = int(AWAY)
b3C_y = int(b3_y)
b3C_width = 230 * sfx
b3C_height = 150 * sfy

#Button 4C info
b4C_x = int(AWAY)
b4C_y = int(b4_y)
b4C_width = 230 * sfx
b4C_height = 150 * sfy

#Button 1M info 
b1M_x = int(AWAY)
b1M_y = int(b1_y)
b1M_width = 230 * sfx
b1M_height = 150 * sfy

#Button 2M info
b2M_x = int(AWAY)
b2M_y = int(b2_y)
b2M_width = 230 * sfx
b2M_height = 150 * sfy

#Button 3M info
b3M_x = int(AWAY)
b3M_y = int(b3_y)
b3M_width = 230 * sfx
b3M_height = 150 * sfy

#Button 4M info
b4M_x = int(AWAY)
b4M_y = int(b4_y)
b4M_width = 230 * sfx
b4M_height = 150 * sfy

#Button 1H info 
b1H_x = int(AWAY)
b1H_y = int(b1_y)
b1H_width = 230 * sfx
b1H_height = 150 * sfy

#Button 2H info
b2H_x = int(AWAY)
b2H_y = int(b2_y)
b2H_width = 230 * sfx
b2H_height = 150 * sfy

#Button 3H info
b3H_x = int(AWAY)
b3H_y = int(b3_y)
b3H_width = 230 * sfx
b3H_height = 150 * sfy

#Button 4H info
b4H_x = int(AWAY)
b4H_y = int(b4_y)
b4H_width = 230 * sfx
b4H_height = 150 * sfy

#Button 1S info 
b1S_x = int(AWAY)
b1S_y = int(b1_y)
b1S_width = 230 * sfx
b1S_height = 150 * sfy

#Button 2S info
b2S_x = int(AWAY)
b2S_y = int(b2_y)
b2S_width = 230 * sfx
b2S_height = 150 * sfy

#Button 3S info
b3S_x = int(AWAY)
b3S_y = int(b3_y)
b3S_width = 230 * sfx
b3S_height = 150 * sfy

#Button 4S info
b4S_x = int(AWAY)
b4S_y = int(b4_y)
b4S_width = 230 * sfx
b4S_height = 150 * sfy

#Sell button info
SB1_x = int(AWAY)
SB1_y = int(b1_y)
SB1_width = 230 * sfx
SB1_height = 150 * sfy

#Open button info
ob_x = 1730 * sfx
ob_y = 500 * sfy
ob_width = 40 * sfx
ob_height = 100 * sfy

#Close button info
cb_x = int(AWAY)
cb_y = 500 * sfy
cb_width = 40 * sfx
cb_height = 100 * sfy

############################################----------------############################################
############################################ Game variables ############################################
############################################----------------############################################

apples = 0
maxapples = 0

clickpower = 1
specialclick = 2

AutoHarvest = 0
AutoSell = 0

money = 1000000000 #1000000000
minmoney = 0
xp_bonus = 2000

p1C = 100
p2C = 1000
p3C = 10000
p4C = 100000

p1M = 200
p2M = 2000
p3M = 20000
p4M = 200000

p1H = 300
p2H = 3000
p3H = 30000
p4H = 300000

p1S = 500
p2S = 5000
p3S = 50000
p4S = 500000

xp_increase = WINDOW_WIDTH * click_per_xp

#Abreviation
def abrv (var):
    var_a = var
    var_abrv = ""
    abrv_num = 0

    while var_a >= 1000:
        var_a = var_a / 1000
        abrv_num += 1

    if abrv_num == 1:
        var_abrv = "K"
    elif abrv_num == 1:
        var_abrv = "K"
    elif abrv_num == 2:
        var_abrv = "M"
    elif abrv_num == 3:
        var_abrv = "B"
    elif abrv_num == 4:
        var_abrv = "T"
    elif abrv_num == 5:
        var_abrv = "Qa"
    elif abrv_num == 6:
        var_abrv = "Qn"
    elif abrv_num == 7:
        var_abrv = "Sx"
    elif abrv_num == 8:
        var_abrv = "Sp"
    elif abrv_num == 9:
        var_abrv = "Oc"
    elif abrv_num == 10:
        var_abrv = "No"
    elif abrv_num == 11:
        var_abrv = "Dc"

    var_a = round(var_a, 2)

    return var_a, var_abrv

#Note to self - CMHS is [Click, Max, Harvester, Seller] (Button types)
t = pygame.time.get_ticks()

#Auto apples 
AUTO_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(AUTO_EVENT, 1000)

#Upgrade stuff
SELL_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SELL_EVENT, 1000)

#Text info
try:
    font = pygame.font.SysFont("bahnschrift", int(30 * sfx))
    ob = pygame.font.SysFont("calibri", int(75 * sfx))
    cb = pygame.font.SysFont("calibri", int(75 * sfx))
    TITLE = pygame.font.SysFont("arialblack", int(40 * sfx))
except Exception as e:
    print(f"Font loading failed: {e}")
    pygame.quit()
    exit()

#Game loop control
FPS = 240
clock = pygame.time.Clock()
running = True

#Game loop
while running:
    #Calling abrv sub program
    apples_a, apples_abrv = abrv(apples)
    maxapples_a, maxapples_abrv = abrv(maxapples)

    AutoHarvest_a, AutoHarvest_abrv = abrv(AutoHarvest)
    AutoSell_a, AutoSell_abrv = abrv(AutoSell)

    money_a, money_abrv = abrv(money)

    p1C_a, p1C_abrv = abrv(p1C)
    p2C_a, p2C_abrv = abrv(p2C)
    p3C_a, p3C_abrv = abrv(p3C)
    p4C_a, p4C_abrv = abrv(p4C)

    p1M_a, p1M_abrv = abrv(p1M)
    p2M_a, p2M_abrv = abrv(p2M)
    p3M_a, p3M_abrv = abrv(p3M)
    p4M_a, p4M_abrv = abrv(p4M)

    p1H_a, p1H_abrv = abrv(p1H)
    p2H_a, p2H_abrv = abrv(p2H)
    p3H_a, p3H_abrv = abrv(p3H)
    p4H_a, p4H_abrv = abrv(p4H)

    p1S_a, p1S_abrv = abrv(p1S)
    p2S_a, p2S_abrv = abrv(p2S)
    p3S_a, p3S_abrv = abrv(p3S)
    p4S_a, p4S_abrv = abrv(p4S)

    #XP event
    if xp_width >= int(WINDOW_WIDTH):
        xp_width = 0
        money += xp_bonus
        xp_bonus *= 2

    #Track mouse
    try:
        mouse_x, mouse_y = pygame.mouse.get_pos()

        #Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == AUTO_EVENT:
                apples += AutoHarvest

            elif event.type == SELL_EVENT:
                if AutoSell > 0 and apples > 0:
                    apples -= AutoSell
                    money += AutoSell

            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_processed = False  #No double clicking

                #Hole click
                distance = math.hypot(mouse_x - hole_x, mouse_y - hole_y)
                if distance <= hole_radius:
                    apples += specialclick
                    click_processed = True

                #Tree trunk click
                if not click_processed and (trunk_x <= mouse_x <= trunk_x + trunk_width and
                                            trunk_y <= mouse_y <= trunk_y + trunk_height):
                    apples += clickpower
                    xp_width += int(xp_increase)
                    click_processed = True

                #Leaf clicking
                if not click_processed:
                    distance = math.hypot(mouse_x - leaf1_x, mouse_y - leaf1_y)
                    if distance <= leaf1_radius:
                        apples += clickpower
                        xp_width += int(xp_increase)
                        click_processed = True

                if not click_processed:
                    distance = math.hypot(mouse_x - leaf2_x, mouse_y - leaf2_y)
                    if distance <= leaf2_radius:
                        apples += clickpower
                        xp_width += int(xp_increase)
                        click_processed = True

                if not click_processed:
                    distance = math.hypot(mouse_x - leaf3_x, mouse_y - leaf3_y)
                    if distance <= leaf3_radius:
                        apples += clickpower
                        xp_width += int(xp_increase)
                        click_processed = True

                if not click_processed:
                    distance = math.hypot(mouse_x - leaf4_x, mouse_y - leaf4_y)
                    if distance <= leaf4_radius:
                        apples += clickpower
                        xp_width += int(xp_increase)
                        click_processed = True

                #Button 1C 
                if not click_processed and (b1C_x <= mouse_x <= b1C_x + b1C_width and
                                            b1C_y <= mouse_y <= b1C_y + b1C_height):
                    if money >= p1C:
                        clickpower += 1
                        money -= p1C
                        p1C = round(p1C * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Button 2C 
                if not click_processed and (b2C_x <= mouse_x <= b2C_x + b2C_width and
                                            b2C_y <= mouse_y <= b2C_y + b2C_height):
                    if money >= p2C:
                        clickpower += 10
                        money -= p2C
                        p2C = round(p2C * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Button 3C 
                if not click_processed and (b3C_x <= mouse_x <= b3C_x + b3C_width and
                                            b3C_y <= mouse_y <= b3C_y + b3C_height):
                    if money >= p3C:
                        clickpower += 100
                        money -= p3C
                        p3C = round(p3C * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                 #Button 4C 
                if not click_processed and (b4C_x <= mouse_x <= b4C_x + b4C_width and
                                            b4C_y <= mouse_y <= b4C_y + b4C_height):
                    if money >= p4C:
                        clickpower += 1000
                        money -= p4C
                        p4C = round(p4C * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Button 1M
                if not click_processed and (b1M_x <= mouse_x <= b1M_x + b1M_width and
                                            b1M_y <= mouse_y <= b1M_y + b1M_height):
                    if money >= p1M:
                        maxapples += 10
                        money -= p1M
                        p1M = round(p1M * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Button 2M 
                if not click_processed and (b2M_x <= mouse_x <= b2M_x + b2M_width and
                                            b2M_y <= mouse_y <= b2M_y + b2M_height):
                    if money >= p2M:
                        maxapples += 100
                        money -= p2M
                        p2M = round(p2M * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Button 3M 
                if not click_processed and (b3M_x <= mouse_x <= b3M_x + b3M_width and
                                            b3M_y <= mouse_y <= b3M_y + b3M_height):
                    if money >= p3M:
                        maxapples += 1000
                        money -= p3M
                        p3M = round(p3M * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Button 4M 
                if not click_processed and (b4M_x <= mouse_x <= b4M_x + b4M_width and
                                            b4M_y <= mouse_y <= b4M_y + b4M_height):
                    if money >= p4M:
                        maxapples += 10000
                        money -= p4M
                        p4M = round(p4M * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Button 1H
                if not click_processed and (b1H_x <= mouse_x <= b1H_x + b1H_width and
                                            b1H_y <= mouse_y <= b1H_y + b1H_height):
                    if money >= p1H:
                        AutoHarvest += 1
                        money -= p1H
                        p1H = round(p1H * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Button 2H 
                if not click_processed and (b2H_x <= mouse_x <= b2H_x + b2H_width and
                                            b2H_y <= mouse_y <= b2H_y + b2H_height):
                    if money >= p2H:
                        AutoHarvest += 10
                        money -= p2H
                        p2H = round(p2H * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Button 3H 
                if not click_processed and (b3H_x <= mouse_x <= b3H_x + b3H_width and
                                            b3H_y <= mouse_y <= b3H_y + b3H_height):
                    if money >= p3H:
                        AutoHarvest += 100
                        money -= p3H
                        p3H = round(p3H * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Button 4H 
                if not click_processed and (b4H_x <= mouse_x <= b4H_x + b4H_width and
                                            b4H_y <= mouse_y <= b4H_y + b4H_height):
                    if money >= p4H:
                        AutoHarvest += 1000
                        money -= p4H
                        p4H = round(p4H * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Button 1S
                if not click_processed and (b1S_x <= mouse_x <= b1S_x + b1S_width and
                                            b1S_y <= mouse_y <= b1S_y + b1S_height):
                    if money >= p1S:
                        AutoSell += 1
                        money -= p1S
                        p1S = round(p1S * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Button 2S 
                if not click_processed and (b2S_x <= mouse_x <= b2S_x + b2S_width and
                                            b2S_y <= mouse_y <= b2S_y + b2S_height):
                    if money >= p2S:
                        AutoSell += 10
                        money -= p2S
                        p2S = round(p2S * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Button 3S 
                if not click_processed and (b3S_x <= mouse_x <= b3S_x + b3S_width and
                                            b3S_y <= mouse_y <= b3S_y + b3S_height):
                    if money >= p3S:
                        AutoSell += 100
                        money -= p3S
                        p3S = round(p3S * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Button 4S 
                if not click_processed and (b4S_x <= mouse_x <= b4S_x + b4S_width and
                                            b4S_y <= mouse_y <= b4S_y + b4S_height):
                    if money >= p4S:
                        AutoSell += 1000
                        money -= p4S
                        p4S = round(p4S * 1.01, 2)
                        money = round(money, 2)
                        click_processed = True

                #Sell button click
                if not click_processed and (SB1_x <= mouse_x <= SB1_x + SB1_width and
                                            SB1_y <= mouse_y <= SB1_y + SB1_height):
                    money += apples
                    apples = 0
                    click_processed = True

                #Open button click
                if not click_processed and (ob_x <= mouse_x <= ob_x + ob_width and
                                            ob_y <= mouse_y <= ob_y + ob_height):

                    b1C_x = int(HOME)
                    b2C_x = int(HOME)
                    b3C_x = int(HOME)
                    b4C_x = int(HOME)

                    ob_x = int(AWAY)
                    cb_x = int(CLOSE_HOME)

                    barrier_x = int(Barrier_HOME)
                    back_x = int(Back_HOME)

                    click_x = int(CLICK_HOME)
                    max_x = int(MAX_HOME)
                    harvester_x = int(AUTO_HOME)
                    seller_x = int(UP_HOME)
                    mis_x = int(MIS_HOME)
                    
                    SHOP_TEXT = "Click"

                    click_processed = True

                #Close button click
                if not click_processed and (cb_x <= mouse_x <= cb_x + cb_width and
                                            cb_y <= mouse_y <= cb_y + cb_height):
                    b1C_x = int(AWAY)
                    b2C_x = int(AWAY)
                    b3C_x = int(AWAY)
                    b4C_x = int(AWAY)

                    b1M_x = int(AWAY)
                    b2M_x = int(AWAY)
                    b3M_x = int(AWAY)
                    b4M_x = int(AWAY)

                    b1H_x = int(AWAY)
                    b2H_x = int(AWAY)
                    b3H_x = int(AWAY)
                    b4H_x = int(AWAY)

                    b1S_x = int(AWAY)
                    b2S_x = int(AWAY)
                    b3S_x = int(AWAY)
                    b4S_x = int(AWAY)

                    cb_x = int(AWAY)
                    ob_x = int(OPEN_HOME)

                    barrier_x = int(AWAY)
                    back_x = int(AWAY)

                    click_x = int(AWAY)
                    max_x = int(AWAY)
                    harvester_x = int(AWAY)
                    seller_x = int(AWAY)
                    mis_x = int(AWAY)

                    SB1_x = int(AWAY)

                    click_processed = True

                #"Click" shop types click
                if not click_processed and (click_x <= mouse_x <= click_x + click_width and
                                            click_y <= mouse_y <= click_y + click_height):
                    b1C_x = int(HOME) 
                    b2C_x = int(HOME)                                                                                        #  <----  ADD NEW CLICK UPGRADE BUTTONS HERE
                    b3C_x = int(HOME)
                    b4C_x = int(HOME)

                    SHOP_TEXT = "Click"
                    SHOP_COLOUR = red_

                    ofset_x = int((sfx) * 85)
                    b1M_x = int(AWAY)
                    b2M_x = int(AWAY)
                    b3M_x = int(AWAY)
                    b4M_x = int(AWAY)
                    
                    b1H_x = int(AWAY)
                    b2H_x = int(AWAY)
                    b3H_x = int(AWAY)
                    b4H_x = int(AWAY)
                    
                    b1S_x = int(AWAY)
                    b2S_x = int(AWAY)
                    b3S_x = int(AWAY)
                    b4S_x = int(AWAY)
                    
                    SB1_x = int(AWAY)
                    click_processed = True

                #"Max" shop types click
                if not click_processed and (max_x <= mouse_x <= max_x + max_width and
                                            max_y <= mouse_y <= max_y + max_height):
                    b1M_x = int(HOME)
                    b2M_x = int(HOME)                                                                                        #  <----  ADD NEW MAX UPGRADE BUTTONS HERE
                    b3M_x = int(HOME)
                    b4M_x = int(HOME)

                    SHOP_TEXT = "Max"
                    SHOP_COLOUR = orange_

                    ofset_x = int((sfx) * 95)
                    b1C_x = int(AWAY)
                    b2C_x = int(AWAY)
                    b3C_x = int(AWAY)
                    b4C_x = int(AWAY)
                    
                    b1H_x = int(AWAY)
                    b2H_x = int(AWAY)
                    b3H_x = int(AWAY)
                    b4H_x = int(AWAY)
                    
                    b1S_x = int(AWAY)
                    b2S_x = int(AWAY)
                    b3S_x = int(AWAY)
                    b4S_x = int(AWAY)
                    
                    
                    SB1_x = int(AWAY)
                    click_processed = True

                #"Harvester" shop type click
                if not click_processed and (harvester_x <= mouse_x <= harvester_x + harvester_width and
                                            harvester_y <= mouse_y <= harvester_y + harvester_height):
                    b1H_x = int(HOME)
                    b2H_x = int(HOME)                                                                                        #  <----  ADD NEW AUTO UPGRADE BUTTONS HERE
                    b3H_x = int(HOME)
                    b4H_x = int(HOME)

                    SHOP_TEXT = "Harvester"
                    SHOP_COLOUR = yellow_

                    ofset_x = int((sfx) * 35)
                    b1C_x = int(AWAY)
                    b2C_x = int(AWAY)
                    b3C_x = int(AWAY)
                    b4C_x = int(AWAY)
                    
                    b1M_x = int(AWAY)
                    b2M_x = int(AWAY)
                    b3M_x = int(AWAY)
                    b4M_x = int(AWAY)
                    
                    b1S_x = int(AWAY)
                    b2S_x = int(AWAY)
                    b3S_x = int(AWAY)
                    b4S_x = int(AWAY)
                    
                    SB1_x = int(AWAY)
                    click_processed = True

                #"Seller" shop type click
                if not click_processed and (seller_x <= mouse_x <= seller_x + seller_width and
                                            seller_y <= mouse_y <= seller_y + seller_height):
                    b1S_x = int(HOME)
                    b2S_x = int(HOME)                                                                                        #  <----  ADD NEW AUTO UPGRADE BUTTONS HERE
                    b3S_x = int(HOME)
                    b4S_x = int(HOME)

                    SHOP_TEXT = "Seller"
                    SHOP_COLOUR = green_

                    ofset_x = int((sfx) * 76)
                    b1C_x = int(AWAY)
                    b2C_x = int(AWAY)
                    b3C_x = int(AWAY)
                    b4C_x = int(AWAY)
                    
                    b1M_x = int(AWAY)
                    b2M_x = int(AWAY)
                    b3M_x = int(AWAY)
                    b4M_x = int(AWAY)
                    
                    b1H_x = int(AWAY)
                    b2H_x = int(AWAY)
                    b3H_x = int(AWAY)
                    b4H_x = int(AWAY)
                    
                    SB1_x = int(AWAY)
                    click_processed = True

                #"MISCELLANEOUS" shop types click
                if not click_processed and (mis_x <= mouse_x <= mis_x + mis_width and
                                            mis_y <= mouse_y <= mis_y + mis_height):
                    SB1_x = int(HOME)                                                                                        #  <----  ADD NEW MISCELLANEOUS BUTTONS HERE

                    SHOP_TEXT = "Other"
                    SHOP_COLOUR = blue_

                    ofset_x = int((sfx) * 75)
                    b1C_x = int(AWAY)
                    b2C_x = int(AWAY)
                    b3C_x = int(AWAY)
                    b4C_x = int(AWAY)
                    
                    b1M_x = int(AWAY)
                    b2M_x = int(AWAY)
                    b3M_x = int(AWAY)
                    b4M_x = int(AWAY)
                    
                    b1H_x = int(AWAY)
                    b2H_x = int(AWAY)
                    b3H_x = int(AWAY)
                    b4H_x = int(AWAY)
                    
                    b1S_x = int(AWAY)
                    b2S_x = int(AWAY)
                    b3S_x = int(AWAY)
                    b4S_x = int(AWAY)
                    click_processed = True

        #Cap apples
        if apples > maxapples:
            apples = maxapples
            
        #XP increase cap when basket is full
        if apples == maxapples:
            xp_increase = 0

        if apples < maxapples:
            xp_increase = WINDOW_WIDTH * click_per_xp

        ########################################---------------########################################
        ######################################## Drawing Stuff ########################################
        ########################################---------------########################################

        #Draws the tree
        screen.fill(BACKGROUND)
        pygame.draw.rect(screen, TRUNK_COLOUR, (trunk_x, trunk_y, trunk_width, trunk_height))  
        pygame.draw.circle(screen, LEAF_COLOUR, (leaf1_x, leaf1_y), leaf1_radius)
        pygame.draw.circle(screen, LEAF_COLOUR, (leaf2_x, leaf2_y), leaf2_radius)
        pygame.draw.circle(screen, LEAF_COLOUR, (leaf3_x, leaf3_y), leaf3_radius)
        pygame.draw.circle(screen, LEAF_COLOUR, (leaf4_x, leaf4_y), leaf4_radius)
        pygame.draw.circle(screen, HOLE_COLOUR, (hole_x, hole_y), hole_radius)

        #Draws XP bar
        pygame.draw.rect(screen, GREY, (xp_back_x, xp_back_y, xp_back_width, xp_back_height))
        pygame.draw.rect(screen, YELLOW, (xp_x, xp_y, xp_width, xp_height))

        #Draws shop
        pygame.draw.rect(screen, BLACK, (barrier_x, barrier_y, barrier_width, barrier_height))
        pygame.draw.rect(screen, SHOP_COLOUR, (back_x, back_y, back_width, back_height))

        pygame.draw.rect(screen, red, (b1C_x, b1C_y, b1C_width, b1C_height))
        pygame.draw.rect(screen, red, (b2C_x, b2C_y, b2C_width, b2C_height))
        pygame.draw.rect(screen, red, (b3C_x, b3C_y, b3C_width, b3C_height))
        pygame.draw.rect(screen, red, (b4C_x, b4C_y, b4C_width, b4C_height))

        pygame.draw.rect(screen, orange, (b1M_x, b1M_y, b1M_width, b1M_height))
        pygame.draw.rect(screen, orange, (b2M_x, b2M_y, b2M_width, b2M_height))
        pygame.draw.rect(screen, orange, (b3M_x, b3M_y, b3M_width, b3M_height))
        pygame.draw.rect(screen, orange, (b4M_x, b4M_y, b4M_width, b4M_height))

        pygame.draw.rect(screen, yellow, (b1H_x, b1H_y, b1H_width, b1H_height))
        pygame.draw.rect(screen, yellow, (b2H_x, b2H_y, b2H_width, b2H_height))
        pygame.draw.rect(screen, yellow, (b3H_x, b3H_y, b3H_width, b3H_height))
        pygame.draw.rect(screen, yellow, (b4H_x, b4H_y, b4H_width, b4H_height))
        

        pygame.draw.rect(screen, green, (b1S_x, b1S_y, b1S_width, b1S_height))
        pygame.draw.rect(screen, green, (b2S_x, b2S_y, b2S_width, b2S_height))
        pygame.draw.rect(screen, green, (b3S_x, b3S_y, b3S_width, b3S_height))
        pygame.draw.rect(screen, green, (b4S_x, b4S_y, b4S_width, b4S_height))

        #Draws sell button
        pygame.draw.rect(screen, blue, (SB1_x, SB1_y, SB1_width, SB1_height))

        #Draws open & close buttons
        pygame.draw.rect(screen, BACKGROUND, (ob_x, ob_y, ob_width, ob_height))
        pygame.draw.rect(screen, BACKGROUND, (cb_x, cb_y, cb_width, cb_height))

        #Draws shop type swappers
        pygame.draw.rect(screen, red, (click_x, click_y, click_width, click_height))
        pygame.draw.rect(screen, orange, (max_x, max_y, max_width, max_height))
        pygame.draw.rect(screen, yellow, (harvester_x, harvester_y, harvester_width, harvester_height))
        pygame.draw.rect(screen, green, (seller_x, seller_y, seller_width, seller_height))
        pygame.draw.rect(screen, blue, (mis_x, mis_y, mis_width, mis_height))

        #Score text
        apples_text = font.render(f"Apples: {apples_a}{apples_abrv}/{maxapples_a}{maxapples_abrv}", True, BLACK)
        screen.blit(apples_text, (10 * sfx, 60 * sfy))

        money_text = font.render(f"Money: £{money_a}{money_abrv}", True, BLACK)
        screen.blit(money_text, (10 * sfx, 100 * sfy))

        AutoH_num = font.render(f"Auto H: {AutoHarvest_a}{AutoHarvest_abrv}", True, BLACK)
        screen.blit(AutoH_num, (10 * sfx, 140 * sfy))

        AutoS_num = font.render(f"Auto S: {AutoSell_a}{AutoSell_abrv}", True, BLACK)
        screen.blit(AutoS_num, (10 * sfx, 180 * sfy))

        #Button 1C text
        b1C_text = font.render("Click [+1]", True, BLACK)
        screen.blit(b1C_text, (b1C_x + 10 * sfx, b1C_y + 40 * sfy))

        p1C_text = font.render(f"£{p1C_a}{p1C_abrv}", True, BLACK)
        screen.blit(p1C_text, (b1C_x + 10 * sfx, b1C_y + 80 * sfy))

        #Button 2C text
        b2C_text = font.render("Click [+10]", True, BLACK)
        screen.blit(b2C_text, (b2C_x + 10 * sfx, b2C_y + 40 * sfy))

        p2C_text = font.render(f"£{p2C_a}{p2C_abrv}", True, BLACK)
        screen.blit(p2C_text, (b2C_x + 10 * sfx, b2C_y + 80 * sfy))

        #Button 3C text
        b3C_text = font.render("Click [+100]", True, BLACK)
        screen.blit(b3C_text, (b3C_x + 10 * sfx, b3C_y + 40 * sfy))

        p3C_text = font.render(f"£{p3C_a}{p3C_abrv}", True, BLACK)
        screen.blit(p3C_text, (b3C_x + 10 * sfx, b3C_y + 80 * sfy))

        #Button 4C text
        b4C_text = font.render("Click [+1K]", True, BLACK)
        screen.blit(b4C_text, (b4C_x + 10 * sfx, b4C_y + 40 * sfy))

        p4C_text = font.render(f"£{p4C_a}{p4C_abrv}", True, BLACK)
        screen.blit(p4C_text, (b4C_x + 10 * sfx, b4C_y + 80 * sfy))

        #Button 1M text
        b1M_text = font.render("Max [+10]", True, BLACK)
        screen.blit(b1M_text, (b1M_x + 10 * sfx, b1M_y + 40 * sfy))

        p1M_text = font.render(f"£{p1M_a}{p1M_abrv}", True, BLACK)
        screen.blit(p1M_text, (b1M_x + 10 * sfx, b1M_y + 80 * sfy))

        #Button 2M text
        b2M_text = font.render("Max [+100]", True, BLACK)
        screen.blit(b2M_text, (b2M_x + 10 * sfx, b2M_y + 40 * sfy))

        p2M_text = font.render(f"£{p2M_a}{p2M_abrv}", True, BLACK)
        screen.blit(p2M_text, (b2M_x + 10 * sfx, b2M_y + 80 * sfy))

        #Button 3M text
        b3M_text = font.render("Max [+1K]", True, BLACK)
        screen.blit(b3M_text, (b3M_x + 10 * sfx, b3M_y + 40 * sfy))

        p3M_text = font.render(f"£{p3M_a}{p3M_abrv}", True, BLACK)
        screen.blit(p3M_text, (b3M_x + 10 * sfx, b3M_y + 80 * sfy))

        #Button 4M text
        b4M_text = font.render("Max [+10K]", True, BLACK)
        screen.blit(b4M_text, (b4M_x + 10 * sfx, b4M_y + 40 * sfy))

        p4M_text = font.render(f"£{p4M_a}{p4M_abrv}", True, BLACK)
        screen.blit(p4M_text, (b4M_x + 10 * sfx, b4M_y + 80 * sfy))

        #Button 1H text
        b1H_text = font.render("Auto H [+1]", True, BLACK)
        screen.blit(b1H_text, (b1H_x + 10 * sfx, b1H_y + 40 * sfy))

        b1H_text = font.render(f"£{p1H_a}{p1H_abrv}", True, BLACK)
        screen.blit(b1H_text, (b1H_x + 10 * sfx, b1H_y + 80 * sfy))

        #Button 2H text
        b2H_text = font.render("Auto H [+10]", True, BLACK)
        screen.blit(b2H_text, (b2H_x + 10 * sfx, b2H_y + 40 * sfy))

        b2H_text = font.render(f"£{p2H_a}{p2H_abrv}", True, BLACK)
        screen.blit(b2H_text, (b2H_x + 10 * sfx, b2H_y + 80 * sfy))

        #Button 3H text
        b3H_text = font.render("Auto H [+100]", True, BLACK)
        screen.blit(b3H_text, (b3H_x + 10 * sfx, b3H_y + 40 * sfy))

        b3H_text = font.render(f"£{p3H_a}{p3H_abrv}", True, BLACK)
        screen.blit(b3H_text, (b3H_x + 15 * sfx, b3H_y + 80 * sfy))

        #Button 4H text
        b4H_text = font.render("Auto H [+1K]", True, BLACK)
        screen.blit(b4H_text, (b4H_x + 10 * sfx, b4H_y + 40 * sfy))

        p4H_text = font.render(f"£{p4H_a}{p4H_abrv}", True, BLACK)
        screen.blit(p4H_text, (b4H_x + 10 * sfx, b4H_y + 80 * sfy))

        #Button 1S text
        b1S_text = font.render("Auto S [+1]", True, BLACK)
        screen.blit(b1S_text, (b1S_x + 10 * sfx, b1S_y + 40 * sfy))

        p1S_text = font.render(f"£{p1S_a}{p1S_abrv}", True, BLACK)
        screen.blit(p1S_text, (b1S_x + 10 * sfx, b1S_y + 80 * sfy))

        #Button 2S text
        b2S_text = font.render("Auto S [+10]", True, BLACK)
        screen.blit(b2S_text, (b2S_x + 10 * sfx, b2S_y + 40 * sfy))

        p2S_text = font.render(f"£{p2S_a}{p2S_abrv}", True, BLACK)
        screen.blit(p2S_text, (b2S_x + 10 * sfx, b2S_y + 80 * sfy))

        #Button 3S text
        b3S_text = font.render("Auto S [+100]", True, BLACK)
        screen.blit(b3S_text, (b3S_x + 10 * sfx, b3S_y + 40 * sfy))

        p3S_text = font.render(f"£{p3S_a}{p3S_abrv}", True, BLACK)
        screen.blit(p3S_text, (b3S_x + 10 * sfx, b3S_y + 80 * sfy))

        #Button 4S text
        b4S_text = font.render("Auto S [+1K]", True, BLACK)
        screen.blit(b4S_text, (b4S_x + 10 * sfx, b4S_y + 40 * sfy))

        p4S_text = font.render(f"£{p4S_a}{p4S_abrv}", True, BLACK)
        screen.blit(p4S_text, (b4S_x + 10 * sfx, b4S_y + 80 * sfy))

        #Other buttons texts
        SB1_text = font.render("Sell all apples", True, BLACK)
        screen.blit(SB1_text, (SB1_x + 20 * sfx, SB1_y + 50 * sfy))

        #Open & Close texts
        open = ob.render(f"<", True, BLACK)
        screen.blit(open, (ob_x + 3 * sfx, ob_y + 12 * sfy))

        close = cb.render(f">", True, BLACK)
        screen.blit(close, (cb_x + 3 * sfx, cb_y + 12 * sfy))

        #Shop text
        shop_type = TITLE.render(f"{SHOP_TEXT}", True, BLACK)
        screen.blit(shop_type, (back_x + ofset_x, back_y + ofset_y))

        #Update display
        pygame.display.flip()
        clock.tick(FPS)

    except Exception as e:
        print(f"Error in game loop: {e}")
        running = False

#Quit game
pygame.quit()