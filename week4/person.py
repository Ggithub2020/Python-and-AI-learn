class person:
    
    def __init__(self, ID:int, Fname, LName,   SSN):
        self.ID = ID
        self.FName = Fname
        self.LName = LName
        self.SSN = SSN

    def GetFullName(self):
        return f"{self.FName} {self.LName} (ID: {self.ID}) SSN: {self.SSN})"

p=person(1212,  "John", "Doe", "123-45-6789")
p=person(1212, "John", "Doe", "123-45-6789")
print(p.GetFullName())  # Output: John Doe (ID: 1212) SSN: 123-45-6789
