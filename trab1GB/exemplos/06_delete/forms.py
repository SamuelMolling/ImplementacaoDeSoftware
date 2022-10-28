from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired()])
    submit = SubmitField('Gravar')

class DeleteTaskForm(FlaskForm):
    submit = SubmitField('Delete')
    cancel = SubmitField('Cancel')