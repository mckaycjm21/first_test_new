
#Currency List Endpoint
#https:#marketdata.tradermade.com/api/v1/live_currencies_list?api_key=UxO-7n8djCmq0KLW2A8s

#Crypto Pairs
#https:#marketdata.tradermade.com/api/v1/live_crypto_list?api_key=UxO-7n8djCmq0KLW2A8s

#Exchange rate example
# live endpoint
#https:#marketdata.tradermade.com/api/v1/live?currency=EURGBP,GBPJPY&api_key=UxO-7n8djCmq0KLW2A8s

# historical
#https:#marketdata.tradermade.com/api/v1/historical?date=2019-10-10&api_key=UxO-7n8djCmq0KLW2A8s

# tick_historical
#https:#marketdata.tradermade.com#api/v1/tick_historical/GBPUSD/2023-12-08 08:30/2023-12-08 09:00?format=json&api_key=UxO-7n8djCmq0KLW2A8s

# tick_historical_sample
#https:#marketdata.tradermade.com#api/v1/tick_historical_sample/GBPUSD/2023-12-08 08:30/2023-12-08 09:00?format=json&api_key=UxO-7n8djCmq0KLW2A8s

# minute_historical
#https:#marketdata.tradermade.com/api/v1/minute_historical?currency=EURUSD&date_time=2019-10-09-13:24&api_key=UxO-7n8djCmq0KLW2A8s

# hour_historical
#https:#marketdata.tradermade.com/api/v1/hour_historical?currency=EURUSD&date_time=2019-10-10-13:00&api_key=UxO-7n8djCmq0KLW2A8s

# convert
#https:#marketdata.tradermade.com/api/v1/convert?api_key=UxO-7n8djCmq0KLW2A8s&from=EUR&to=GBP&amount=1000

# timeseries
#https:#marketdata.tradermade.com/api/v1/timeseries?start_date=2015-01-01&end_date=2015-05-01&api_key=UxO-7n8djCmq0KLW2A8s

# pandasDF
#https:#marketdata.tradermade.com/api/v1/pandasDF?currency=EURUSD&start_date=2015-01-01&end_date=2015-05-01&api_key=UxO-7n8djCmq0KLW2A8s

#Live Rates
#https://marketdata.tradermade.com/api/v1/live?currency=EURUSD,GBPUSD,UK100&api_key=UxO-7n8djCmq0KLW2A8s

from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddSnackForm, NewEmployeeForm
import requests

RESPONSES_KEY = "responses"

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['DEBUG_TB_ENABLED'] = True

debug = DebugToolbarExtension(app)

@app.route("/")
def conversion_start():
    """basic page to start conversion"""

    return render_template("index.html")

@app.route("/answer", methods=["POST"])
def display_results():
    """Display results"""
    start = request.form['start_cur'].upper()
    end = request.form['end_cur'].upper()
    base_amt = request.form['base_amt']
    url = f"https://marketdata.tradermade.com/api/v1/convert?api_key=UxO-7n8djCmq0KLW2A8s&from={start}&to={end}&amount={base_amt}"

    response = requests.get(url)
    status_code = response.status_code
    if(status_code == 200):
        test = response.json()
        total = round(float(test['total']), 2)
        base = test['base_currency']
        quote = test['quote_currency']
        return render_template("answer.html", start = start, base=base, quote=quote,base_amt=base_amt, total=total, test=test)
    elif(status_code == 400):
        test = response.json()
        return render_template("error.html", test = test, status_code=status_code)
    

@app.route("/snack/new", methods=["GET", "POST"])
def add_snack():
    
    form = AddSnackForm()

    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        flash(f"Created new snack: name is {name}, price is ${price}")
        return redirect('/snack')
    else:
        return render_template("add_snack_form.html", form=form)
    

@app.route("/snack")
def base_snack():
    return render_template("home.html")

@app.route("/employees/new", methods=["GET", "POST"])
def add_employee():
    form = NewEmployeeForm()
    if form.validate_on_submit():
        return render_template("add_employees.html", form=form)