from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    return f"Form submitted with data: {data}"

if __name__ == '__main__':
    app.run(debug=True)