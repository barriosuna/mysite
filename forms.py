from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Dolar Referencia', validators=[DataRequired()])
    password = StringField('Taker fee Criptomkt', validators=[DataRequired()])
    #remember_me = BooleanField('Remember Me')
    submit = SubmitField('Ver')