def my_function():
    joystickbit.Vibration_Motor(100)
    basic.show_string("E")
joystickbit.on_button_event(joystickbit.JoystickBitPin.P14,
    joystickbit.ButtonType.DOWN,
    my_function)

def my_function2():
    joystickbit.Vibration_Motor(100)
    basic.show_string("F")
joystickbit.on_button_event(joystickbit.JoystickBitPin.P15,
    joystickbit.ButtonType.DOWN,
    my_function2)

def my_function3():
    joystickbit.Vibration_Motor(100)
    basic.show_string("D")
joystickbit.on_button_event(joystickbit.JoystickBitPin.P13,
    joystickbit.ButtonType.DOWN,
    my_function3)

def my_function4():
    joystickbit.Vibration_Motor(100)
    basic.show_string("C")
joystickbit.on_button_event(joystickbit.JoystickBitPin.P12,
    joystickbit.ButtonType.DOWN,
    my_function4)

y = 0
x = 0
joystickbit.init_joystick_bit()
music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
radio.set_group(7)

def on_forever():
    global x, y
    x = Math.map(joystickbit.get_rocker_value(joystickbit.rockerType.X),
        1023,
        0,
        -100,
        100)
    y = Math.map(joystickbit.get_rocker_value(joystickbit.rockerType.Y),
        1023,
        0,
        -100,
        100)
    radio.send_value("x", x)
    radio.send_value("y", y)
basic.forever(on_forever)
