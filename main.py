from flask import Flask, render_template, request, redirect, url_for
from user import getUser

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        valid_user = getUser()
        if valid_user.username == request.form['username'] and valid_user.password == request.form['password']:
              return redirect(url_for('home'))
        else:
            error_message = "Invalid username or password"
            return render_template('login.html',error_message=error_message)
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
