from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/soma', methods=['GET'])
def soma():
    try:
        a = float(request.args.get('a',0))
        a = float(request.args.get('b',0))
        resultado = a + b
        return jsonify({'resultado': resultado})
    except ValueError:
        return jsonify({'erro': 'Parâmetro inválido'}), 400

if __name__ == '__main__':
    app.run(debug=True)