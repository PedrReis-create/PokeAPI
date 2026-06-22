from flask import Flask, render_template, request
from src.pokemon_api import get_pokemon_info


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    
    pokemon_info= None
    
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon')
        pokemon_info = get_pokemon_info(pokemon_name)
    
    return render_template(
        'index.html',
        pokemon_info=pokemon_info
    )

if __name__ == '__main__':
    app.run(debug=True)