from flask import render_template
from app import app
from app import constants

from app.models.db import IconScanDb
from app.models.txcount_per_day import txcount as txcount_model
from app.views.txcount_per_day import txcount as txcount_view

import json

@app.route('/')
@app.route('/index')
def index():
    db = IconScanDb ("app/conf/credentials.json")
    db.connect_to_mysql()
    txcount = txcount_view (txcount_model (db))
    print(txcount)
    return render_template (
        'index.jinja', 
        constants=constants, 
        txcount=json.dumps(txcount)
    )
