from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template("base.html", title=title)


@app.route('/training/<prof>')
def training(prof):
    if "инженер" in prof or "строитель" in prof:
        type_prof = "Инженерные тренажеры"
        image_dir = url_for('static', filename='img/scientist_train.jpg')
    else:
        type_prof = "Научные симуляторы"
        image_dir = url_for('static', filename='img/engineer_train.jpg')

    return render_template("training.html", title=type_prof, type_prof=type_prof,
                           image_dir=image_dir)

@app.route('/list_prof/<list>')
def list_prof(list):
    list_prof = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач", "инженер по терраформированию",
                 "климатолог", "специалист по радиационной защите", "астрогеолог", "гляциолог",
                 "инженер жизнеобеспечения", "метероолог", "оператор", "кибрпрограммист", "штурман", "пилот дронов"
                 ]
    return render_template("list_prof.html", list_prof=list_prof, types=list)

@app.route('/')
@app.route('/auto_answer')
@app.route('/answer')
def answer():
    person = {'surname': 'Mercenari', 'name': 'ArtloK', 'education': 'high',
              'profession': 'programmist', 'sex': 'male', 'motivation': 'Money',
              'ready': 'True'}
    return render_template("answer.html", title="Анкета", person=person,
                           css=url_for('static', filename='css/answer_style.css'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
