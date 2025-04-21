from flask import Flask, render_template, request, redirect, url_for
from models import init_db, get_all_entries, add_entry, get_entry, update_entry, delete_entry
import getpass
import jdatetime


app = Flask(__name__)

@app.route('/')
def index():
    user = getpass.getuser()
    entries = get_all_entries()
    return render_template('index.html', entries=entries, username=user)

@app.route('/add', methods=['GET', 'POST'])
def add():
    
    if request.method == 'POST':
        name = request.form['name']
        des = request.form['des']
        edit_by = getpass.getuser()
        edit_date = jdatetime.date.today().strftime("%Y-%m-%d")
        subject = 'none'
        add_entry(name,des,edit_date,edit_by,subject)
        return redirect(url_for('index'))
    return render_template('form.html', action="Add", entry={})

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    entry = get_entry(id)
    if request.method == 'POST':
        name = request.form['name']
        des = request.form['des']
        edit_by = getpass.getuser()
        edit_date = jdatetime.date.today().strftime("%Y-%m-%d")
        subject = 'none'
        update_entry(id, name,des,edit_date,edit_by,subject)
        return redirect(url_for('index'))
    return render_template('form.html', action="Edit", entry=entry)

@app.route('/delete/<int:id>')
def delete(id):
    delete_entry(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)