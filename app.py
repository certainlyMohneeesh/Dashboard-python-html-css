from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/analytics')
def get_analytics():
    data = {
        'patients': [
            {'month': 'Jan', 'count': 65, 'revenue': 8400},
            {'month': 'Feb', 'count': 78, 'revenue': 9200},
            {'month': 'Mar', 'count': 90, 'revenue': 10600},
            {'month': 'Apr', 'count': 81, 'revenue': 9800},
            {'month': 'May', 'count': 95, 'revenue': 11200},
            {'month': 'Jun', 'count': 110, 'revenue': 13400}
        ]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
