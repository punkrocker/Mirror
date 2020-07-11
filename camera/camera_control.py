import time
from PCA9685 import PCA9685

pwm = PCA9685()
x = 90
y = 40
try:
    print("This is an PCA9685 routine")
    pwm.setPWMFreq(50)
    # 初始位置
    pwm.setRotationAngle(1, x)
    pwm.setRotationAngle(0, y)
    is_up = False
    is_right = False
    while True:
        if is_up:
            y += 1
        else:
            y -= 1
        if y >= 80:
            is_up = False
        elif y <= 10:
            is_up = True
        pwm.setRotationAngle(0, y)

        if is_right:
            x += 1
        else:
            x -= 1
        if x >= 170:
            is_right = False
        elif x <= 10:
            is_right = True
        pwm.setRotationAngle(1, x)
        print(str(x) + ":" + str(y))
        time.sleep(0.1)


except Exception as e:
    print(str(e))
    pwm.exit_PCA9685()
    print("\nProgram end")
    exit()
