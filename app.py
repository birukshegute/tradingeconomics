from flask import Flask, render_template
from dotenv import load_dotenv
import os
import requests

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_BASE_URL = 'https://api.tradingeconomics.com'

def fetch_economic_data(country, indicators):
    try:
        response = requests.get(
            f"{API_BASE_URL}/country/{country}",
            params={'c': API_KEY, 'f': 'json'}
        )
        response.raise_for_status()
        data = response.json()

        extracted_data = {}
        for indicator in indicators:
            for item in data:
                if 'category' in item and item['category'].lower() == indicator.lower():
                    extracted_data[indicator] = item.get('value', 'N/A')
                    break
                elif 'indicator' in item and item['indicator'].lower() == indicator.lower():
                    extracted_data[indicator] = item.get('value', 'N/A')
                    break
        print(f"Extracted data for {country}: {extracted_data}")
        return extracted_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {}

@app.route('/')
def index():
    indicators = [
        'Consumer Spending',
        'Inflation Rate MOM',
        'Military Expenditure',
        'Long Term Unemployment Rate',
        'Retirement Age Men'
    ]

    mexico_data = fetch_economic_data('mexico', indicators)
    sweden_data = fetch_economic_data('sweden', indicators)

    return render_template('index.html', mexico_data=mexico_data, sweden_data=sweden_data)

if __name__ == '__main__':
    app.run(debug=True)
