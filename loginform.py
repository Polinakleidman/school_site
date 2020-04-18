from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, SubmitField, StringField, TextAreaField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('введите ФИО', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    school_class = SelectField('Введите класс, в который поступаете', coerce=str, choices=[('7', '7'), ('8', '8'),
                                                                                        ('9', '9'), ('10', '10'),
                                                                                        ('11','11'), ('0', 'Я учитель')])
    main_subject = SelectField('Выберите направление, на которое поступаете', coerce=str,
                               choices=[('1', 'Биология+химия'), ('2', 'физика+химия'),
                                        ('3', 'физика+математика'), ('4', 'информатика+математика'),
                                        ('5', 'историко-филологическое направление'), ('6', 'Искусство'),
                                        ('0', 'Я учитель')])
    submit = SubmitField('Войти')


class NewsForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    content = TextAreaField("Содержание")
    is_private = BooleanField("Личное")
    submit = SubmitField('Применить')