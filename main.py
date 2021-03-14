def 原地右转():
    makerobo.motor_run_dual(makerobo.Motors.LEFT, 150, makerobo.Motors.RIGHT, -150)
def 原地左转():
    makerobo.motor_run_dual(makerobo.Motors.LEFT, -150, makerobo.Motors.RIGHT, 150)
def 右转():
    makerobo.motor_run_dual(makerobo.Motors.LEFT, 200, makerobo.Motors.RIGHT, 0)
def 左转():
    makerobo.motor_run_dual(makerobo.Motors.LEFT, 0, makerobo.Motors.RIGHT, 200)
def 后退():
    makerobo.motor_run_dual(makerobo.Motors.LEFT, -150, makerobo.Motors.RIGHT, -150)
def 前进():
    makerobo.motor_run_dual(makerobo.Motors.LEFT, 120, makerobo.Motors.RIGHT, 120)
def 停止():
    makerobo.motor_run_dual(makerobo.Motors.LEFT, 0, makerobo.Motors.RIGHT, 0)
右侧循迹传感器 = 0
左侧循迹传感器 = 0
火焰传感器的值 = 0
basic.show_icon(IconNames.HAPPY)
while not (input.button_is_pressed(Button.A)):
    停止()
basic.show_icon(IconNames.HEART)

def on_forever():
    global 火焰传感器的值, 左侧循迹传感器, 右侧循迹传感器
    火焰传感器的值 = pins.digital_read_pin(DigitalPin.P5)
    if 火焰传感器的值 == 0:
        makerobo.motor_run(makerobo.Motors.CENTRE, 255)
        停止()
        basic.pause(1000)
    else:
        makerobo.motor_run(makerobo.Motors.CENTRE, 0)
        左侧循迹传感器 = pins.digital_read_pin(DigitalPin.P1)
        右侧循迹传感器 = pins.digital_read_pin(DigitalPin.P2)
        if 左侧循迹传感器 == 1 and 右侧循迹传感器 == 1:
            前进()
        elif 左侧循迹传感器 == 1 and 右侧循迹传感器 == 0:
            左转()
        elif 左侧循迹传感器 == 0 and 右侧循迹传感器 == 1:
            右转()
        else:
            停止()
basic.forever(on_forever)
