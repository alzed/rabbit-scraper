from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data = request.form.get('url')
    tag = request.form.get('tag')
    return (data, tag)

if __name__ == '__main__':
	app.run(debug=True)
