from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    def __repr__(self):
        return self.username


@app.route("/", methods= ["POST"] )
def main():
    if request.method == "POST":
        id = request.form.get('id')
        password = request.form.get("password")
        user = User(username=id, password=password)
        db.session.add(user)
        db.session.commit()
        data = User.query.all()
        print(data)
        return "<p> this is awsome</p>"

@app.route("/random")
def random():
    users = User.query.all()
    return render_template('users.html', users=users)
if '__name__' == '__main__':
    db.create_all()
    app.run()
