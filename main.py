from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

      
        if username == 'hussain' and password == 'password':
      
            return redirect(url_for('home'))
        else:
      
            error_message = 'Invalid username or password. Please try again.'
            return render_template('login.html', error_message=error_message)

    return render_template('login.html')



@app.route('/home')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
