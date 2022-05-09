import sys, random

class Converttask:

    __systems__ = ["bin", "dec", "hex"]

    def __init__(self, s, d):
        if s in self.__systems__ and d in self.__systems__:
            self.__source__ = s
            self.__destignation__ = d
        else:
            print("Wrong number!")
            sys.exit(1)
        self.__number__ = random.randint(1,128)
        self.__numberdec__ = str(self.__number__)
        self.__numberbin__ = str(bin(self.__number__))[2:]
        self.__numberhex__ = str(hex(self.__number__))[2:]

    def getNumberDec(self):
        return self.__numberdec__

    def getNumberBin(self):
        return self.__numberbin__

    def getNumberHex(self):
        return self.__numberhex__

    def setInput(self,i):
        self.__input__=str(i).lower()

    def getInput(self):
        return self.__input__

    def testResult(self):
        if self.__destignation__ == "bin":
            return self.__numberbin__ == self.__input__
        elif self.__destignation__ == "dec":
            return self.__numberdec__ == self.__input__
        elif self.__destignation__ == "hex":
            return self.__numberhex__ == self.__input__
            
    

if __name__ == "__main__":

    t1 = Converttask("bin","dec")
    print(t1.getNumberBin(),t1.getNumberDec())
    eingabe = input("Bin -> Dec: ")
    t1.setInput(eingabe)
    print(t1.getInput(),t1.testResult())

    t2 = Converttask("bin","hex")
    print(t2.getNumberBin(),t2.getNumberHex())
    eingabe = input("Bin -> Hex: ")
    t2.setInput(eingabe)
    print(t2.getInput(),t2.testResult())

    t3 = Converttask("dec","bin")
    print(t3.getNumberDec(),t3.getNumberBin())
    eingabe = input("Dec -> Bin: ")
    t3.setInput(eingabe)
    print(t3.getInput(),t3.testResult())

    t4 = Converttask("dec","hex")
    print(t4.getNumberDec(),t4.getNumberHex())
    eingabe = input("Dec -> Hex: ")
    t4.setInput(eingabe)
    print(t4.getInput(),t4.testResult())

    t5 = Converttask("hex","bin")
    print(t5.getNumberHex(),t5.getNumberBin())
    eingabe = input("Hex -> Bin: ")
    t5.setInput(eingabe)
    print(t5.getInput(),t5.testResult())

    t6 = Converttask("a","b")