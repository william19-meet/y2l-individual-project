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

@app.route('/question1', methods = ['GET', 'POST'])
def question1():
	if request.method == 'POST':
		answer = request.form['answer']
		if answer == 'catdog' or 'dogcat' or 'mistake':
			return render_template('question2.html')
		else:
			return render_template('losing_screen.html')
	else:
		return render_template('question1.html')
@app.route('/question2', methods = ['GET', 'POST'])

def question2():
	if request.method == 'POST':
		answer = request.form['answer']
		print(answer)
		if answer == 'ko':
			return render_template('question3.html')
		else:
			return render_template('losing_screen.html')
@app.route('/question3', methods = ['GET', 'POST'])

def question3():
	if request.method == 'POST':
		answer = request.form['answer']
		print(answer)
		if answer == 'gravity':
			return render_template('question4.html')
		else:
			return render_template('losing_screen.html')
		
@app.route('/question4', methods = ['GET', 'POST'])

def question4():
	if request.method == 'POST':
		answer = request.form['answer']
		print(answer)
		if answer == 'yes' or 'sure' or 'yup':
			return render_template('winningscreen.html')
		else:
			return render_template('losing_screen.html')
		


if __name__ == '__main__':
    app.run(debug=True)

