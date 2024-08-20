from flask import Flask
from my_blueprint import my_blueprint

app = Flask(__name__)
app.register_blueprint(my_blueprint, url_prefix='/my_blueprint')

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)