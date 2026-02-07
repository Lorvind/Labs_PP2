class StringHandler:
    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())

handler = StringHandler()
handler.getString()
handler.printString()