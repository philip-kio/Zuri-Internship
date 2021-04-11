class Budget:


    def __init__(self,category:str,deposits:float):
        self.category = category
        self.deposits =deposits
        self.balance = 0.00


    def check_balance(self):
        self.balance += self.deposits
        return 'Your  %s category balance is #%d' %(self.category, self.deposits)


    def withdrawal(self,ammount:float):
        self.ammount = ammount
        if (self.ammount <= self.balance):
            self.balance -= self.ammount
            return 'your withdrawal of # %d is successful.\nYour new balance is %d.' %(self.ammount, self.balance)
        else:
            return 'Insuficient ammount in your %s. Please deposit into your %s account to enable withdrawal.'%(self.category,self.category)


    def transfer(self,category:str, ammount:float):
        self.ammount = ammount
        self.newCategory = category
        if (self.ammount <= self.balance):
            self.balance -= self.ammount
            return 'Transfer was successful.\n #%d was transfered to %s from %s.\nYour new balance for %s category is #%d.' %(self.ammount, self.newCategory, self.category,self.category, self.balance)
        else:
            return 'Trasaction failed insufficient funds.'









Food = Budget('Food', 500000)



print(Food.check_balance(), Food.withdrawal(800000),Food.balance)

Clothing = Food.transfer('clothing', 10000)

print(Clothing)