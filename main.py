from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

# app.route(rule, options)
# ,methods=['GET','POST']
@app.route('/',methods=['GET','POST'])
def main_render():
    if request.method == 'POST':
        msg = '{"status":"fail"}'
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        try:
            with sqlite3.connect("usr_req_db.db") as conn:
                cur = conn.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS usr_request (entryID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, msg TEXT)')
                cur.execute(f'INSERT INTO usr_request (name, email, msg) VALUES ("{name}","{email}","{message}")')
                conn.commit()
                msg = '{"status":"success"}'
                print(msg)
        except:
            conn.rollback()
            msg = '{"status":"fail","reason":"error in insert operation"}'
            print(msg)
        finally:
            conn.close()
        return msg
    else:
        return render_template('index.html')
        # return redirect(url_for('success',name = user))

if __name__ == '__main__':
    # app.run()
    # app.debug = True
    # app.run(debug=True)
    app.run('207.180.211.78', 8089, debug=True)
    # app.add_url_rule(‘ / ’, ‘hello’, hello_world)