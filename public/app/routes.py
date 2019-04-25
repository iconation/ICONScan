from flask import render_template
from app import app
from app import constants

from app.models.db import IconScanDb

from app.models import transactions_count_per_day as model_transactions_count_per_day
from app.views import transactions_count_per_day as view_transactions_count_per_day

from app.models import transactions_count_per_day_big_icx_transfer as model_transactions_count_per_day_big_icx_transfer
from app.views import transactions_count_per_day_big_icx_transfer as view_transactions_count_per_day_big_icx_transfer

from app.models import all_transactions as model_all_transactions
from app.views import transaction_processor as view_transaction_processor

import json

def balances_more_than (accounts, date, args):
    threshold = args[0]
    return len (filter (lambda account: account[1].balance >= threshold, accounts.iteritems()))

def average_holding (accounts, date, args):
    circulating_supply = 473406688
    not_empty = filter (lambda account: account[1].balance > 0, accounts.iteritems())
    return circulating_supply / len(not_empty)

from datetime import timedelta
def time_holding (accounts, date, args):
    days = args[0]
    holders = filter (lambda account: (account[1].withdraw + timedelta(days=days)) < date and account[1].balance > 0, accounts.iteritems())
    return len(holders)

def active_wallets (accounts, date, args):
    hours = args[0]
    holders = filter (lambda account: (account[1].withdraw + timedelta(hours=hours)) > date and account[1].balance > 0, accounts.iteritems())
    return len(holders)

@app.route('/')
@app.route('/index')
def index():
    db = IconScanDb ("app/conf/credentials.json")
    db.connect_to_mysql()

    alltx = model_all_transactions.process (db)
    txcount = view_transactions_count_per_day.process (model_transactions_count_per_day.process (db))
    txcountbig = view_transactions_count_per_day_big_icx_transfer.process (model_transactions_count_per_day_big_icx_transfer.process (db))
    holders_0 = view_transaction_processor.process (alltx, balances_more_than, 0)
    holders_20k = view_transaction_processor.process (alltx, balances_more_than, 20000)
    holders_100k = view_transaction_processor.process (alltx, balances_more_than, 100000)
    holders_1m = view_transaction_processor.process (alltx, balances_more_than, 1000000)
    avg_holding = view_transaction_processor.process (alltx, average_holding)
    holding_3months = view_transaction_processor.process (alltx, time_holding, 3*30)
    active = view_transaction_processor.process (alltx, active_wallets, 24)

    return render_template (
        'index.jinja', 
        constants=constants, 
        txcount=json.dumps(txcount),
        txcountbig=json.dumps(txcountbig),
        holders_0=json.dumps(holders_0),
        holders_20k=json.dumps(holders_20k),
        holders_100k=json.dumps(holders_100k),
        holders_1m=json.dumps(holders_1m),
        avg_holding=json.dumps(avg_holding),
        holding_3months=json.dumps(holding_3months),
        active=json.dumps(active)
    )
