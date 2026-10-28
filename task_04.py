class Device:
    def power_on(self):
        print("Power ON")


class Phone(Device):
    def call(self, number):
        print(f"Calling {number}")


class SmartPhone(Phone):
    def browse(self):
        print("Browsing the internet")


if __name__ == "__main__":
    phone = SmartPhone()
    phone.power_on()
    phone.call("0300-1234567")
    phone.browse()
