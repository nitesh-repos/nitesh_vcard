from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

# app.route(rule, options)
@app.route('/',methods=['GET','POST'])
def main_render():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        conn = sqlite3.connect('request.db')
        try:
            with sqlite3.connect("database.db") as conn:
                cur = conn.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS usr_request (entryID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, msg TEXT)')
                cur.execute(f'INSERT INTO usr_request (name, email, msg) VALUES ("{name}","{email}","{message}")')
                conn.commit()
                msg = "Record successfully added"
        except:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
    else:
        return render_template('index.html')
        # return redirect(url_for('success',name = user))

if __name__ == '__main__':
    # app.run()
    # app.debug = True
    app.run(debug=True)
    # app.add_url_rule(‘ / ’, ‘hello’, hello_world)