#Импорт
from flask import Flask, render_template, request

app = Flask(__name__)

#Первая страница
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    #Создай переменные для сбора информации
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    text = request.form['text']
    with open('form.txt', 'a',) as f:
            
            f.write(name + '\n')
            f.write(email + '\n')
            f.write(text + '\n')
            f.write(address + '\n')
            f.close()
    
    # здесь вы можете сохранить данные или отправить их по электронной почте
    return render_template('form_result.html', 
                           #Помести переменные
                           name=name,email=email,address=address,text=text
                           )
app.run(debug=True)