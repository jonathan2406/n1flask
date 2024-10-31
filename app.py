from flask import Flask, render_template, redirect, url_for
from datetime import datetime
import random

app = Flask(__name__)

# Valores quemados iniciales
last_update = "2024-10-31 12:00:00"
temperature = 22  # Valor de temperatura en °C
crying = False

@app.route('/')
def index():
    # Renderizamos la página inicial con los valores quemados
    return render_template('index.html', last_update=last_update, temperature=temperature, crying=crying)

@app.route('/update', methods=['POST'])
def update():
    global last_update, temperature, crying
    # Actualizamos los datos con valores aleatorios
    last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temperature = random.randint(18, 35)  # Genera un valor de temperatura aleatorio
    crying = random.choice([True, False])  # Cambia aleatoriamente el estado de crying

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
