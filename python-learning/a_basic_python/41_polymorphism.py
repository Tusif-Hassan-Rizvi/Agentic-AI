class Laptop:
    def build(self):
        print("print laptop")


class Desktop:
    def build(self):
        print("desktop  build")


class Tablets:
    def open_pdf(self):        
        print("pdf openning...")

class Alien:
    def code(self, machine:Laptop):
        print("Alien building")
        machine.build()


acer=Laptop()
beast=Desktop()

tausif=Alien()
tab=Tablets()

# tausif.code(beast)
# tausif.code(acer)
tausif.code(tab)


# duckTyping 