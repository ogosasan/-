from flask import Flask, render_template
import sqlite3
database = "iu4.db"

app = Flask(__name__)

@app.route('/')
def print_items():
    database = "iu4.db"
    con = sqlite3.connect(database)
    cur = con.cursor()
    cursor = cur.execute('SELECT Country,Capital,Population,Language FROM Countries')
    return render_template('index.html', items=cursor.fetchall())

if __name__ == '__main__':
    app.run()
