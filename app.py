from flask import Flask
app = Flask(__name__)
@app.route('/hello')
def sayHello():
    return "Hello World"

app.run(debug=True)