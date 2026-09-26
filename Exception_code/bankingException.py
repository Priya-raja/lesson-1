class BankingError(Exception):
    pass

class InsufficientFundError(BankingError):
    pass

class UnauthorizedError(BankingError):
    pass

class BankConnectionError(BankingError):
    pass

class BankA:
    
    @staticmethod
    def withdraw(amount):
        if amount > 10000:
            raise InsufficientFundError("Funds are less in bank")
        return f"Withdrew {amount} from Bank A"
        
class BankB:

    @staticmethod
    def withdraw(amount):
        if not amount.is_integer():
            raise UnauthorizedError("Unauthorized detected in bank B")
        return f"Withdre {amount} from Bank b"        

def perform_transaction(bank, amount):
    try:
        if bank == "BankA":
            return BankA.withdraw(amount)
        elif bank == "BankB":
            return BankB.withdraw(amount)
        else:
            raise ValueError("Unknown bank")
    except InsufficientFundError:
            return "Transaction failed due to insufficient funds!"
    except UnauthorizedError:
           return "Transaction failed due to unauthorized access!"
    except BankConnectionError:
           return "Transaction failed due to connection issues with the bank!"
    except BankingError:
           return "General banking error occurred!"
    except Exception as e:
           return f"An unexpected error occurred: {e}"
print(perform_transaction("BankA", 15000))
print(perform_transaction("BankB", 1500.5))
print(perform_transaction("BankC", 1000))    