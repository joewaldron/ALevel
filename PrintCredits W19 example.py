# Hi all - please open the shared folder | Program Examples | OOP Question
# and PyCharm

class PrintAccount:

    def __init__(self, FirstName, LastName, PrintID):
        self.Credits = 50
        self.FirstName = FirstName
        self.LastName = LastName
        self.PrintID = PrintID

    def SetFirstName(self,NewName):
        self.FirstName = NewName

    def GetName(self):
        return self.FirstName + " " + self.LastName

    def GetPrintID(self):
        return self.PrintID

    def AddCredits(self,MoneyInput):
        credits_for_dollar = 25
        bigbonus = 50
        smallbonus = 25
        self.Credits += MoneyInput * credits_for_dollar
        if MoneyInput >= 20:
            self.Credits += bigbonus
        elif 10 <= MoneyInput <= 19:
            self.Credits += smallbonus

Student1 = PrintAccount("John","Eveson","007")
print(Student1.GetName())
Student1.SetFirstName("Johnboy")
print(Student1.GetName())

#DECLARE StudentsAccounts[1:1000] OF PrintAccount
StudentsAccounts = []

def CreateID(FirstName,LastName):
    global StudentsAccounts
    PrintID = FirstName.lower()[:3] + LastName.lower()[:3]+"1"
    for eachaccountpos in range(len(StudentsAccounts)):
        if StudentsAccounts[eachaccountpos].GetPrintID() == PrintID:
            PrintID = PrintID[:-1] + str(int(PrintID[-1])+1)
    StudentsAccounts.append(PrintAccount(FirstName,LastName,PrintID))
