from random import *
from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def move_character():
    global character_x, character_y
    global hand_x, hand_y

    if character_x < hand_x:
        character_x += 1
    elif character_x > hand_x:
        character_x -= 1

    if character_y < hand_y:
        character_y += 1
    elif character_y > hand_y:
        character_y -= 1


open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

running = True
character_x, character_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
hand_x, hand_y = randint(0, KPU_WIDTH), randint(0, KPU_HEIGHT)
direction = 0  # 0: right / 1: left
frame = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(hand_x, hand_y)

    if hand_x == character_x and hand_y == character_y:
        hand_x = randint(0, KPU_WIDTH)
        hand_y = randint(0, KPU_HEIGHT)

    if character_x <= hand_x:
        direction = 0
    else:
        direction = 1

    if direction == 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, character_x, character_y)
    elif direction == 1:
        character.clip_draw(frame * 100, 0, 100, 100, character_x, character_y)

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()
    move_character()

close_canvas()




