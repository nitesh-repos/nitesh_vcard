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
    else:
        return render_template('index.html')
        # return redirect(url_for('success',name = user))
if __name__ == '__main__':
    # app.run()
    # app.debug = True
    app.run(debug=True)
    # app.add_url_rule(‘ / ’, ‘hello’, hello_world)