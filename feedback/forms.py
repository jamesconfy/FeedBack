from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

data = ['None', 'James', 'Confidence', 'Praise', 'Honour']

class FeedBack(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=120, min=1)])
    email = EmailField('Email', validators=[DataRequired()])
    feedback = TextAreaField('Feedback', validators=[DataRequired(), Length(min=1)])
    dealer = SelectField('Dealers', choices=data, validators=[DataRequired()], validate_choice=True)
    submit = SubmitField('Submit')