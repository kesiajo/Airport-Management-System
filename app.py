from flask import Flask
from flask import flash, render_template, request, redirect
from flask_mysqldb import MySQL
from flask import request
from tables import Results

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
    return render_template('employee.html', msg=msg)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    msg = ''
    if request.method == "POST":
        details = request.form
        user = details['username']
        password = details['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM admin WHERE user = % s AND password = % s', (user, password))
        account = cursor.fetchone()
        if account:
            msg = 'Logged in successfully !'
            return render_template('adminHome.html')
        else:
            msg = 'Incorrect username / password !'

    return render_template('admin.html', msg=msg)


@app.route('/addAirport', methods=['GET', 'POST'])
def addAirport():
    msg = ''
    if request.method == 'POST':
        details = request.form
        name = details['ap_name']
        state = details['state']
        country = details['country']
        city = details['city']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO AIRPORT VALUES (%s, %s, %s, %s)", (name, state, country, city))
        mysql.connection.commit()
        cur.close()
        msg = "Successfully added"
    return render_template('addAirport.html', msg=msg)


@app.route('/addAirline', methods=['GET', 'POST'])
def addAirline():
    msg = ''
    if request.method == 'POST':
        details = request.form
        id = details['a_id']
        name = details['a_name']
        code = details['a_code']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO AIRLINE VALUES (%s, %s, %s)", (id, name, code))
        mysql.connection.commit()
        cur.close()
        msg = "Successfully added"
    return render_template('addAirline.html', msg=msg)


@app.route('/addFlight', methods=['GET', 'POST'])
def addFlight():
    msg = ''
    if request.method == 'POST':
        details = request.form
        code = details['code']
        source = details['source']
        destination = details['dest']
        arrival = details['arr']
        depart = details['dept']
        status = details['status']
        duration = details['duration']
        f_type = details['type']
        layover = details['layover']
        stops = details['stops']
        a_id = details['a_id']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO FLIGHT VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
            code, source, destination, arrival, depart, status, duration, f_type, layover, stops, a_id)
        )
        mysql.connection.commit()
        cur.close()
        msg = "Successfully added"
    return render_template('addFlight.html', msg=msg)


@app.route("/find", methods=['GET'])
def find():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM FLIGHT')
    results = cursor.fetchall()
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        # table = Results(results)
        # table.border = True
        return render_template('flights.html', table=results)

if __name__ == '__main__':
    app.run()