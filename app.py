from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/account', methods=['POST'])
def account_logic():
    data = request.json
    balance = float(data.get('balance', 0))
    # Rule: 1:500 leverage if balance >= 10,000, else Unlimited
    leverage = "1:500" if balance >= 10000 else "1:Unlimited"
    return jsonify({"leverage": leverage})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
