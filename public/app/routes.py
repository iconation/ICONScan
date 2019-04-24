from flask import render_template
from app import app
from app import constants

from app.models.db import IconScanDb

from app.models import transactions_count_per_day as model_transactions_count_per_day
from app.views import transactions_count_per_day as view_transactions_count_per_day

from app.models import average_icx_daily_transfer as model_average_icx_daily_transfer
from app.views import average_icx_daily_transfer as view_average_icx_daily_transfer

import json

@app.route('/')
@app.route('/index')
def index():
    db = IconScanDb ("app/conf/credentials.json")
    db.connect_to_mysql()
    txcount = view_transactions_count_per_day.process (model_transactions_count_per_day.process (db))

    return render_template (
        'index.jinja', 
        constants=constants, 
        txcount=json.dumps(txcount)
    )
