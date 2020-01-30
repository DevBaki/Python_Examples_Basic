class Generator:
    def __init__(self, n):
        self.n = n

    def oddNumbers(self):
        oddness = []
        for i in range(0, self.n+1):
            if i % 7 == 0:
                oddness.append(i)
        return oddness


print("Enter number")
num=input()
g = Generator(int(num))
print(g.oddNumbers())
