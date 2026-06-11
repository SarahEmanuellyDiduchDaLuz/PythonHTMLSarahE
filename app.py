from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def início():
    nome = "Turma de programação"
    curso = "Python com HTML"

    return render_template(
        'index.html'
        nome = nome,
        curso = curso
    )