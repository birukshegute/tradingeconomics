from flask import Flask, render_template
from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_BASE_URL = 'https://api.tradingeconomics.com'

app = Flask(__name__)
def fetch_economic_data(country, categories):
    try:
        response = requests.get(
            f"{API_BASE_URL}/country/{country}",
            params={'c': API_KEY, 'f': 'json'}
        )
        response.raise_for_status()
        data = response.json()

        
        # Initialize a dictionary to store the extracted data
        extracted_data = {}

        for category in categories:
            for item in data:
                if item.get('Category') == category:
                    extracted_data[category] = {
                        'LatestValue': item.get('LatestValue', 'N/A'),
                        'Unit': item.get('Unit', ''),
                        'Date': item.get('LatestValueDate', '')
                    }
                    break

        print(f"Extracted data for {country}: {extracted_data}")
        return extracted_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

@app.route('/')
def index():
    categories = [
        'Consumer Spending',
        'Core Inflation Rate',
        'Employment Rate',
        'Balance of Trade',
        'Gold Reserves',
        'Corruption Rank',
        'GDP',
        'GDP Growth Rate'
    ]
        
        

    mexico_data = fetch_economic_data('mexico', categories)
    sweden_data = fetch_economic_data('sweden', categories)

    return render_template('index.html', mexico_data=mexico_data, sweden_data=sweden_data)
    