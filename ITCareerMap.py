from flask import Flask, render_template, request
from compute import mapp
from models import InputForm

app = Flask(__name__)
app.config['SECRET KEY'] ='IAMNOTTELLINGANYONE'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/explore', methods=['GET', 'POST'])
def explore():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = mapp(form.A.data, form.B.data)

    else:
        result = None
    return render_template('view.html', form=form, result=result)


if __name__ == '__main__':
    app.run(debug=True)
