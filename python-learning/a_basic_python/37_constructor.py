class Abc:

    def __new__(cls):
        print("this is constructor")
        return super(Abc, cls).__new__(cls)

    def __init__(self):
        print("it's called")

    def show(self):    
        print("in show")



obj1=Abc()
obj1.show()


obj2=Abc.__new__(Abc)
obj2.__init__()
obj2.show()