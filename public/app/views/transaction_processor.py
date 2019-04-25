from datetime import datetime
import collections

class Account:
    def __init__ (self, balance, withdraw):
        self.balance = balance
        self.withdraw = withdraw

def process (model, processor, *args):

    result = []
    accounts = {}

    # Mainnet Genesis
    last_date = datetime.fromtimestamp(0)
    accounts["hx54f7853dc6481b670caf69c5a27c7c8fe5be8269"] = Account (800460000, last_date)

    for _, timestamp, txfrom, txto, txamount, itxfrom, itxto, itxamount in model:

        timestamp /= 1000000
        date = datetime.fromtimestamp(timestamp)

        if last_date.date() != date.date():
            result.append ((last_date.isoformat(), processor (accounts, date, args)))
            last_date = date

        if txfrom:
            accounts[txfrom].balance -= txamount
            accounts[txfrom].withdraw = date
            if not txto in accounts:
                accounts[txto] = Account (txamount, date)
            else:
                accounts[txto].balance += txamount
        if itxfrom:
            accounts[itxfrom].balance -= itxamount
            accounts[itxfrom].withdraw = date
            if not itxto in accounts:
                accounts[itxto] = Account (itxamount, date)
            else:
                accounts[itxto].balance += itxamount

    return result[1:]