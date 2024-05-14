x = 0
y = 0

def on_button_pressed_a():
    global x, y
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    x = randint(1, 5)
    y = randint(1, 5)
    led.plot(x, y)
input.on_button_pressed(Button.A, on_button_pressed_a)
