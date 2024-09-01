from flask import Flask, render_template
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('API_KEY')

def fetch_data(country, indicator):
    url = f'https://api.tradingeconomics.com/historical/country/{country}/indicator/{indicator}?c={API_KEY}'
    response = requests.get(url)
    return response.json()

@app.route('/')
def index():
    gdp_egypt = fetch_data('egypt', 'gdp')
    gdp_ethiopia = fetch_data('ethiopia', 'gdp')

    return render_template('index.html', gdp_egypt=gdp_egypt, gdp_ethiopia=gdp_ethiopia)

if __name__ == '__main__':
    app.run(debug=True)