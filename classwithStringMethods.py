class StringClass:
    def __init__(self,inputString):
        self.inputString=inputString

    def getString(self):
        self.inputString=input()
    def printString( self ):
        print(self.inputString.upper())

objStringClass= StringClass('baki')
objStringClass.getString()
objStringClass.printString()