from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}!'
    return render_template('form.html')

@app.route("/table")
def table():
    prices = {
        'Phone': 12000,
        'TV': 14000,
        'Car': 50000
    }

    return render_template('table.html', prices = prices)

if __name__ == "__main__":
    app.run(debug=True)