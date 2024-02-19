from flask import Flask, render_template, request, redirect, url_for
from project.forms import MessageForm
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
#app.config['SECRET_KEY'] = 'хуёмоё'


@app.route('/')
def index():
    '''Функция корневой страницы возвращает html с параметрами Jinja.'''
    return render_template('index.html',
                           text='text',
                           num=232434340)

@app.route('/area/<float:num>/')
@app.route('/area/<float:num>')
def area_of_a_circle(num: float) -> str:
    '''Функция принимает float в адресной строке и возвращает страницу с площадью круга.'''
    return render_template('area_circle.html',
                           r=num,
                           pi=3.14)

@app.route('/calc/<float:a>/<string:sign>/<float:b>/')
def calculate(a: float, sign: str, b: float) -> str:
    '''Демонстрирует реализацию калькулятора на шаблонизаторе Jinja в html файле.'''
    return render_template('calculate.html', num_1=a, sign=sign, num_2=b)

@app.route('/jinja/')
def jinja_template() -> str:
    '''Демонстрирует решение питоновской задачи силами шаблонизатора Jinja в html файле.'''
    return render_template('jinja.html',
                           numbers={'string': 0,
                                    'f2': 1,
                                    '15': 6,
                                    'g3': -8,
                                    '19': 19,
                                    'b2c5f': 11,
                                    '09': 90})

@app.route('/macros/')
def macros() -> str:
    '''Демонстрирует примем аргументов макросом жижи.'''
    return render_template('res_macros.html', num_1=1, num_2=2, a=34, b=43)

@app.route('/postmail/')
def post_email(email='ppp@ru.ru', message='Hello, Vasya!', title='oke') -> str:
    '''Демонстрирует работу макроса Jinja в html файле.'''
    return render_template('post_email.html', email=email, message=message, title=title)


@app.route('/forms', methods=['GET', 'POST'])
def forms() -> str:
    '''Функция демонстрирует работу форм и запросов.'''
    server_message = ''
    client_message = ''

    if request.method == 'POST':
        client_message = request.form.get('message')
    if client_message == 'Hi':
        server_message = 'Hello!'
    if client_message == '':
        server_message = 'How are you doing?'

    return render_template('sample_forms.html', message=server_message)



@app.route('/message', methods=['GET', 'POST'])
def message() -> str:
    '''Функция представления демонстрирует формы с проверкой на валидность.'''
    name = ''
    email = ''
    text = ''
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        text = form.message.data
        print(name)
        print(email)
        print(text)
        print('\nData received. Now redirection...')
        return redirect(url_for('message'))

    return render_template(
        'message.html',
        form=form,
        name=name,
        email=email,
        text=text,
    )






if __name__ == '__main__':
    app.run(debug=True)