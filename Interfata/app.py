import pandas as pd
import numpy as np
from flask import Flask, render_template, flash, request
import wtforms
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import keras
from keras.models import load_model
import numpy as np
from sklearn.externals.joblib import Parallel, delayed
from sklearn.externals import joblib 
from joblib import dump, load
from sklearn.pipeline import make_pipeline
from wtforms import Form, BooleanField, StringField, PasswordField, validators ,SelectField ,DecimalField
from flask_wtf import Form , FlaskForm
from sklearn import preprocessing , svm ,  datasets
from sklearn.preprocessing import MinMaxScaler , StandardScaler
from keras import backend as K
#http://localhost:5000/
# App config.
#imagine doker
DEBUG = True
app = Flask(__name__ , template_folder='template')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

def is_number(s):
    try:
        float(s) # for int, long, float and complex
    except ValueError:
        return False

    return True

class ReusableForm(Form):
    treapta = wtforms.SelectField('Category', choices=[('1','2eme_TLX_accel_80_Nm'),('2','2eme_TLX_retro_-40_Nm'),('3','3eme_TLX_accel_80_Nm'),('4','3eme_TLX_deccel_-40_Nm'),('5','4eme_TLX_accel_80_Nm'),('6','4eme_TLX_retro_-40_Nm'),('7','5eme_TLX_accel_80_Nm'),('8','5eme_TLX_deccel_-40_Nm'),('9','6eme_TLX_retro_-40_Nm'),('10','6eme_TLX_tirage_80_Nm'),('11','PT4_TLX_accel_80_Nm'),('12','PT4_TLX_retro_-40_Nm')])
    p1 = wtforms.DecimalField('fhb1 : ', validators=[validators.required])
    p2 = wtforms.DecimalField('fha1 : ', validators=[validators.required])
    p3 = wtforms.DecimalField('ffa1 : ', validators=[validators.required])
    p4 = wtforms.DecimalField('fhb2 : ', validators=[validators.required])
    p5 = wtforms.DecimalField('fha2 : ', validators=[validators.required])
    p6 = wtforms.DecimalField('ffa2 : ', validators=[validators.required])


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
        value = dict(form.treapta.choices).get(form.treapta.data)
        extension = '.sav'
        if is_number(p1) :
            K.clear_session()
            model = joblib.load('model%s%s' % (value,extension))
            scaler = joblib.load('wheight%s%s' % (value,extension))
            yscaler= joblib.load('y_scalerwheight%s%s' % (value,extension))

            ind = []
            for p in [p1, p2, p3, p4, p5, p6]:
                ind.append(float(p))
        
            q = np.array(ind)
            C = q.reshape(1,6)
            s = scaler.transform(C)
            print(s, s.shape)
            pred = model.predict(s)
    
            print(pred)
            pval =  yscaler.inverse_transform(pred)

            K.clear_session()
            flash('%.2f' %float(pval))
            print(pval)
        else :
             flash('Fill in the fields with numbers!')


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