from flask import *
from database import *

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def sign_up():
	if request.method == 'POST':
		name = request.form['account_name']
		create_account(name)
		return render_template("home.html")
	else:
		return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)

