let x = 0
let y = 0
input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    x = randint(1, 5)
    y = randint(1, 5)
    led.plot(x, y)
})
