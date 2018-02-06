from flask import Flask, render_template, request, redirect
from currs.weighted_graph import weighted_graph


app = Flask(__name__)



@app.route('/test', methods=['GET', 'POST'])
def home():

    currs=None

    if request.method == 'POST':
        c = request.form.getlist('currencies')
        w = weighted_graph(c)
        currs = w.curr_df
        currs = currs.to_dict(orient='dict')
        print currs

    return render_template('test.html', currs=currs)



@app.route('/currs', methods=['POST'])
def currs():
    c = request.form.getlist('currencies')
    print c
    if len(c) > 1:
        currs = get_df(c)
        session['currs'] = currs


    return redirect('/test')

'''
@app.route('/home', methods=['GET'])
def home(currs):
    currs = currs.to_dict(orient='dict')
    return render_template('test.html', currs=currs)
'''

def get_df(data):

    w = weighted_graph(data)
    currs = w.curr_df
    currs = currs.to_dict(orient='dict')
    return (currs)




#

if __name__ == '__main__':
    app.run(debug='on')
