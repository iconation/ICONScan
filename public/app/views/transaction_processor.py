from datetime import datetime, date
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
    last_date = date (last_date.year, last_date.month, last_date.day)
    accounts["hx54f7853dc6481b670caf69c5a27c7c8fe5be8269"] = Account (800460000, last_date)

    for _, dt, txfrom, txto, txamount, itxfrom, itxto, itxamount in model:

        # date = datetime.fromtimestamp (timestamp)
        # date = datetime.strptime (timestamp, '%Y-%m-%d').date()
        dt = date (dt.year, dt.month, dt.day)

        if last_date != dt:
            result.append ((last_date.isoformat(), processor (accounts, dt, args)))
            last_date = dt

        if txfrom:
            accounts[txfrom].balance -= txamount
            accounts[txfrom].withdraw = dt
            if not txto in accounts:
                accounts[txto] = Account (txamount, dt)
            else:
                accounts[txto].balance += txamount
        if itxfrom:
            accounts[itxfrom].balance -= itxamount
            accounts[itxfrom].withdraw = dt
            if not itxto in accounts:
                accounts[itxto] = Account (itxamount, dt)
            else:
                accounts[itxto].balance += itxamount

    return result[1:]