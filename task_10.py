class Person:
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name

    def skills(self):
        return []


class Player(Person):
    def skills(self):
        return super().skills() + ["Fitness"]


class Batsman(Player):
    role = "Batsman"

    def __init__(self, runs, **kwargs):
        super().__init__(**kwargs)
        self.runs = runs

    def skills(self):
        return super().skills() + [f"Batting ({self.runs} runs)"]


class Bowler(Player):
    role = "Bowler"

    def __init__(self, wickets, **kwargs):
        super().__init__(**kwargs)
        self.wickets = wickets

    def skills(self):
        return super().skills() + [f"Bowling ({self.wickets} wickets)"]


class AllRounder(Batsman, Bowler):
    role = "AllRounder"


class Coach:
    def __init__(self, name):
        self.name = name


class Academy:
    def __init__(self, coach, players):
        self.coach = coach
        self.players = players

    def report(self):
        print(f"Coach: {self.coach.name}")
        for player in self.players:
            skills = ", ".join(player.skills())
            print(f"- {player.name} ({player.role}): {skills}")


if __name__ == "__main__":
    academy = Academy(
        Coach("Misbah"),
        [
            Batsman(name="Babar", runs=120),
            Bowler(name="Shaheen", wickets=5),
            AllRounder(name="Shadab", runs=40, wickets=3),
        ],
    )
    academy.report()
    mro = " -> ".join(cls.__name__ for cls in AllRounder.__mro__)
    print(f"AllRounder MRO: {mro}")
