import math
import os


class ProgressBar:

    def __init__(self, numberOfSteps):
        self.amountFull = 0
        self.empty = " "
        self.third = "-"
        self.twoThird = "="
        self.full = "#"
        self.length = 20
        self.increment = math.ceil((self.length * 3)/numberOfSteps)
        self.full = self.length * 3
        self.progressBar = ["["]
        for i in range(1, self.length):
            self.progressBar.append(self.empty)
        self.progressBar.append("]")
        self.hasBeenPrinted = False

    def incrementBar(self):
        self.amountFull += self.increment

    def displayBar(self):
        if (not self.hasBeenPrinted):
            self.clearBar()
        self.hasBeenPrinted = True
        for i in range(1, self.amountFull//3):
            self.progressBar[i] = self.full
            if (i == self.amountFull//3):
                self.progressBar[i+1] = self.empty if self.amountFull % 3 == 0 else self.third if self.amountFull % 3 == 1 else self.twoThird
        for i in self.progressBar:
            print(i, end="")

    def clearBar(self):
        os.system('cls')
