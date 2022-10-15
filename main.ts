joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P14, joystickbit.ButtonType.down, function () {
    joystickbit.Vibration_Motor(100)
    basic.showString("E")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P15, joystickbit.ButtonType.down, function () {
    joystickbit.Vibration_Motor(100)
    basic.showString("F")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P13, joystickbit.ButtonType.down, function () {
    joystickbit.Vibration_Motor(100)
    basic.showString("D")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P12, joystickbit.ButtonType.down, function () {
    joystickbit.Vibration_Motor(100)
    basic.showString("C")
})
let y = 0
let x = 0
joystickbit.initJoystickBit()
music.startMelody(music.builtInMelody(Melodies.BaDing), MelodyOptions.Once)
radio.setGroup(7)
basic.forever(function () {
    x = Math.map(joystickbit.getRockerValue(joystickbit.rockerType.X), 1023, 0, -100, 100)
    y = Math.map(joystickbit.getRockerValue(joystickbit.rockerType.Y), 1023, 0, -100, 100)
    radio.sendValue("x", x)
    radio.sendValue("y", y)
})
