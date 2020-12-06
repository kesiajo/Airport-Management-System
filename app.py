from flask import Flask
from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask import request

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'airport'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_UNIX_SOCKET'] = '/opt/lampp/var/mysql/mysql.sock'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/bookTicket', methods=['GET', 'POST'])
def bookTicket():
    return render_template('book.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == "POST":
        details = request.form
        id = details['empid']
        firstName = details['fname']
        lastName = details['lname']
        addr = details['address']
        job = details['jobtype']
        sex = details['sex']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s)", (id, firstName, lastName, addr, job, sex))
        mysql.connection.commit()
        cur.close()
        msg = "Successfully registered as employee"
    return render_template('employee.html', msg = msg)

if __name__ == '__main__':
    app.run()