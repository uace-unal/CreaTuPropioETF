from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # process form data here
        tickers = request.form.get('tickers').split(',')
        coefficients = [float(coef) for coef in request.form.get('coefficients').split(',')]
        data = fetch_data(tickers)
        portfolio, total_return = calculate_total_return(data, coefficients)
        plot_url = plot_data(data, portfolio)
        return render_template('index.html', plot_url=plot_url, total_return=total_return)
    return render_template('index.html')

# ... include your other functions here, modifying them as needed ...

def plot_data(data, portfolio):
    plt.figure(figsize=(12, 6))
    # ... plotting code ...
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    return 'data:image/png;base64,{}'.format(plot_url)

if __name__ == '__main__':
    app.run(debug=True)
