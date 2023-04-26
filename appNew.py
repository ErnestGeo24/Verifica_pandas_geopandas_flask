from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
df = pd.read_excel("https://github.com/PolisenoRiccardo/perilPopolo/blob/main/milano_housing_02_2_23.xlsx?raw=true", sheet_name='Sheet1')

@app.route('/')
def form():
    return render_template('home.html')

@app.route('/quartiere')
def form():
    quartiere = re.match(request.form['quartiere'])
    df[df['neighborhood'] == quartiere].sort_values(by = 'date')
    return render_template('quartiere.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=32245, debug=True)