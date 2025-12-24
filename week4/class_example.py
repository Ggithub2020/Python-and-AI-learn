class person:
    def __init__(self, ID: int, Fname: str, LName: str, SSN: str):
        self.ID = ID
        self.FName = Fname
        self.LName = LName
        self.SSN = SSN

    def GetFullName(self) -> str:
        return f"{self.FName} {self.LName} (ID: {self.ID}) SSN: {self.SSN}"