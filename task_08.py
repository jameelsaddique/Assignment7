class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels


class Engine:
    def __init__(self, cc):
        self.cc = cc


class Rickshaw(Vehicle):
    def __init__(self, wheels, engine):
        super().__init__(wheels)
        self.engine = engine


if __name__ == "__main__":
    rickshaw = Rickshaw(wheels=3, engine=Engine(cc=200))
    print(f"IS-A Vehicle: {isinstance(rickshaw, Vehicle)}")
    print(f"HAS-A Engine: {isinstance(rickshaw.engine, Engine)}")
    print(f"IS-A Engine: {isinstance(rickshaw, Engine)}")
    print(f"Wheels: {rickshaw.wheels}, Engine: {rickshaw.engine.cc}cc")
