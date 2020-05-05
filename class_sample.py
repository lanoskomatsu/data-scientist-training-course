class PrintClass:
    def print_me(self):
        print(self.x, self.y)

p1 = PrintClass()

p1.x = 10
p1.y = 100
p1.z = 1000

p1.print_me()
