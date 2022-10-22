import os


class RIVER:
    def __init__(self, name, continent, length):
        self.name = name
        self.continent = continent
        self.length = length

    def setName(self, name):
        self.name = name

    def setLength(self, length):
        self.length = length

    def __str__(self):
        return f"name={self.name}, continent={self.continent}, length={self.length}"


rivers: list[RIVER] = []


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def type_input(prompt, expected_type):
    while True:
        n = input(prompt)
        try:
            n = expected_type(n)
            return n
        except ValueError:
            print(f"Unexpected input \"{n}\", expecting {expected_type.__name__}")


def inputName():
    return input("Name = ")


def inputLength():
    return type_input("Length = ", int)


def inputContinent():
    return input("Continent = ")


def inputRiver():
    return inputName(), inputContinent(), inputLength()


def outputRivers():
    global rivers
    for i, r in enumerate(rivers):
        print(f"{i}. {r}")


while True:
    cls()
    outputRivers()
    print()
    print("1. Add element")
    print("2. Edit name")
    print("3. Edit length")
    try:
        ch = int(input("> "))
    except KeyboardInterrupt:
        exit()
    except:
        continue

    if ch == 1:
        rivers.append(RIVER(*inputRiver()))

    if ch == 2:
        ind = type_input("index = ", int)
        rivers[ind].setName(inputName())

    if ch == 3:
        ind = type_input("index = ", int)
        rivers[ind].setLength(inputLength())
