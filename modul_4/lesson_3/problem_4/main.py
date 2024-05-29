from flask import Flask, request

app = Flask(__name__)


@app.route('/hello')
def hello():
    name = request.args.get('name',
                            'World')
    return f'Hello, {name}!'


if __name__ == '__main__':
    app.run(debug=True)
