from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    
    pokemon = ''
    
    if request.method == 'POST':
        pokemon = request.form.get('pokemon')
    
    return render_template(
        'index.html',
        dados = pokemon
    )

if __name__ == '__main__':
    app.run()