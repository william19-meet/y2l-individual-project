from flask import *
from database import *

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def sign_up():
	if request.method == 'POST':
		name = request.form['account_name']
		create_account(name)
		return render_template("question1.html")
	else:
		return render_template("home.html")

@app.route('/people_who_tried', methods = ['GET', 'POST'])
def people_who_failed():
	if request.method == 'GET':
		return render_template('people_who_failed.html',accounts = get_all_accounts())

@app.route('/question1', methods = ['GET', 'POST'])
def question1():
	if request.method == 'POST':
		answer = request.form['answer']
		if answer == '1':
			return render_template('question2.html')
		else:
			return render_template('losing_screen.html')
	else:
		return render_template('question1.html')
@app.route('/question2', methods = ['GET', 'POST'])

def question2():
	if request.method == 'POST':
		answer = request.form['answer']
		if answer == '1':
			return render_template('question3.html')
		else:
			return render_template('losing_screen.html')
@app.route('/question3', methods = ['GET', 'POST'])

def question3():
	if request.method == 'POST':
		answer = request.form['answer']
		if answer == '4':
			return render_template('question4.html')
		else:
			return render_template('losing_screen.html')

@app.route('/question4', methods = ['GET', 'POST'])

def question4():
	if request.method == 'POST':
		answer = request.form['answer']
		if answer == '2':
			return render_template('question5.html')
		else:
			return render_template('losing_screen.html')

@app.route('/question5', methods = ['GET', 'POST'])

def question5():
	if request.method == 'POST':
		answer = request.form['answer']
		if answer == '4':
			return render_template('question6.html')
		else:
			return render_template('losing_screen.html')
@app.route('/question6', methods = ['GET', 'POST'])
def question6():
	if request.method == 'POST':
		answer = request.form['answer']
		if answer == '3':
			return render_template('question7.html')
		else:
			return render_template('losing_screen.html')


@app.route('/question7', methods = ['GET', 'POST'])
def question7():
	if request.method == 'POST':
		answer = request.form['answer']
		if answer == '3':
			return render_template('question8.html')
		else:
			return render_template('losing_screen.html')
@app.route('/question8', methods = ['GET', 'POST'])
def question8():
	if request.method == 'POST':
		answer = request.form['answer']
		if answer == '3':
			return render_template('question9.html')
		else:
			return render_template('losing_screen.html')
@app.route('/question9', methods = ['GET', 'POST'])
def question9():
	if request.method == 'POST':
		answer = request.form['answer']
		if answer == '4':
			return render_template('question10.html')
		else:
			return render_template('losing_screen.html')



@app.route('/question10', methods = ['GET', 'POST'])

def question10():
	if request.method == 'POST':
		answer = request.form['answer']
		print(answer)
		if answer == '2':
			return render_template('winningscreen.html')
		else:
			return render_template('losing_screen.html')
		


if __name__ == '__main__':
    app.run(debug=True)

