from os import truncate
from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.wrappers import response
from models import Pessoas, Atividades

app = Flask(__name__)
api  = Api(app)

class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade
            }
        except AttributeError:
            response = {
                'status':'error',
                'aviso':"Pessoa nao encontrada"
            } 
        return response
    
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = str(dados['nome'])
        
        if 'idade' in dados:
            pessoa.idade = int(dados['idade'])

        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome,
            'idade':pessoa.idade
        }
        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = "Pessoa {} excluida com sucesso".format(pessoa.nome)
        pessoa.delete()
        return {
            "status": "Error",
            "mensagem": mensagem
        }

class ListarPessoa(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{"id":i.id,"nome":i.nome,"idade":i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id':pessoa.id,
            'nome':pessoa.nome
        }
        return response 


class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{'id':i.id, 'nome':i.nome, 'pessoa':i.pessoa.nome} for i in atividades ] 
        return response

    def post(self): 
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa':atividade.pessoa.nome,
            'nome':atividade.nome
        }
        return response 

api.add_resource(Pessoa,       '/pessoa/<string:nome>/')
api.add_resource(ListarPessoa, '/pessoa/')
api.add_resource(ListaAtividades, '/atividades/')

if __name__ == '__main__':
    app.run(debug=True)