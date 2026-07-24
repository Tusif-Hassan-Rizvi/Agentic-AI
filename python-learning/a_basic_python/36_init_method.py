# dunder method init 
# dunder=double underscore __ method called dunder 




class comptuer:
    def __init__(self, cpu, ram, ssd):
        self.cpu=cpu
        self.ram=ram
        self.ssd=ssd

    def config(self):
        print("System bahut tagda hai bro...trust me.", self.cpu, self.ram, self.ssd)


comp1=comptuer("i5", "8GB", "1TB")
comp2=comptuer("i7", "16GB", "1TB")


comp1.config()
comp2.config()
