from flask import Flask, render_template, request
from compute import mapp, InputForm


#initializiong flask app
app = Flask(__name__)
app.config['SECRET KEY'] ='IAMNOTTELLINGANYONE'

#creating index page
@app.route("/")
def index():
    return render_template("index.html")

#creating about page
@app.route("/about")
def about():
    return render_template("about.html")

#creating the explore page (actual algorithm works in this page)
@app.route('/explore', methods=['GET', 'POST'])
def explore():
    #intiializing an
    form = InputForm(request.form)
    if request.method == 'POST':
        result = mapp(form.A.data, form.B.data)
    else:
        result = None
    return render_template('view.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
