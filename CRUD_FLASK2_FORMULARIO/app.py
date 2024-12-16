from flask import Flask, render_template,request, url_for, redirect, flash
from flask_mysqldb import MySQL
from flask import request

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'contactsdb'
mysql = MySQL(app)


#stting secret key
app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
        mysql.connection.commit()
        flash('Contacto agregado correctamente')
        return redirect(url_for('index'))

@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('editcontact.html', contact = data[0])
    
    
@app.route('/update/<id>', methods = ['POST'])
def update_contact(id):
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE contacts
        SET fullname = %s,
            email = %s,
            phone = %s
        WHERE id = %s
    """, (fullname, email, phone, id))
        mysql.connection.commit()
        flash('Contacto actualizado correctamente')
        return redirect(url_for('index'))
    

@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Contacto eliminado correctamente')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=3000, debug=True)
