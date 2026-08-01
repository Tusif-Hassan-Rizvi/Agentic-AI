class A:
    def show(self):
        print("in A Show")


class B(A):        
    def show(self):
        print("in B show")
        super().show()


obj1=B()
obj1.show()