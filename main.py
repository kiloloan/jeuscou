def on_button_pressed_a():
    global Game, baseTempo
    for index in range(6):
        basic.show_number(5 - index)
    Game = 1
    basic.show_icon(IconNames.HAPPY)
    baseTempo = control.millis() + 3000
input.on_button_pressed(Button.A, on_button_pressed_a)

def Boucle():
    global score, Game
    score = 0
    while control.millis() < baseTempo:
        if input.is_gesture(Gesture.SHAKE):
            score += 1
    basic.show_icon(IconNames.YES)
    Game = 0
    score = score / 1000
    score = abs(score)

def on_button_pressed_b():
    basic.show_string("" + str(input.temperature()) + "C")
input.on_button_pressed(Button.B, on_button_pressed_b)

baseTempo = 0
Game = 0
score = 0
basic.show_leds("""
    . . # # #
        . . # # .
        . . # . .
        . # . # #
        # # . . #
""")
score = 0

def on_forever():
    if Game == 1:
        Boucle()
    basic.show_number(abs(score))
basic.forever(on_forever)
