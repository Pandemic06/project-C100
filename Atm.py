class Atm():
    def __init__(self,cardNumber,pinNumber,name,bank):
        self.cardNumber=cardNumber 
        self.pinNumber=pinNumber
        self.name=name 
        self.bank=bank

    def cashWithdrawal(self):
        money=input("Enter amount to be withdrawn")
        pin=float(input("Please enter you PIN")) 
        if pin==self.pinNumber:
            print("Please collect the amount")
        else: print("The PIN entered is incorrect")      

card1=Atm(368145,3415,"Ivan","Moscow Cooperative")
card2=Atm(123456,1234,"Richtofen","Berlin Cooperative")
card1.cashWithdrawal()