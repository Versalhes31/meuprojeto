from app import app
from flask import render_template, url_for, request, flash
from app.forms import Contato

@app.route('/')
def index():
    return render_template('index.html',titulo = 'Pagina inicial')

@app.route('/contatos', methods=['POST', 'GET'])
def contatos():
    dados_formulario = None
    formulario = Contato()
    print('Acessou a rota contatos')
    if formulario.validate_on_submit():
        
        nome = formulario.nome.data
        email = formulario.email.data
        telefone = formulario.telefone.data
        mensagem = formulario.mensagem.data
        print('o formulario foi validado')
        print(nome)
        print(telefone)
        print(mensagem)
        dados_formulario = {
            'nome': nome,
            'email': email,
            'telefone': telefone,
            'mensagem': mensagem
        }


    return render_template('contatos.html',titulo = 'Contatos', formulario = formulario,dados_formulario = formulario)


@app.route('/sobre')
def sobre():
    return render_template('sobre.html',titulo = 'Sobre')

@app.route('/linguagens')
def linguagens():
    return render_template('linguagens.html',titulo = 'Linguagens')

@app.route('/teste')
def teste():
    return render_template('teste.html')
