from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, owner, bal=0):
        self._owner = owner
        self.__balance = bal
        self._transactions = []

    
    def get_balance(self):
        return self.__balance
    
    # internal method to update balance safely.    
    def _update_balance(self, amt):
        self.__balance += amt

    
    # not an abstract method because the implementation is the same for all child classes    
    def deposit(self, amt):
        if amt <= 0:
            print("Invalid deposit amount")
            return
        
        self._update_balance(amt)
        self._transactions.append(f"Deposit: {amt}")
        print(f"deposit successful: deposited {amt}/-")
    
    
    # abstract method bcz all accounts must implement it, and the implementation varies for different child classes.
    @abstractmethod
    def withdraw(amt):
        pass

    @abstractmethod
    def apply_interest():
        pass


    # shows transaction history. Implement later!
    def show_transactions(self):
        for transaction in self._transactions:
            print(transaction)
    
    


class SavingsAccount(Account):
    MIN_BALANCE = 5000
    INTEREST_RATE = 0.04        # 4%

    def withdraw(self, amt):
        if amt <= 0:
            print("Invalid withdraw amount")
            return False

        if (self.get_balance() - amt) > self.MIN_BALANCE:
            self._update_balance(-amt)
            self._transactions.append(f"Withdrawl: {amt}")
            print(f"withdrew {amt}/- successfully")
            return True

        else:
            print("Insufficient funds! Minimum balance must be maintained")
            return False
    

    def apply_interest(self):
        self._update_balance(self.get_balance() * self.INTEREST_RATE)


class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 1000

    def withdraw(self, amt):
        if amt <= 0:
            print("Invalid withdraw amount")
            return False

        if (self.get_balance() + self.OVERDRAFT_LIMIT) > amt:
            self._update_balance(-amt)
            print(f"withdrew {amt}/- successfully")
            self._transactions.append(f"Withdrawl: {amt}")
            return True

        else:
            print("cannot withdraw: overdraft limit exceeded")
            return False
        
    def apply_interest(self):
        pass    # no interest in current account



class PremiumSavingsAccount(SavingsAccount):
    MINIMUM_BALANCE = 2_000
    INTEREST_RATE = 0.06    # 6%
    BONUS = 100

    def apply_interest(self):
        self._update_balance(self.get_balance() * self.INTEREST_RATE + self.BONUS)
        