class ENTERPRISE:
    def __init__(self, name, finance: int, year, owner):
        self.__Name = name
        self.__Finance = finance
        self.__Year = year
        self.__Owner = owner

    def SetFinance(self, finance):
        self.__Finance = finance

    def GetFinance(self):
        return self.__Finance

    def SetOwner(self, owner):
        self.__Owner = owner

    def GetOwner(self):
        return self.__Owner

    def DisplayAll(self):
        print(str(self))

    def __str__(self):
        return f"{self.__Name=}, {self.__Finance=}, {self.__Year=}, {self.__Owner=}"
