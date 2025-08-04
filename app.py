from flask import Flask, render_template, request
from scraper import fetch_case_details
from database import log_query

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    # Fetch from scraper logic
    result = fetch_case_details(case_type, case_number, filing_year)

    # Save to database
    log_query(case_type, case_number, filing_year, result)

    return render_template('result.html', data=result)

if __name__ == '__main__':
    app.run(debug=True)
