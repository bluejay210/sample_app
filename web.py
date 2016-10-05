from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index_about')
def index_about():
    return render_template('index_about.html')

app.run(debug=True)