from flask import Flask, render_template, request, redirect
from currs.weighted_graph import weighted_graph
app = Flask(__name__)



@app.route('/test', methods=['GET', 'POST'])
def home():

    return render_template('test.html')


@app.route('/currs', methods=['POST'])
def currs():

    c = request.form.getlist('currencies')
    print c
    if len(c) > 1:
        get_df(c)
    return redirect('/test')

def get_df(data):
    print data
    w = weighted_graph(data)


#

if __name__ == '__main__':
    app.run(debug='on')
