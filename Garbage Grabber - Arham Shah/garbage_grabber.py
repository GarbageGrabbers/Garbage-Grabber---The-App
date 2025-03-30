import pgzrun
from random import randint
import time
WIDTH = 1080
HEIGHT = 1080
score = 0
timer = 60
game_over = False
player = Actor("humanplayer")
player.pos = randint(100,950), randint(100,950)
garbage = Actor("trash")
garbage.pos =  randint(100,950), randint(100,950)
elements = Actor("elements")
end=Actor("end")
def draw():
    if timer<=0:
        background = Actor("end")
        end.draw()
        screen.draw.text(str(score), topleft=(500, 500), fontsize=120)
    else:
        background = Actor("background")
        background.draw()
        player.draw()
        garbage.draw()
        elements.draw()
        screen.draw.text("Time: " + str(round(timer, 2)),(780,10),color="black", fontsize = 70)
        screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10), fontsize = 70)
if timer<0:
    print('Game Over')
    screen.fill("pink")
    screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)
def place_garbage():
    garbage.x = randint(20, (WIDTH - 20))
    garbage.y = randint(130, (HEIGHT - 20))
def time_up():
    global game_over
    game_over = True
def update():
    global score
    global timer
    if keyboard.left:
        player.x = player.x - 2
    elif keyboard.right:
        player.x = player.x + 2
    elif keyboard.up:
        player.y = player.y - 2
    elif keyboard.down:
        player.y = player.y + 2
    garbage_collected = player.colliderect(garbage)
    if garbage_collected:
        score = score + 10
        place_garbage()
    if player.x < 0:
        player.x = 1080
    if player.x >1080:
        player.x = 0
    if player.y < 130:
        player.y = 1080
    if player.y >1080:
        player.y = 130

    if timer <= 0:
        return
        screen.clear()
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)
    else:
        timer-= 1/60
        
place_garbage()
pgzrun.go()
