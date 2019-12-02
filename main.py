from flask import Flask, request, jsonify
from web_scraper import get_html

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    data = request.args.get('url')
    tag = request.args.get('tag', 'meta')
    result =  get_html(data, tag)
    return jsonify(result)

if __name__ == '__main__':
	app.run(debug=True)
