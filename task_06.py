class Father:
    def skill(self):
        return "Cricket"


class Mother:
    def skill(self):
        return "Painting"


class Child1(Father, Mother):
    pass


class Child2(Mother, Father):
    pass


if __name__ == "__main__":
    print(f"Child1: {Child1().skill()}")
    print(f"Child2: {Child2().skill()}")
    print([parent.__name__ for parent in Child1.__mro__])
