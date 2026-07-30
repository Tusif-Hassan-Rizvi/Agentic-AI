# dunder method init 
# dunder=double underscore __ method called dunder 




class comptuer:

    brand="HP" #class variable 

    def __init__(self, cpu, ram, ssd):
        self.cpu=cpu  #instance variable
        self.ram=ram
        self.ssd=ssd

    def config(self):  #instance method
        print("System bahut tagda hai bro...trust me.", self.cpu, self.ram, self.ssd)

    @classmethod
    def info(cls):    #class method
        return cls.brand

    @staticmethod    #static method is like it is here but nothing to do with class. it's like a utility class
    def gb_to_bytes(gb):
        return gb * (1024 ** 3)



comp1=comptuer("i5", "8GB", "1TB")
comp2=comptuer("i7", "16GB", "1TB")


comp1.config()
comp2.config()


# class method 
print(comptuer.brand)
print(comptuer.info())



# static method 

print(comptuer.gb_to_bytes(16))