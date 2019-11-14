from flask import Flask, render_template, flash, request
import wtforms
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    p1 = wtforms.DecimalField('P1: ', validators=[validators.required])
    p2 = wtforms.DecimalField('P1: ', validators=[validators.required])
    p3 = wtforms.DecimalField('P1: ', validators=[validators.required])
    p4 = wtforms.DecimalField('P1: ', validators=[validators.required])
    p5 = wtforms.DecimalField('P1: ', validators=[validators.required])
    p6 = wtforms.DecimalField('P1: ', validators=[validators.required])

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    
    print(form.errors)
    if request.method == 'POST':
        p1=request.form['p1']
        p2=request.form['p2']
        p3=request.form['p3']
        p4=request.form['p4']
        p5=request.form['p5']
        p6=request.form['p6']
        if form.validate():
            print('ók')
        print(p1,p2,p3,p4,p5,p6)

    return render_template('hello.html', form=form)


'''    
        if form.validate():
            # Save the comment here.
            flash('Hello ' + p1)
        else:
            flash('All the form fields are required. ')
'''    
   

if __name__ == "__main__":
    app.run()