class A:
    def f1(self):
        print("f1 works")


    def f2(self):   
        print("f2 works")


    def show(self):    
        print("in show")


class B(A): #single level inheritence 
    def f3(self):
        print("f3 works")


    def f4(self):   
        print("f4 works")


    def show(self):    
            print("in b show")    


class C(B): #multi level inhertence 
    def f5(self):
        print("f5 works")

    def show(self):    
            print("in C show")    


class D(C, B, A): #multiple level inhertence 
    def f6(self):
        print("f6 works")

    def show(self):    
                print("in D show")        


obj1=D()

obj1.show()


B.show(obj1)
