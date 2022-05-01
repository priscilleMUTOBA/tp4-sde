#exercice 1
def on_forever():
    if input.button_is_pressed(Button.B):
        basic.show_number(input.temperature()) 
    elif input.logo_is_pressed(): 
        basic.show_icon(input.light_level())
basic.forever(on_forever)

#exercice 2
def on_forever():
    images.icon_image(IconNames.SQUARE).show_image(0)
    if input.logo_is_pressed():
        images.icon_image(IconNames.SMALL_SQUARE).show_image(0)
basic.forever(on_forever)

 #exrcice 3
def on_sound_loud():
    for index in range(5):
        led.plot(index, 0)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

#exrcice 4
def on_forever():
    angle= input.compass_heading()
    if angle< 45 or angle> 315:
        basic.show_string("N")
        basic.show_number(input.sound_level())
    elif angle< 135:
        basic.show_string("E")
        basic.show_number(input.light_level())
    elif angle< 225:
        basic.show_string("S")
        basic.show_number(input.sound_level())
    elif angle< 315:
        basic.show_string("O")
        basic.show_number(input.light_level())
    else:
        basic.clear_screen()
basic.forever(on_forever)


#exrcice 5
gauche = 0
droite = 0

def on_forever():
    global gauche, droite
    i = 0
    gauche = 0
    droite = 0
    while i >= 0:
        if input.is_gesture(Gesture.TILT_LEFT):
            gauche += 1
            basic.show_string("G")
            basic.show_number(gauche)
        elif input.is_gesture(Gesture.TILT_RIGHT):
            droite += 1
            basic.show_string("D")
            basic.show_number(droite)
basic.forever(on_forever)
