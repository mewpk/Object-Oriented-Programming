class ATM :
    def __init__(self,id, cash_1, cash_2,cash_3 , bank):
        self.__id  = id
        self.__amount = cash_1*1000 + cash_2*500 + cash_3*100
        self.__bank = bank
        self.__cash_1 = cash_1
        self.__cash_2 = cash_2
        self.__cash_3 = cash_3
    @property
    def amount(self):
        return self.__amount
    @property
    def bank(self):
        return self.__bank
    @property
    def cash_1(self):
        return self.__cash_1
    @property
    def cash_2(self):
        return self.__cash_2
    @property
    def cash_3(self):
        return self.__cash_3
    @cash_1.setter
    def cash_1(self, value):
        self.__cash_1 = value
        return self.__cash_1
    @cash_2.setter
    def cash_2(self, value):
        self.__cash_2 = value
        return self.__cash_2
    @cash_3.setter
    def cash_3(self, value):
        self.__cash_3  = value
        return self.__cash_3
    @amount.setter
    def amount(self, value):
        self.__amount = value
        return self.__amount
    def insert_card(self,card):
        pin = input("Enter your PIN :")
        if self.bank.verify_card(card,pin) :
            print("Success")
            self.select_transaction(card)
        else : print("Account Incorrect")
    def select_transaction(self,card):
        print("Select transaction: ")
        print("1. Withdraw Cash")
        print("2. Deposite Cash")
        print("3.Transfer Money")
        select = input("transaction (1,2,3) :")
        if select == "1" :
            self.withdraw_cash(card)
        elif select == "2" :
            self.deposit_cash(card)
        elif select == "3" :
            self.transfer_money(card)
        
        print(f"------------------------------------")
        print(f"Amount ATM : {self.amount}")
        print(f"Cash 1000 : {self.cash_1}")
        print(f"Cash 500 : {self.cash_2}")
        print(f"Cash 100 : {self.cash_3}")

    def withdraw_cash(self,card):
        print(f"Available balance ATM: {self.amount}")
        cash_account = self.bank.CashAccountCollection.get_cash_account_by_id(card.account_id)
        print(f"Balance Account: {cash_account.amount}")
        withdraw = int(input("Enter amount to withdraw :"))
        temp_withdraw = withdraw
        if self.check_balance(withdraw) and cash_account.check_amount(withdraw) :
            cash_1 = 0
            cash_2 = 0
            cash_3 = 0
            while(True):
                if withdraw >= 1000:
                    if self.cash_1 >= 1 :
                        cash_1 += 1
                        self.cash_1 -= 1
                        withdraw -= 1000
                elif withdraw >= 500 :
                    if self.cash_2 >= 1 :
                        cash_2 += 1
                        self.cash_2 -= 1
                        withdraw -= 500
                elif withdraw >= 100 :
                    if self.cash_3 >= 1 :
                        cash_3 += 1
                        self.cash_3 -= 1
                        withdraw -= 100
                else : 
                    break
            print(f"1000 : {cash_1} , 500 : {cash_2} , 100 : {cash_3}")
            cash_account.history.append({"date" : "25/04/2023" , "options" :"withdraw", "Before" : cash_account.amount , "After" : cash_account.amount-temp_withdraw})
            print(f"Before withdraw money: {cash_account.amount}")
            cash_account.amount -= temp_withdraw
            print(f"after withdraw money: {cash_account.amount}")
            self.amount -= temp_withdraw
        else : 
            print("Not enough funds to withdraw")
            print(f"Balance ATM: {self.amount}")
            print(f"Balance Account: {cash_account.amount}")
    def deposit_cash(self,card):
        print(f"Available balance ATM: {self.amount}")
        cash_account = self.bank.CashAccountCollection.get_cash_account_by_id(card.account_id)
        print(f"Balance Account: {cash_account.amount}")
        deposit = int(input("Enter amount to deposit :"))
        cash_1 = int(input("Enter Cash 1000 : "))
        cash_2 = int(input("Enter Cash 500 : " ))
        cash_3 = int(input("Enter Cash 100 : " ))
        self.cash_1 += cash_1
        self.cash_2 += cash_2
        self.cash_3 += cash_3
        self.amount += deposit
        cash_account.history.append({"date" : "25/04/2023" , "options" :"deposit", "Before" : cash_account.amount , "After" : cash_account.amount+deposit})
        cash_account.amount += deposit
        print(f"Balance ATM: {self.amount}")
        print(f"Balance Account: {cash_account.amount}")
        

    def transfer_money(self,card):
        account_id = input("Enter transfer account number :")
        if self.bank.AccountCollection.get_account_by_id(account_id) :
            print(f"Available balance ATM: {self.amount}")
            cash_account = self.bank.CashAccountCollection.get_cash_account_by_id(card.account_id)
            print(f"Balance Account: {cash_account.amount}")
            transfer_account = self.bank.CashAccountCollection.get_cash_account_by_id(account_id)
            transfer = int(input("Enter amount to transfer :"))
            temp_transfer = transfer
            if self.check_balance(transfer) and cash_account.check_amount(transfer) :
                cash_account.history.append({"date" : "25/04/2023" , "options" :"transfer", "Before" : cash_account.amount , "After" : cash_account.amount-temp_transfer})
                print(f"Before transfer money: {cash_account.amount}")
                cash_account.amount -= temp_transfer
                print(f"after transfer money: {cash_account.amount}")
                transfer_account.amount += temp_transfer
            else : 
                print("Not enough funds to transfer")
                print(f"Balance ATM: {self.amount}")
                print(f"Balance Account: {cash_account.amount}")
        else : 
            print("Invalid Transfer account")
    def check_balance(self,withdraw):
        if withdraw <= self.amount :
            text = str(withdraw)
            if int(text[::-1][0]) == 0 and int(text[::-1][1]) == 0 :
                return True
            return False
        else :
            return False
class ATMCard : 
    def __init__(self, card_id , full_name , account_id , end_date ,bank) :
        self.__card_id = card_id
        self.__full_name = full_name
        self.__account_id = account_id
        self.__end_date = end_date
        self.__bank = bank
    @property
    def id(self):
        return self.__card_id
    @property
    def account_id(self):
        return self.__account_id
    @property
    def bank(self):
        return self.__bank
    def verify(self,pin) :
        return self.bank.verify(self.account_id,pin)
        

class ATMCardCollection:
    def __init__(self) -> None:
        self.__ATMCards = []

    @property
    def ATMCards(self):
        return self.__ATMCards

    def add_card(self, card):
        self.ATMCards.append(card)
    def get_card_by_id(self,card):
        try:
            for cards in self.ATMCards :
                if cards.id == card.id :
                    return cards
            return False
        except : 
            return False
    def verify_card(self,card,pin):
        Card =  self.get_card_by_id(card)
        return Card.verify(pin)
        

class Account :
    def __init__(self,full_name , account_id , passcode , bank):
        self.__full_name = full_name
        self.__account_id = account_id
        self.__passcode = passcode
    @property
    def id(self):
        return self.__account_id
    @property
    def passcode(self):
        return self.__passcode
    def passcode_verify(self,pin):
        if self.passcode == pin :
            return True
class AccountCollection:
    def __init__(self) -> None:
        self.__Accounts = []

    @property
    def Accounts(self):
        return self.__Accounts
    def get_account_by_id(self,id):
        try:
            for Accounts in self.Accounts :
                if Accounts.id == id :
                    return Accounts
            return False
        except : 
            return False
    def add_account(self, card):
        self.Accounts.append(card)
    def verify(self,account_id, pin):
        account = self.get_account_by_id(account_id)
        return account.passcode_verify(pin)


class Bank :
    def __init__(self,name,passcode):
        self.__name = name
        self.__passcode = passcode
        self.__ATMCardCollection = ATMCardCollection()
        self.__AccountCollection = AccountCollection()
        self.__CashAccountCollection = CashAccountCollection()
    @property
    def ATMCardCollection(self):
        return self.__ATMCardCollection
    @property
    def AccountCollection(self):
        return self.__AccountCollection
    @property
    def CashAccountCollection(self):
        return self.__CashAccountCollection

    def verify(self,account_id,pin):
        return self.AccountCollection.verify(account_id,pin)
    def verify_card(self,card,pin):
        return self.ATMCardCollection.verify_card(card,pin)
    def add_account(self,account):
        self.AccountCollection.add_account(account)
    def add_card(self,card):
        self.ATMCardCollection.add_card(card)
    def add_cash_account(self,account):
        self.CashAccountCollection.add_account(account)
    

class CashAccount :
    def __init__(self,account_id,amount,bank):
        self.__account_id = account_id
        self.__amount = amount
        self.history = []
    @property
    def id(self):
        return self.__account_id
    @property
    def amount(self):
        return self.__amount
    @property
    def history(self):
        return self.__history
    @history.setter
    def history(self,value):
        self.__history = value
        return self.__history
    @amount.setter
    def amount(self,value):
        self.__amount = value
        return self.__amount
    def check_amount(self,value):
        if value <= self.amount :
            return True
        else :
            return False
    
class CashAccountCollection :
    def __init__(self):
        self.__cash_accounts = []
    @property
    def cash_accounts(self):
        return self.__cash_accounts
    def get_cash_account_by_id(self,account_id):
        try:
            for accounts in self.cash_accounts :
                if accounts.id == account_id :
                    return accounts
            return False
        except : 
            return False
    def add_account(self,account):
        self.cash_accounts.append(account)
        return self.cash_accounts

oop_bank = Bank("OOP","1232")
atm_1 =  ATM("65010731",100,100,100,oop_bank)
mewpk_card =  ATMCard("65010731","Patsakorn Thong-un","65010731","25/07/2026",oop_bank)
mewpk_account  = Account("Patsakorn Thong-un","65010731","0731",oop_bank)
mewpk_cash_account = CashAccount("65010731",1000, oop_bank)

cat_card =  ATMCard("65010732","Cat Thong-un","65010732","25/07/2026",oop_bank)
cat_account  = Account("Cat Thong-un","65010732","0731",oop_bank)
cat_cash_account = CashAccount("65010732",1000, oop_bank)


oop_bank.add_card(mewpk_card)
oop_bank.add_account(mewpk_account)
oop_bank.add_cash_account(mewpk_cash_account)

oop_bank.add_card(cat_card)
oop_bank.add_account(cat_account)
oop_bank.add_cash_account(cat_cash_account)

while(True):
    input_xy = input("Please insert your card (Y/N) : ") 
    if input_xy == "y":
        atm_1.insert_card(mewpk_card)
    elif input_xy == "n" :
        break
print("------------Transaction---------------")
for transaction in oop_bank.CashAccountCollection.cash_accounts :
    print(transaction.id ,transaction.history)