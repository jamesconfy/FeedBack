from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

data = ['None', 'James', 'Confidence', 'Praise', 'Honour']

class FeedBackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=120, min=4)])
    email = EmailField('Email', validators=[DataRequired()])
    feedback = TextAreaField('Feedback', validators=[DataRequired(), Length(min=1)])
    dealer = StringField('Dealers', validators=[DataRequired()]) # ,choices=data, validate_choice=True)
    submit = SubmitField('Submit')