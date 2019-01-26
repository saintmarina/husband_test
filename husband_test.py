from flask import Flask, request, make_response, url_for, render_template, redirect
import json
app = Flask(__name__)

@app.route('/')
def main_page():
	return render_template('start_test.html')

@app.route('/options', methods = ['POST'])
def options_page():
	options = request.form
	with open('data.json', 'w') as f:
		json.dump(options, f)
	return redirect(f'/result')

@app.route('/test')
def question2_page():
	return render_template('test.html')

@app.route('/result')
def result_page():
	return render_template('result.html')

@app.route('/about_us')
def about_us_page():
	return render_template('about_us.html')

@app.route('/gallery')
def gallery_page():
	return render_template('gallery.html')