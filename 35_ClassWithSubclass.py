class Indian(object):

    @staticmethod
    def printNationality():
        print("I am an Indian")


class Vizagian(Indian):
    pass


indian = Indian()
indian.printNationality()
vizian = Vizagian()
vizian.printNationality()
