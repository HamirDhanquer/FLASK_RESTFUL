'''
02/07/2021 - Hamir Dhanquer. 
Obs: Estudo de API Restful com Flask. 
'''
from flask import Flask, request 
from flask_restful import Resource, Api 
from habilidades import Habilidades
import json 

app = Flask(__name__)
api = Api(app)

'''
        try:
            response = desenvolvedores[id]
        except IndexError:
            msg = 'Desenvolvedor de ID {} nao existe' .format(id)
            response = {'status':'erro','mensagem':msg}
        except Exception:
            msg = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro','mensagem':msg}
'''
desenvolvedores = [
    {
        'id':0,
        'nome':'Rafael',
        'habilidades':['Python','Flask']
    },
    {
        'id':1,
        'nome':'Hamir Dhanquer',
        'habilidades': ['SQL','SSRS']
    }
]



class Desenvolvedor(Resource):
    def get(self,id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            msg = 'Desenvolvedor de ID {} nao existe' .format(id)
            response = {'status':'erro','mensagem':msg}
        except Exception:
            msg = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro','mensagem':msg}
        return response
    
    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados 
    
    def delete(self,id):
        desenvolvedores.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro Excluido com Sucesso'} 


class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor,'/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
