from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Ciao, mondo! Questo è il mio server Flask!</h1>"

@app.route('/saluto/<nome>')
def saluto(nome):
    return jsonify({'messaggio':f'ciao, {nome}'})

if __name__ == '__main__':
    app.run(debug=True)
