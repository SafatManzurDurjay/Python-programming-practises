class practise:
    def move(self):
        print("move")
    def draw(self):
        print("draw")

practise1 = practise()
practise1.x = 10
print(practise1.x)

practise2 = practise
practise2.x = 20
print(practise2.x)

practise1.draw()