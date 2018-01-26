from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/test', methods=['GET', 'POST'])
def home():
    return render_template('test.html')


@app.route('/currs', methods=['POST'])
def currs():

    c = request.form['currencies']

    print (c)

    return redirect('/test')

if __name__ == '__main__':
    app.run(debug='on')
