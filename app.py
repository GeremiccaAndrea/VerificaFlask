from flask import Flask, request, render_template
app = Flask(__name__)

import pandas as pd 
df = pd.read_csv('/workspace/VerificaFlask/ds1880_studenti_scuola_secondaria_2grado_sudd_indirizzo_statale_as_2020_2021 (1).csv', sep = ";")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/Es1')
def Es1():
    utente = request.args.get('scuola')
    info = df[df['DenominazioneScuola'] == utente ].to_html()
    return render_template('risultato.html', tabella = info )

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)