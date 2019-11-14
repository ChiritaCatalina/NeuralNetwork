from flask import Flask, render_template, flash, request
import wtforms
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import keras
from keras.models import load_model
import numpy as np

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    treapta = wtforms.SelectField('Treapta', choices=[('1','4TLX_accel_80_Nm.sav'),('2','model'),('3','ceva')])
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
        treapta = request.form['treapta']
        if form.validate():
            model = joblib.load('model%s' % treapta)
            scaler = joblib.load('weights%s' % treapta)
            ind = []
            for p in [p1, p2, p3, p4, p5, p6]:
                ind.append(p)
            pred = model.predict(scaler.transform(ind))
            pval = scaler.inverse_transform(pred)
            print(pval)


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