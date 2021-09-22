input.onButtonPressed(Button.A, function () {
    for (let index = 0; index <= 5; index++) {
        basic.showNumber(5 - index)
    }
    Game = 1
    basic.showIcon(IconNames.Happy)
    baseTempo = control.millis() + 3000
})
function Boucle () {
    score = 0
    while (control.millis() < baseTempo) {
        if (input.isGesture(Gesture.Shake)) {
            score += 1
        }
    }
    basic.showIcon(IconNames.Yes)
    Game = 0
    score = score / 1000
    score = Math.abs(score)
}
input.onButtonPressed(Button.B, function () {
    basic.showString("" + input.temperature() + "C")
})
let baseTempo = 0
let Game = 0
let score = 0
basic.showLeds(`
    . . # # #
    . . # # .
    . . # . .
    . # . # #
    # # . . #
    `)
score = 0
basic.forever(function () {
    if (Game == 1) {
        Boucle()
    }
    basic.showNumber(Math.abs(score))
})
