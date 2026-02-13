class Contest:
    contest_name: str = "NONAME"
    contest_id: int = -1
    start_time: int = -1
    team_name: str = "NOTEAM"
    solved: int = 0
    member1: str = "NOMEMBER"
    member2: str = "NOMEMBER"
    member3: str = "NOMEMBER"
    upsolved1: int = 0
    upsolved2: int = 0
    upsolved3: int = 0


class Team:
    team_name: str = "NOTEAM"
    members: list[str] = ["NOMEMBER"] * 10
    