from flask import Flask, render_template, request

app = Flask('MyApp')

@app.route('/') #decorators allow you to execute code and functions at a particular location
def hello():
	return 'Welcome'

@app.route('/<name>')
def hello_someone(name):
	return render_template('index.html', name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
	form_data = request.form
	print (form_data["email"])
	return "All OK"

app.run(debug = True) #it provides extra information that you can use to debug your code yourself