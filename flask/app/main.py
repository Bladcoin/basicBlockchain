from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from block import *

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])


def index():

    if request.method == "POST":
        lender = request.form['sender']
        amount = request.form['amount']
        reciept = request.form['reciept']
        writeBlock(name=lender, amount=amount, to_whom=reciept )
        return redirect( url_for( 'index' ) )
    
    return render_template('index.html')

@app.route('/check')

def check():
    result = blocksCheck()
    return render_template('index.html', results=result )


if __name__ == '__main__':
   app.run(debug=True)