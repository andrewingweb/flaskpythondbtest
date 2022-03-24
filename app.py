from flask import Flask, render_template, request
import pandas as pd



app = Flask(__name__)

dataset = pd.read_csv('DBNetz.csv', sep=';', header=None)

data = dataset[[1]]
data1 = dataset[[2]]
data2 = dataset[[4]]
data3 = dataset[[10]]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/btrs')
def searchByBcode():
    name = request.args.get('name').upper()
    btrs = (data.loc[data[1] == name])
    lname = (data1.loc[data[1] == name])
    type1 = (data2.loc[data[1] == name])
    regio = (data3.loc[data[1] == name])
    
    return render_template('btrs.html', btrs=btrs, lname=lname, type1=type1, regio=regio)

if __name__ == "__main__":
    app.run()

