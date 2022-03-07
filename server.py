from flask import Flask, render_template, session, request

app = Flask(__name__)

app.secret_key = "password" 

@app.route('/')
def show_survey():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def show_submitted_info():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['fav-language'] = request.form['fav-language']
    session['comment'] = request.form['comment']
    session['type-bootcamp'] = request.form['type-bootcamp']
    session['master-languages'] = request.form.getlist('master-languages')

    return render_template('submitted.html',name=session['name'],location=session['location'],fav_language=session['fav-language'],comment=session['comment'], type_bootcamp=session['type-bootcamp'], master_languages=session['master-languages'])

if __name__ == '__main__':
    app.run(debug=True)