from flask import Flask,render_template,current_user
app=Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/protected')
def protected():
    user = current_user.username  # Assuming you are using Flask-Login
    messages = ["Hello!", "Welcome to your profile.", "Have a great day!"]
    return render_template('protected.html', user=user, messages=messages)

if __name__=="__main__":
    app.run(debug=True,port=6000)