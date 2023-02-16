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

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')