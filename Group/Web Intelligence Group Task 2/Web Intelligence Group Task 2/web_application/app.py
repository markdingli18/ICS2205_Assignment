import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/category_data')
def category_data():
    with open('category_data.json', 'r') as f:
        data = json.load(f)
    return render_template('category_data.html', data=data)

@app.route('/cluster_data')
def cluster_data():
    with open('cluster_data.json', 'r') as f:
        data = json.load(f)
    return render_template('cluster_data.html', data=data)

if __name__ == '__main__':
    app.run()