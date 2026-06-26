# 🐍 Pokédex Web API

Aplicação web desenvolvida em Python utilizando Flask.  
O projeto consome a PokéAPI para buscar informações de Pokémons e utiliza MySQL para armazenar o histórico de pesquisas.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-Web-green)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-yellow)
![API](https://img.shields.io/badge/API-PokeAPI-red)

---

## 📌 Funcionalidades

- 🔎 Pesquisa de Pokémons pelo nome
- 🌐 Interface web com Flask
- 📡 Integração com API externa (PokéAPI)
- 💾 Histórico de pesquisas com MySQL
- 📋 Página para visualizar pesquisas anteriores
- ⚠️ Tratamento de erros de conexão
- 🔐 Variáveis de ambiente com `.env`
- 📁 Código separado em módulos

Informações exibidas:

- Foto
- Nome
- ID
- Altura
- Peso
- Habilidades
- Tipo

---

## 🛠 Tecnologias utilizadas

- Python
- Flask
- Requests
- MySQL
- HTML5
- CSS3
- Jinja Templates
- python-dotenv

---

## 📂 Estrutura do projeto

```text
PokeAPI/

├── app.py
│
├── src/
│   ├── database.py
│   └── pokemon_api.py
│
├── templates/
│   ├── index.html
│   └── historico.html
│
├── static/
│   └── style.css
│
├── .env
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

---

## 🚀 Como executar

Clone o repositório:

```bash
git clone https://github.com/PedrReis-create/PokeAPI.git
```

Entre na pasta:

```bash
cd PokeAPI
```

Crie um ambiente virtual (opcional):

```bash
python -m venv venv
```

Ative o ambiente:

Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure o arquivo `.env`:

MySQL

```env
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=seu_banco
DB_PORT=3307
```

Execute:

```bash
python app.py
```

Abra no navegador:

```text
http://127.0.0.1:5000/
```

---

## 🖥 Exemplo de uso

Pesquisa:

```text
pikachu
```

Resultado:

```text
# Foto do pokemon

Nome: Pikachu

ID: 25

Altura: 4

Peso: 60

Habilidades:
Static
Lightning-rod

Tipo:
Electric
```

---

## 📊 Estatísticas do Projeto

![Commits](https://img.shields.io/github/commit-activity/m/PedrReis-create/PokeAPI)

![Último Commit](https://img.shields.io/github/last-commit/PedrReis-create/PokeAPI)

![Tamanho](https://img.shields.io/github/repo-size/PedrReis-create/PokeAPI)

---

## 📈 Próximas melhorias

- 🎨 Melhorar design da interface
- ⭐ Sistema de Pokémons favoritos
- 🔎 Filtros avançados de pesquisa
- 🐳 Docker
- 🚀 Deploy online

---

## 👥 Desenvolvedor

<table>
<tr>

<td align="center">

<a href="https://github.com/PedrReis-create">

<img src="https://github.com/PedrReis-create.png" width="100">

<br>

<b>PedrReis-create</b>

</a>

</td>

</tr>
</table>