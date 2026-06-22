from flask import Flask, render_template, request
from src.pokemon_api import get_pokemon_info
from src.database import mostrar_historico, salvar_historico

app = Flask(__name__)

#Pegar infos do pokemon digitado
@app.route('/', methods=['GET', 'POST'])
def home():
    
    pokemon_info= None
    
    if request.method == 'POST':
        pokemon_name = request.form.get('pokemon')
        pokemon_info = get_pokemon_info(pokemon_name)
        
    if pokemon_info:
        salvar_historico(pokemon_info['name'])
    
    return render_template(
        'index.html',
        pokemon_info=pokemon_info
    )

#Mostrar histórico
@app.route('/historico')
def historico():
    
    pesquisas = mostrar_historico()
    
    return render_template(
        'historico.html',
        historico=pesquisas
    )

if __name__ == '__main__':
    app.run(debug=True)