class SpeakMixin:
    def speak(self):
        print("Beep! I can speak")


class WalkMixin:
    def walk(self):
        print("I can walk")


class Robot(SpeakMixin, WalkMixin):
    pass


if __name__ == "__main__":
    robot = Robot()
    robot.speak()
    robot.walk()
