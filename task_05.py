class Player:
    def __init__(self, name):
        self.name = name


class Batsman(Player):
    def __init__(self, name, runs):
        super().__init__(name)
        self.runs = runs


class Captain(Batsman):
    def __init__(self, name, runs, team):
        super().__init__(name, runs)
        self.team = team

    def report(self):
        print(f"{self.name} | Runs: {self.runs} | Captain of: {self.team}")


if __name__ == "__main__":
    captain = Captain("Babar", 120, "Pakistan")
    captain.report()
