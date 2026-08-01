from abc import ABC, abstractmethod

# class A(ABC):

#     @abstractmethod 
#     def show(self):
#         pass


# obj1=A()        
# obj1.show()


class PaymentGateway(ABC):
    @abstractmethod
    def pay(self):
     pass


class TusPay(PaymentGateway):
    def pay(self):
        print("Paying using tuspay")

class Razorpay(PaymentGateway):
    def pay(self):
        print("Paying using razorpay...")


class Purchase:
    def __init__(self, gateway):
        self.gateway=gateway
   
    def checkout(self):
        print("checking out...")
        self.gateway.pay()
        
gateway1=Razorpay()        
gateway2=TusPay()        
purchase=Purchase(gateway2)


purchase.checkout()