from flask import Flask, request, jsonify, render_template
import time
from src.ideityfier import ideityfier as model
from src.helper import get_arg, is_url_image

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

@app.route('/predict', methods = ['GET', 'POST'])
def predict():
	if request.method == 'GET':
		return render_template('input.html')

	if request.method == 'POST':
		url = request.form['url']
		if url == '':
			return 'Empty URL!'

		elif is_url_image(url):		
			prediction = model.predict(url)
			return render_template('input.html',prediction = prediction, source = url)
			# return jsonify(prediction)

		else:
			return "invalid url"

if __name__ == '__main__':
	app.run(debug=True)