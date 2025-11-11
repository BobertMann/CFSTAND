class Contest:
    name: str = "NONAME"
    contest_id: int = -1
    team_name: str = "NOTEAM"
    solved: int = 0
    member1: str = "NOMEMBER"
    member2: str = "NOMEMBER"
    member3: str = "NOMEMBER"
    solved1: int = 0
    solved2: int = 0
    solved3: int = 0
    start_time: int = -1
    def __init__(self, contest_id: int, name: str, verdict: str = "UNKNOWN"):
        self.contest_id = contest_id
        self.name = name
        self.verdict = verdict
    def __repr__(self):
        return f"Contest({self.contest_id!r}, {self.name!r}, {self.verdict!r})"
    def __eq__(self, other):
        return isinstance(other, Contest) and (self.__dict__ == other.__dict__)