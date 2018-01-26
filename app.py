from flask import Flask, render_template, request, redirect
from currs.weighted_graph import weighted_graph
app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/test', methods=['GET', 'POST'])
def home():
    return render_template('test.html')


@app.route('/currs', methods=['POST'])
def currs():

    c = request.form.getlist('currencies')
    get_df(c)
    return redirect('/test')

def get_df(data):
    w = weighted_graph(data)



if __name__ == '__main__':
    app.run(debug='on')
