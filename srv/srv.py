from flask import Flask
from flask import request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        try:
            title = request.form['Title']
            url = request.form['Url']
            cat = request.form['Cat']
            
            with sql.connect("bay.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO bookmarks (title,url,cat) VALUES (?,?,?)",(title,url,cat))     
                          
                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"
        
        finally:
            print(msg)
            return 'ok'
            con.close()    