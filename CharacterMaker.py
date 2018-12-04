import unittest
import random

class Character:
    str = 0
    dex = 0
    con = 0
    int = 0
    wis = 0
    cha = 0

    def __init__(self):
        self.str = self.generateAttribute(3, 6)

    def generateAttribute(self, hi, low):
        return (random.randint(hi, low) + random.randint(hi, low) + random.randint(hi, low))

newCharacter = Character()
print(newCharacter.str)

if __name__ == '__main__':
    unittest.main()