from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/health')
def health():
    return "okkkkkkk!!!!!!!!!"


def test_index():
    assert True


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
